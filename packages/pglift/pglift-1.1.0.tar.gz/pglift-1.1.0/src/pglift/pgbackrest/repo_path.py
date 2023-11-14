from __future__ import annotations

import configparser
import logging
from pathlib import Path

import click
from pgtoolkit import conf as pgconf

from .. import cmd, exceptions, hookimpl, postgresql, types, util
from ..ctx import Context
from ..models import interface, system
from ..settings import Settings, _pgbackrest
from ..task import task
from ..types import BackupType, CompletedProcess
from . import base, models
from . import register_if as base_register_if
from . import role
from .base import get_settings

PathRepository = _pgbackrest.PathRepository
logger = logging.getLogger(__name__)


def register_if(settings: Settings) -> bool:
    if not base_register_if(settings):
        return False
    s = get_settings(settings)
    return isinstance(s.repository, PathRepository)


@hookimpl
def site_configure_install(settings: Settings) -> None:
    s = get_settings(settings)
    base.site_configure_install(settings, base_config(s))
    logger.info("creating pgbackrest repository path")
    repository_settings(s).path.mkdir(exist_ok=True, parents=True)


@hookimpl
def site_configure_uninstall(settings: Settings, ctx: Context) -> None:
    s = get_settings(settings)
    base.site_configure_uninstall(settings)
    util.rmdir(s.configpath)
    rs = repository_settings(s)
    if ctx.confirm(f"Delete pgbackrest repository path {rs.path}?", False):
        logger.info("deleting pgbackrest repository path")
        util.rmtree(rs.path)


@hookimpl
def site_configure_uninstalled(settings: Settings) -> None:
    s = get_settings(settings)
    rs = repository_settings(s)
    for f in (base.config_directory(s), base.base_configpath(s), rs.path):
        if not f.exists():
            raise exceptions.InstallationError(
                f"pgBackRest configuration path {f} missing"
            )


@hookimpl
def instance_configured(
    ctx: Context,
    manifest: interface.Instance,
    config: pgconf.Configuration,
    changes: types.ConfigChanges,
    creating: bool,
    upgrading_from: system.Instance | None,
) -> None:
    with base.instance_configured(
        ctx, manifest, config, changes, creating, upgrading_from
    ) as instance:
        settings = get_settings(instance._settings)
        service_manifest = manifest.service_manifest(models.ServiceManifest)
        service = base.service(instance, service_manifest, settings, upgrading_from)
        if creating and upgrading_from is None and base.enabled(instance, settings):
            if not ctx.confirm(
                f"Stanza {service.stanza!r} already bound to another instance, continue by overwriting it?",
                False,
            ):
                raise exceptions.Cancelled("pgbackrest repository already exists")
            revert_init(service, settings, instance.datadir)
            base.revert_setup(
                ctx, service, settings, config, {}, False, instance.datadir
            )

    if upgrading_from is not None:
        upgrade(service, settings)
    elif creating:
        init(service, settings, instance.datadir)

    if creating and postgresql.is_running(instance):
        password = None
        backup_role = role(instance._settings, manifest)
        assert backup_role is not None
        if backup_role.password is not None:
            password = backup_role.password.get_secret_value()
        if instance.standby:
            logger.warning("not checking pgBackRest configuration on a standby")
        else:
            base.check(instance, service, settings, password)


@hookimpl
def instance_dropped(ctx: Context, instance: system.Instance) -> None:
    with base.instance_dropped(ctx, instance) as service:
        if not service:
            return
        settings = get_settings(instance._settings)
        if not (nb_backups := len(base.backup_info(service, settings)["backup"])) or (
            can_delete_stanza(service, settings, instance.datadir)
            and ctx.confirm(
                f"Confirm deletion of {nb_backups} backup(s) for stanza {service.stanza}?",
                False,
            )
        ):
            delete_stanza(service, settings, instance.datadir)


@hookimpl
def instance_cli(group: click.Group) -> None:
    from .cli import instance_backup

    group.add_command(instance_backup)


def repository_settings(settings: _pgbackrest.Settings) -> PathRepository:
    assert isinstance(settings.repository, PathRepository)
    return settings.repository


def base_config(settings: _pgbackrest.Settings) -> configparser.ConfigParser:
    cp = base.parser()
    cp.read_string(
        util.template("pgbackrest", "pgbackrest.conf").format(**dict(settings))
    )
    s = repository_settings(settings)
    cp["global"]["repo1-path"] = str(s.path)
    for opt, value in s.retention:
        cp["global"][f"repo1-retention-{opt}"] = str(value)
    return cp


@task(title="creating pgBackRest stanza {service.stanza}")
def init(
    service: models.Service,
    settings: _pgbackrest.Settings,
    datadir: Path,
) -> None:
    cmd.run(
        base.make_cmd(service.stanza, settings, "stanza-create", "--no-online"),
        check=True,
    )


@init.revert(title="deleting pgBackRest stanza {service.stanza}")
def revert_init(
    service: models.Service,
    settings: _pgbackrest.Settings,
    datadir: Path,
) -> None:
    if not can_delete_stanza(service, settings, datadir):
        logger.debug(
            "not deleting stanza %s, still used by another instance", service.stanza
        )
        return
    delete_stanza(service, settings, datadir)


def can_delete_stanza(
    service: models.Service, settings: _pgbackrest.Settings, datadir: Path
) -> bool:
    for idx, path in base.stanza_pgpaths(service.path, service.stanza):
        if (idx, path) != (service.index, datadir):
            return False
    return True


def delete_stanza(
    service: models.Service, settings: _pgbackrest.Settings, datadir: Path
) -> None:
    stanza = service.stanza
    cmd.run(base.make_cmd(stanza, settings, "stop"), check=True)
    cmd.run(
        base.make_cmd(
            stanza, settings, "stanza-delete", "--pg1-path", str(datadir), "--force"
        ),
        check=True,
    )


def upgrade(service: models.Service, settings: _pgbackrest.Settings) -> None:
    """Upgrade stanza"""
    stanza = service.stanza
    logger.info("upgrading pgBackRest stanza %s", stanza)
    cmd.run(
        base.make_cmd(stanza, settings, "stanza-upgrade", "--no-online"), check=True
    )


def backup_command(
    instance: system.Instance,
    settings: _pgbackrest.Settings,
    *,
    type: BackupType = BackupType.default(),  # noqa: B008
    start_fast: bool = True,
    backup_standby: bool = False,
) -> list[str]:
    """Return the full pgbackrest command to perform a backup for ``instance``.

    :param type: backup type (one of 'full', 'incr', 'diff').

    Ref.: https://pgbackrest.org/command.html#command-backup
    """
    args = [f"--type={type.name}", "backup"]
    if start_fast:
        args.insert(-1, "--start-fast")
    if backup_standby:
        args.insert(-1, "--backup-standby")
    s = instance.service(models.Service)
    return base.make_cmd(s.stanza, settings, *args)


def backup(
    instance: system.Instance,
    settings: _pgbackrest.Settings,
    *,
    type: BackupType = BackupType.default(),  # noqa: B008
) -> CompletedProcess:
    """Perform a backup of ``instance``.

    :param type: backup type (one of 'full', 'incr', 'diff').

    Ref.: https://pgbackrest.org/command.html#command-backup
    """
    logger.info("backing up instance %s with pgBackRest", instance)
    cmd_args = backup_command(
        instance, settings, type=type, backup_standby=instance.standby is not None
    )
    postgresql_settings = instance._settings.postgresql
    env = postgresql.ctl.libpq_environ(instance, postgresql_settings.backuprole.name)
    return cmd.run(cmd_args, check=True, env=env)
