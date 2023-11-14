from __future__ import annotations

import configparser
import io
from collections.abc import Iterator
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pytest
from pgtoolkit.conf import Configuration, parse

from pglift import exceptions, types
from pglift.ctx import Context
from pglift.models import interface
from pglift.models.system import BaseInstance, Instance
from pglift.pgbackrest import base as pgbackrest
from pglift.pgbackrest import (
    models,
    repo_host_ssh,
    repo_host_tls,
    repo_path,
    site_configure_install,
    site_configure_installed,
    site_configure_uninstall,
)
from pglift.settings import Settings, _pgbackrest


@pytest.fixture
def pgbackrest_settings(settings: Settings) -> _pgbackrest.Settings:
    assert settings.pgbackrest is not None
    return settings.pgbackrest


@pytest.fixture
def pgbackrest_site_configure(
    settings: Settings, pgbackrest_settings: _pgbackrest.Settings
) -> Iterator[None]:
    assert not site_configure_installed(settings)
    site_configure_install(settings)
    assert site_configure_installed(settings)
    assert pgbackrest_settings.logpath.exists()
    assert pgbackrest_settings.spoolpath.exists()
    yield
    site_configure_uninstall(settings)
    assert not pgbackrest_settings.logpath.exists()
    assert not pgbackrest_settings.lockpath.exists()


@pytest.mark.usefixtures("pgbackrest_site_configure")
def test_site_configure_base() -> None:
    # Assertions in pgbackrest_site_configure fixture already.
    pass


@pytest.mark.usefixtures("pgbackrest_site_configure")
def test_site_configure_repo_path(
    ctx: Context,
    settings: Settings,
    pgbackrest_settings: _pgbackrest.Settings,
    caplog: pytest.LogCaptureFixture,
) -> None:
    repo_path.site_configure_install(settings)
    assert (pgbackrest_settings.configpath / "pgbackrest.conf").exists()
    config = (
        (pgbackrest_settings.configpath / "pgbackrest.conf").read_text().splitlines()
    )
    assert isinstance(pgbackrest_settings.repository, _pgbackrest.PathRepository)
    assert f"repo1-path = {pgbackrest_settings.repository.path}" in config
    assert "repo1-retention-full = 2" in config
    assert pgbackrest_settings.repository.path.exists()

    include_dir = pgbackrest_settings.configpath / "conf.d"
    assert include_dir.exists()
    leftover = include_dir / "x.conf"
    leftover.touch()
    repo_path.site_configure_uninstall(settings, ctx)
    assert leftover.exists() and include_dir.exists()
    assert pgbackrest_settings.configpath.exists()

    leftover.unlink()

    repo_path.site_configure_uninstall(settings, ctx)
    assert not include_dir.exists()
    assert pgbackrest_settings.repository.path.exists()
    assert not (pgbackrest_settings.configpath / "pgbackrest.conf").exists()

    class YesContext(Context):
        def confirm(self, message: str, default: bool) -> bool:
            return True

    repo_path.site_configure_uninstall(settings, YesContext(settings=settings))
    assert not pgbackrest_settings.repository.path.exists()


