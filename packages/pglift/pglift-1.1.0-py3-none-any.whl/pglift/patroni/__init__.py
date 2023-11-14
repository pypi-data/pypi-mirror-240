from __future__ import annotations

import logging
from collections.abc import Iterator
from typing import Any, Literal, NoReturn, Optional

import click
import pgtoolkit.conf
from pydantic import Field

from .. import exceptions, hookimpl, instances, postgresql
from .. import service as service_mod
from .. import systemd, types, util
from ..ctx import Context
from ..models import interface, system
from ..settings import Settings
from . import impl, models
from .impl import available as available
from .impl import get_settings

logger = logging.getLogger(__name__)


def register_if(settings: Settings) -> bool:
    return available(settings) is not None


@hookimpl
def system_lookup(instance: system.BaseInstance) -> models.Service | None:
    settings = get_settings(instance._settings)
    try:
        patroni = models.Patroni.get(instance.qualname, settings)
    except FileNotFoundError:
        return None
    return models.Service(
        cluster=patroni.scope,
        node=patroni.name,
        name=instance.qualname,
        settings=settings,
    )


@hookimpl
def interface_model() -> tuple[str, Any, Any]:
    return (
        models.ServiceManifest.__service__,
        Optional[models.ServiceManifest],
        Field(
            default=None,
            description="Configuration for the Patroni service, if enabled in site settings",
        ),
    )


@hookimpl
def standby_model(instance: system.Instance) -> NoReturn | None:
    if system_lookup(instance) is None:
        return None
    raise ValueError("standby not supported with Patroni")


@hookimpl
def get(instance: system.Instance) -> models.ServiceManifest | None:
    settings = get_settings(instance._settings)
    if (s := system_lookup(instance)) is None:
        return None
    config = models.Patroni.get(instance.qualname, settings)
    cluster_members = impl.cluster_members(instance.qualname, settings)
    return models.ServiceManifest(
        cluster=s.cluster,
        node=s.node,
        postgresql={
            "connect_host": types.address_host(config.postgresql.connect_address)
        },
        restapi=config.restapi,
        cluster_members=cluster_members,
    )


SYSTEMD_SERVICE_NAME = "pglift-patroni@.service"


@hookimpl
def systemd_unit_templates(
    settings: Settings, content: bool
) -> Iterator[str] | Iterator[tuple[str, str]]:
    if not content:
        yield SYSTEMD_SERVICE_NAME
        return
    s = get_settings(settings)
    configpath = str(s.configpath).replace("{name}", "%i")
    yield SYSTEMD_SERVICE_NAME, systemd.template(SYSTEMD_SERVICE_NAME).format(
        executeas=systemd.executeas(settings),
        configpath=configpath,
        execpath=s.execpath,
    )


@hookimpl
def initdb(
    ctx: Context, manifest: interface.Instance, instance: system.BaseInstance
) -> Literal[True] | None:
    """Initialize PostgreSQL database cluster through Patroni by configuring
    Patroni, then starting it (as the only way to get the actual instance
    created).
    """
    settings = get_settings(instance._settings)
    try:
        service_manifest = manifest.service_manifest(models.ServiceManifest)
    except ValueError:
        return None
    configuration = instances.configuration(ctx, manifest, instance)
    with impl.setup(
        ctx,
        instance,
        manifest,
        service_manifest,
        settings,
        configuration,
        validate=True,
    ) as patroni:
        pass
    service = models.Service(
        cluster=patroni.scope,
        name=instance.qualname,
        node=patroni.name,
        settings=settings,
    )
    impl.init(ctx, instance, patroni, service)
    return True


@hookimpl
def configure_postgresql(
    ctx: Context,
    manifest: interface.Instance,
    configuration: pgtoolkit.conf.Configuration,
    instance: system.BaseInstance,
) -> types.ConfigChanges | None:
    """Build and validate Patroni configuration, and return changes to PostgreSQL configuration."""
    settings = get_settings(instance._settings)
    try:
        service = manifest.service_manifest(models.ServiceManifest)
    except ValueError:
        return None
    with impl.setup(
        ctx, instance, manifest, service, settings, configuration
    ) as patroni:
        changes = impl.postgresql_changes(instance.qualname, patroni, settings)
    if changes:
        impl.reload(ctx, instance, settings)
    return changes