def test_setup(
    tmp_path: Path, ctx: Context, pgbackrest_settings: _pgbackrest.Settings
) -> None:
    stanza_path1 = tmp_path / "1.conf"
    datadir1 = tmp_path / "pgdata1"
    service1 = models.Service(stanza="unittests", path=stanza_path1)
    conf = Configuration()
    with pytest.raises(exceptions.SystemError, match="Missing base config file"):
        pgbackrest.setup(ctx, service1, pgbackrest_settings, conf, {}, True, datadir1)

    pgbackrest_settings.logpath.mkdir(parents=True)
    logfile = pgbackrest_settings.logpath / "unittests-123.log"
    logfile.touch()

    baseconfig = pgbackrest.base_configpath(pgbackrest_settings)
    baseconfig.parent.mkdir(parents=True)
    baseconfig.touch()
    pgbackrest.setup(ctx, service1, pgbackrest_settings, conf, {}, True, datadir1)

    datadir2 = tmp_path / "pgdata2"
    service2 = models.Service(stanza="unittests", path=stanza_path1, index=2)
    pgbackrest.setup(
        ctx,
        service2,
        pgbackrest_settings,
        parse(io.StringIO("port=5433\nunix_socket_directories=/tmp\n")),
        {},
        True,
        datadir2,
    )
    assert stanza_path1.read_text().rstrip() == (
        "[unittests]\n"
        f"pg1-path = {datadir1}\n"
        "pg1-port = 5432\n"
        "pg1-user = backup\n"
        f"pg2-path = {datadir2}\n"
        "pg2-port = 5433\n"
        "pg2-user = backup\n"
        "pg2-socket-path = /tmp"
    )

    stanza_path3 = tmp_path / "3.conf"
    datadir3 = tmp_path / "pgdata3"
    service3 = models.Service(stanza="unittests2", path=stanza_path3)
    pgbackrest.setup(ctx, service3, pgbackrest_settings, conf, {}, True, datadir3)
    assert stanza_path3.exists()

    pgbackrest.revert_setup(
        ctx, service1, pgbackrest_settings, conf, {}, False, datadir1
    )
    assert stanza_path1.exists()
    assert stanza_path3.exists()
    assert str(datadir1) not in stanza_path1.read_text()
    assert logfile.exists()
    pgbackrest.revert_setup(
        ctx, service2, pgbackrest_settings, conf, {}, False, datadir2
    )
    assert not stanza_path1.exists()
    assert not logfile.exists()
    assert stanza_path3.exists()
    pgbackrest.revert_setup(
        ctx, service3, pgbackrest_settings, conf, {}, False, datadir3
    )
    assert not stanza_path3.exists()


def test_make_cmd(
    settings: Settings,
    pgbackrest_settings: _pgbackrest.Settings,
    pgbackrest_execpath: Path,
) -> None:
    assert pgbackrest.make_cmd("42-test", pgbackrest_settings, "stanza-upgrade") == [
        str(pgbackrest_execpath),
        f"--config-path={settings.prefix}/etc/pgbackrest",
        "--log-level-stderr=info",
        "--stanza=42-test",
        "stanza-upgrade",
    ]


def test_backup_info(
    settings: Settings,
    pgbackrest_settings: _pgbackrest.Settings,
    pgbackrest_execpath: Path,
    tmp_path: Path,
) -> None:
    with patch("pglift.cmd.run", autospec=True) as run:
        run.return_value.stdout = "[]"
        assert (
            pgbackrest.backup_info(
                models.Service(stanza="testback", path=tmp_path / "mystanza.conf"),
                pgbackrest_settings,
                backup_set="foo",
            )
            == {}
        )
    run.assert_called_once_with(
        [
            str(pgbackrest_execpath),
            f"--config-path={settings.prefix}/etc/pgbackrest",
            "--log-level-stderr=info",
            "--stanza=testback",
            "--set=foo",
            "--output=json",
            "info",
        ],
        check=True,
    )


def test_backup_command(
    instance: Instance,
    settings: Settings,
    pgbackrest_settings: _pgbackrest.Settings,
    pgbackrest_execpath: Path,
) -> None:
    assert repo_path.backup_command(
        instance, pgbackrest_settings, type=types.BackupType.full, backup_standby=True
    ) == [
        str(pgbackrest_execpath),
        f"--config-path={settings.prefix}/etc/pgbackrest",
        "--log-level-stderr=info",
        "--stanza=test-stanza",
        "--type=full",
        "--start-fast",
        "--backup-standby",
        "backup",
    ]


def test_restore_command(
    instance: Instance,
    settings: Settings,
    pgbackrest_settings: _pgbackrest.Settings,
    pgbackrest_execpath: Path,
) -> None:
    with pytest.raises(exceptions.UnsupportedError):
        pgbackrest.restore_command(
            instance, pgbackrest_settings, date=datetime.now(), backup_set="sunset"
        )

    assert pgbackrest.restore_command(instance, pgbackrest_settings) == [
        str(pgbackrest_execpath),
        f"--config-path={settings.prefix}/etc/pgbackrest",
        "--log-level-stderr=info",
        "--stanza=test-stanza",
        "--delta",
        "--link-all",
        "restore",
    ]

    assert pgbackrest.restore_command(
        instance,
        pgbackrest_settings,
        date=datetime(2003, 1, 1).replace(tzinfo=timezone.utc),
    ) == [
        str(pgbackrest_execpath),
        f"--config-path={settings.prefix}/etc/pgbackrest",
        "--log-level-stderr=info",
        "--stanza=test-stanza",
        "--delta",
        "--link-all",
        "--target-action=promote",
        "--type=time",
        "--target=2003-01-01 00:00:00.000000+0000",
        "restore",
    ]

    assert pgbackrest.restore_command(
        instance,
        pgbackrest_settings,
        backup_set="x",
    ) == [
        str(pgbackrest_execpath),
        f"--config-path={settings.prefix}/etc/pgbackrest",
        "--log-level-stderr=info",
        "--stanza=test-stanza",
        "--delta",
        "--link-all",
        "--target-action=promote",
        "--type=immediate",
        "--set=x",
        "restore",
    ]


def test_standby_restore(
    ctx: Context, pgbackrest_settings: _pgbackrest.Settings, standby_instance: Instance
) -> None:
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby",
    ):
        pgbackrest.restore(ctx, standby_instance, pgbackrest_settings)


def test_instance_configure_cancelled_if_repo_exists(
    ctx: Context, instance: Instance, instance_manifest: interface.Instance
) -> None:
    settings = ctx.settings.pgbackrest
    assert settings is not None
    with patch.object(
        pgbackrest, "enabled", return_value=True, autospec=True
    ) as enabled:
        with pytest.raises(exceptions.Cancelled):
            repo_path.instance_configured(
                ctx=ctx,
                manifest=instance_manifest,
                config=Configuration(),
                changes={},
                creating=True,
                upgrading_from=None,
            )
    assert enabled.call_count == 1


def test_stanza_pgpaths(tmp_path: Path) -> None:
    p = tmp_path / "st.conf"
    p.write_text("\n".join(["[s]", "pg1-path = a", "pg3-path = b"]))
    assert list(pgbackrest.stanza_pgpaths(p, "s")) == [(1, Path("a")), (3, Path("b"))]


def test_service(
    pg_version: str,
    settings: Settings,
    instance: Instance,
    instance_manifest: interface.Instance,
    standby_instance: Instance,
    pgbackrest_settings: _pgbackrest.Settings,
) -> None:
    manifest = instance_manifest.service_manifest(models.ServiceManifest)
    # Plain system_lookup().
    s = pgbackrest.service(instance, manifest, pgbackrest_settings, None)

    # Upgrade.
    upgrade_s = pgbackrest.service(instance, manifest, pgbackrest_settings, instance)
    assert upgrade_s == s

    # Creation/update, with stanza from manifest mismatching.
    m = manifest._copy_validate(manifest.dict() | {"stanza": "svc"})
    with pytest.raises(
        exceptions.InstanceStateError,
        match=f"instance {instance} is already bound to pgbackrest stanza 'test-stanza'",
    ):
        pgbackrest.service(instance, m, pgbackrest_settings, None)

    # Another instance, sharing the same stanza (index=2).
    i = BaseInstance("samestanza", pg_version, settings)
    m = manifest._copy_validate(manifest.dict() | {"stanza": s.stanza})
    with s.path.open("a") as f:
        f.write(f"pg2-path = {i.datadir}\n")
    assert pgbackrest.service(i, m, pgbackrest_settings, None) == models.Service(
        s.stanza, s.path, 2
    )

    # Creation.
    s.path.unlink()
    m = manifest._copy_validate(manifest.dict() | {"stanza": "sv"})
    assert pgbackrest.service(instance, m, pgbackrest_settings, None).stanza == "sv"


def test_env_for(
    instance: Instance,
    settings: Settings,
    pgbackrest_settings: _pgbackrest.Settings,
) -> None:
    service = instance.service(models.Service)
    assert pgbackrest.env_for(service, pgbackrest_settings) == {
        "PGBACKREST_CONFIG_PATH": f"{settings.prefix}/etc/pgbackrest",
        "PGBACKREST_STANZA": "test-stanza",
    }