@hookimpl
def configure_auth(manifest: interface.Instance) -> Literal[False] | None:
    # In 'patroni' is defined in 'manifest', this is a no-op, since pg_hba.conf
    # and pg_ident.conf are installed through Patroni configuration.
    try:
        manifest.service_manifest(models.ServiceManifest)
    except ValueError:
        return None
    return False


@hookimpl
def postgresql_editable_conf(
    ctx: Context, instance: system.PostgreSQLInstance
) -> str | None:
    settings = get_settings(instance._settings)
    try:
        patroni = models.Patroni.get(instance.qualname, settings)
    except FileNotFoundError:
        return None
    conf = pgtoolkit.conf.Configuration()
    with conf.edit() as entries:
        for k, v in patroni.postgresql.parameters.items():
            entries.add(k, v)
    return "".join(conf.lines)


@hookimpl
def start_postgresql(
    ctx: Context, instance: system.PostgreSQLInstance, foreground: bool, wait: bool
) -> Literal[True] | None:
    """Start PostgreSQL with Patroni."""
    if (service := system_lookup(instance)) is None:
        return None
    impl.start(ctx, service, foreground=foreground)
    if wait:
        postgresql.wait_ready(instance)
    return True


@hookimpl
def stop_postgresql(
    ctx: Context, instance: system.PostgreSQLInstance, deleting: bool
) -> Literal[True] | None:
    """Stop PostgreSQL through Patroni.

    If 'deleting', do nothing as this will be handled upon by Patroni
    deconfiguration.
    """
    if not deleting:
        if (service := system_lookup(instance)) is None:
            return None
        impl.stop(ctx, service)
    return True


@hookimpl
def restart_postgresql(ctx: Context, instance: system.Instance) -> Literal[True] | None:
    """Restart PostgreSQL with Patroni."""
    settings = get_settings(instance._settings)
    if system_lookup(instance) is None:
        return None
    impl.restart(ctx, instance, settings)
    return True


@hookimpl
def reload_postgresql(ctx: Context, instance: system.Instance) -> Literal[True] | None:
    settings = get_settings(instance._settings)
    if system_lookup(instance) is None:
        return None
    impl.reload(ctx, instance, settings)
    return True


@hookimpl
def promote_postgresql(instance: system.PostgreSQLInstance) -> NoReturn | None:
    if system_lookup(instance) is None:
        return None
    raise exceptions.UnsupportedError(
        "unsupported operation: instance managed by Patroni"
    )


@hookimpl
def postgresql_service_name(instance: system.BaseInstance) -> str | None:
    if system_lookup(instance) is None:
        return None
    return "patroni"


@hookimpl
def instance_status(
    ctx: Context, instance: system.Instance
) -> tuple[types.Status, str] | None:
    try:
        service = instance.service(models.Service)
    except ValueError:
        return None
    return (service_mod.status(ctx, service), "Patroni API")


@hookimpl
def instance_dropped(ctx: Context, instance: system.Instance) -> None:
    """Uninstall Patroni from an instance being dropped."""
    if system_lookup(instance) is None:
        return
    service = instance.service(models.Service)
    impl.delete(ctx, service)


@hookimpl
def instance_env(instance: system.Instance) -> dict[str, str]:
    settings = get_settings(instance._settings)
    if (s := system_lookup(instance)) is None:
        return {}
    configpath = impl._configpath(instance.qualname, settings)
    assert configpath.exists()
    return {
        "PATRONI_NAME": s.node,
        "PATRONI_SCOPE": s.cluster,
        "PATRONICTL_CONFIG_FILE": str(configpath),
    }


@hookimpl
def logrotate_config(settings: Settings) -> str:
    s = get_settings(settings)
    return util.template("patroni", "logrotate.conf").format(logpath=s.logpath)


@hookimpl
def cli() -> click.Group:
    from .cli import cli as patroni

    return patroni