def test_system_lookup(
    pgbackrest_settings: _pgbackrest.Settings, instance: Instance
) -> None:
    stanza_config = (
        pgbackrest.config_directory(pgbackrest_settings)
        / f"{instance.name}-stanza.conf"
    )

    stanza_config.write_text("\nempty\n")
    with pytest.raises(configparser.MissingSectionHeaderError):
        pgbackrest.system_lookup(instance.datadir, pgbackrest_settings)

    stanza_config.write_text("\n[asection]\n")
    assert pgbackrest.system_lookup(instance.datadir, pgbackrest_settings) is None

    other_config = stanza_config.parent / "aaa.conf"
    other_config.write_text(f"[mystanza]\npg42-path = {instance.datadir}\n")
    s = pgbackrest.system_lookup(instance.datadir, pgbackrest_settings)
    assert s is not None and s.path == other_config and s.index == 42
    other_config.unlink()

    stanza_config.write_text(f"[mystanza]\npg1-path = {instance.datadir}\n")
    s = pgbackrest.system_lookup(instance.datadir, pgbackrest_settings)
    assert s is not None and s.stanza == "mystanza" and s.index == 1


def test_repo_host_tls_base_config(tmp_path: Path, pgbackrest_execpath: Path) -> None:
    ca_file = tmp_path / "ca.crt"
    ca_file.touch()
    crt = tmp_path / "pgbackrest.crt"
    crt.touch()
    key = tmp_path / "pgbackrest.key"
    key.touch(mode=0o600)
    settings = _pgbackrest.Settings.parse_obj(
        {
            "execpath": str(pgbackrest_execpath),
            "repository": {
                "mode": "host-tls",
                "host": "backup-srv",
                "host_port": 8433,
                "host_config": "/conf/pgbackrest.conf",
                "cn": "pghost",
                "certificate": {"ca_cert": ca_file, "cert": crt, "key": key},
            },
        }
    )
    cp = repo_host_tls.base_config(settings)
    s = io.StringIO()
    cp.write(s)
    assert s.getvalue().strip().splitlines() == [
        "[global]",
        "lock-path = pgbackrest/lock",
        "log-path = pgbackrest",
        "spool-path = pgbackrest/spool",
        "repo1-host-type = tls",
        "repo1-host = backup-srv",
        "repo1-host-port = 8433",
        "repo1-host-config = /conf/pgbackrest.conf",
        f"repo1-host-ca-file = {ca_file}",
        f"repo1-host-cert-file = {crt}",
        f"repo1-host-key-file = {key}",
    ]
    cp = repo_host_tls.server_config(settings)
    s = io.StringIO()
    cp.write(s)
    assert s.getvalue().strip().splitlines() == [
        "[global]",
        "lock-path = pgbackrest/lock",
        "log-path = pgbackrest",
        "tls-server-address = *",
        "tls-server-auth = pghost=*",
        f"tls-server-ca-file = {ca_file}",
        f"tls-server-cert-file = {crt}",
        f"tls-server-key-file = {key}",
        "tls-server-port = 8432",
    ]


def test_repo_host_tls_systemd_unit_templates(
    settings: Settings,
    pgbackrest_settings: _pgbackrest.Settings,
    pgbackrest_execpath: Path,
) -> None:
    ((name, content),) = list(
        repo_host_tls.systemd_unit_templates(settings=settings, content=True)
    )
    assert name == "pglift-pgbackrest.service"
    lines = content.splitlines()
    configpath = repo_host_tls.server_configpath(pgbackrest_settings)
    assert f"ExecStart={pgbackrest_execpath} server --config={configpath}" in lines
    assert f'Environment="PGPASSFILE={settings.postgresql.auth.passfile}"' in lines


def test_repo_host_ssh_base_config(tmp_path: Path, pgbackrest_execpath: Path) -> None:
    ca_file = tmp_path / "ca.crt"
    ca_file.touch()
    crt = tmp_path / "pgbackrest.crt"
    crt.touch()
    key = tmp_path / "pgbackrest.key"
    key.touch(mode=0o600)
    settings = _pgbackrest.Settings.parse_obj(
        {
            "execpath": str(pgbackrest_execpath),
            "repository": {
                "mode": "host-ssh",
                "host": "backup-srv",
                "host_port": 2222,
                "host_config": "/conf/pgbackrest.conf",
            },
        }
    )
    cp = repo_host_ssh.base_config(settings)
    s = io.StringIO()
    cp.write(s)
    assert s.getvalue().strip().splitlines() == [
        "[global]",
        "lock-path = pgbackrest/lock",
        "log-path = pgbackrest",
        "spool-path = pgbackrest/spool",
        "repo1-host-type = ssh",
        "repo1-host = backup-srv",
        "repo1-host-port = 2222",
        "repo1-host-config = /conf/pgbackrest.conf",
    ]
