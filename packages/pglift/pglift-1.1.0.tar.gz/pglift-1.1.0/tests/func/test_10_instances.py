from __future__ import annotations

import logging
import re
import socket
from pathlib import Path

import psycopg
import pytest
from pgtoolkit import conf as pgconf

from pglift import databases, exceptions, instances, postgresql, systemd
from pglift.ctx import Context
from pglift.models import interface, system
from pglift.settings import Settings
from pglift.systemd import service_manager
from pglift.types import Status

from .. import CertFactory
from . import (
    AuthType,
    check_connect,
    connect,
    execute,
    passfile_entries,
    running_instance,
)
from .conftest import Factory


def test_directories(instance: system.Instance) -> None:
    assert instance.datadir.exists()
    assert instance.waldir.exists()
    assert (instance.waldir / "archive_status").is_dir()


def test_config(
    instance: system.Instance, instance_manifest: interface.Instance
) -> None:
    postgresql_conf = instance.datadir / "postgresql.conf"
    assert postgresql_conf.exists()
    pgconfig = pgconf.parse(postgresql_conf)
    assert {k for k, v in pgconfig.entries.items() if not v.commented} & set(
        instance_manifest.settings
    )


def test_psqlrc(instance: system.Instance) -> None:
    assert instance.psqlrc.read_text().strip().splitlines() == [
        f"\\set PROMPT1 '[{instance}] %n@%~%R%x%# '",
        "\\set PROMPT2 ' %R%x%# '",
    ]


def test_systemd(ctx: Context, instance: system.Instance) -> None:
    if ctx.settings.service_manager == "systemd":
        assert systemd.is_enabled(
            ctx, service_manager.unit("postgresql", instance.qualname)
        )


def test_pgpass(
    ctx: Context,
    passfile: Path,
    instance_manifest: interface.Instance,
    instance: system.Instance,
    surole_password: str,
    pgbackrest_password: str,
    pgbackrest_available: bool,
) -> None:
    port = instance.port
    backuprole = ctx.settings.postgresql.backuprole.name

    assert passfile_entries(passfile) == [f"*:{port}:*:postgres:{surole_password}"]
    if pgbackrest_available:
        assert passfile_entries(passfile, role=backuprole) == [
            f"*:{port}:*:{backuprole}:{pgbackrest_password}"
        ]


def test_connect(
    ctx: Context,
    instance_manifest: interface.Instance,
    instance: system.Instance,
    postgresql_auth: AuthType,
    surole_name: str,
) -> None:
    check_connect(ctx, postgresql_auth, surole_name, instance_manifest, instance)


def test_replrole(instance: system.Instance) -> None:
    (row,) = execute(
        instance,
        # Simplified version of \du in psql.
        "SELECT rolsuper, rolcanlogin, rolreplication,"
        " ARRAY(SELECT b.rolname"
        "       FROM pg_catalog.pg_auth_members m"
        "       JOIN pg_catalog.pg_roles b ON (m.roleid = b.oid)"
        "       WHERE m.member = r.oid) as memberof"
        " FROM pg_catalog.pg_roles r"
        " WHERE rolname = 'replication'",
    )
    assert row == {
        "rolsuper": False,
        "rolcanlogin": True,
        "rolreplication": True,
        "memberof": ["pg_read_all_stats"],
    }


def test_hba(
    ctx: Context,
    instance_manifest: interface.Instance,
    instance: system.Instance,
    postgresql_auth: AuthType,
) -> None:
    hba_path = instance.datadir / "pg_hba.conf"
    hba = hba_path.read_text().splitlines()
    auth_settings = ctx.settings.postgresql.auth
    auth_instance = instance_manifest.auth
    assert auth_instance is not None
    if postgresql_auth == AuthType.peer:
        assert "peer" in hba[0]
    assert (
        f"local   all             all                                     {auth_settings.local}"
        in hba
    )
    assert (
        f"host    all             all             127.0.0.1/32            {auth_instance.host}"
        in hba
    )
    assert (
        f"hostssl all             all             127.0.0.1/32            {auth_settings.hostssl}"
        in hba
    )


def test_ident(
    ctx: Context, instance: system.Instance, postgresql_auth: AuthType, surole_name: str
) -> None:
    ident_path = instance.datadir / "pg_ident.conf"
    ident = ident_path.read_text().splitlines()
    assert ident[0] == "# MAPNAME       SYSTEM-USERNAME         PG-USERNAME"
    if postgresql_auth == AuthType.peer:
        assert re.match(rf"^test\s+\w+\s+{surole_name}$", ident[1])
    else:
        assert len(ident) == 1


def test_start_stop_restart_running_is_ready_stopped(
    ctx: Context, instance: system.Instance, caplog: pytest.LogCaptureFixture
) -> None:
    i = instance
    assert postgresql.status(i) == Status.running
    assert postgresql.is_ready(i)
    use_systemd = ctx.settings.service_manager == "systemd"
    if use_systemd:
        assert systemd.is_active(ctx, service_manager.unit("postgresql", i.qualname))

    instances.stop(ctx, i)
    try:
        assert postgresql.status(i) == Status.not_running
        assert not postgresql.is_ready(i)
        if use_systemd:
            assert not systemd.is_active(
                ctx, service_manager.unit("postgresql", i.qualname)
            )
        # Stopping a non-running instance is a no-op.
        caplog.clear()
        with caplog.at_level(logging.WARNING, logger="pglift"):
            instances.stop(ctx, i)
        assert f"instance {instance} is already stopped" in caplog.records[0].message
    finally:
        instances.start(ctx, i)

    assert postgresql.status(i) == Status.running
    assert postgresql.is_ready(i)
    if use_systemd:
        assert systemd.is_active(ctx, service_manager.unit("postgresql", i.qualname))

    assert postgresql.status(i) == Status.running
    assert postgresql.is_ready(i)
    if not use_systemd:
        # FIXME: systemctl restart would fail with:
        #   Start request repeated too quickly.
        #   Failed with result 'start-limit-hit'.
        instances.restart(ctx, i)
        assert postgresql.status(i) == Status.running
        assert postgresql.is_ready(i)
    instances.reload(ctx, i)
    assert postgresql.status(i) == Status.running
    assert postgresql.is_ready(i)

    assert postgresql.status(i) == Status.running
    with instances.stopped(ctx, i):
        assert postgresql.status(i) == Status.not_running
        with instances.stopped(ctx, i):
            assert postgresql.status(i) == Status.not_running
            assert not postgresql.is_ready(i)
        with running_instance(ctx, i):
            assert postgresql.status(i) == Status.running
            assert postgresql.is_ready(i)
            with running_instance(ctx, i):
                assert postgresql.status(i) == Status.running
            with instances.stopped(ctx, i):
                assert postgresql.status(i) == Status.not_running
                assert not postgresql.is_ready(i)
            assert postgresql.status(i) == Status.running
            assert postgresql.is_ready(i)
        assert postgresql.status(i) == Status.not_running
    assert postgresql.status(i) == Status.running
    assert postgresql.is_ready(i)


def test_apply(
    ctx: Context,
    pg_version: str,
    tmp_path: Path,
    instance_factory: Factory[tuple[interface.Instance, system.Instance]],
    caplog: pytest.LogCaptureFixture,
    ca_cert: Path,
    cert_factory: CertFactory,
) -> None:
    base_instance = system.BaseInstance.get("test_apply", pg_version, ctx.settings)
    with pytest.raises(exceptions.InstanceNotFound):
        base_instance.check()
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    server_cert = cert_factory(host, common_name=hostname)
    im, i = instance_factory(
        ctx.settings,
        name="test_apply",
        settings={
            "unix_socket_directories": str(tmp_path),
            "ssl": True,
            "ssl_cert_file": str(server_cert.path),
            "ssl_key_file": str(server_cert.private_key),
            "ssl_ca_file": str(ca_cert),
            "log_connections": True,
        },
        auth={"hostssl": "cert"},
        restart_on_changes=False,
        roles=[{"name": "bob", "password": "loooooooooong p3w2d!", "login": True}],
        databases=[
            {"name": "db1", "schemas": [{"name": "sales"}]},
            {
                "name": "db2",
                "owner": "bob",
                "extensions": [{"name": "unaccent", "schema": "public"}],
            },
        ],
        pgbackrest={"stanza": "test_apply_stanza"},
    )
    assert i.port == im.port
    pgconfig = i.config()
    assert pgconfig

    # Re-applying the same manifest is a no-op.
    result_apply = instances.apply(ctx, im)
    assert result_apply.change_state is None

    # Change the runtime state.
    assert postgresql.status(i) == Status.not_running
    im = im._copy_validate({"state": "started"})
    result_apply = instances.apply(ctx, im)
    assert result_apply.change_state == interface.ApplyChangeState.changed
    assert postgresql.status(i) == Status.running
    with connect(i) as conn:
        assert not instances.pending_restart(conn)

    with postgresql.running(ctx, i):
        assert databases.exists(ctx, i, "db1")
        db1 = databases.get(ctx, i, "db1")
        assert db1.schemas[1].name == "sales"
        assert databases.exists(ctx, i, "db2")
        db2 = databases.get(ctx, i, "db2")
        assert db2.extensions[0].name == "unaccent"
        assert db2.owner == "bob"

    # Check SSL client connections
    client_cert = cert_factory("127.0.0.1", common_name="bob")
    connargs = {
        "hostaddr": "127.0.0.1",
        "port": i.port,
        "user": "bob",
        "password": "!!! invalid but unused !!!",
        "dbname": "db2",
        "sslmode": "require",
        "sslrootcert": str(ca_cert),
        "application_name": "pglift-tests-ssl",
    }
    with pytest.raises(
        psycopg.OperationalError, match="connection requires a valid client certificate"
    ):
        psycopg.connect(**connargs)  # type: ignore[call-overload]

    connargs |= {
        "sslmode": "verify-ca",
        "sslcert": str(client_cert.path),
        "sslkey": str(client_cert.private_key),
    }

    expected = [
        "connection authorized: user=bob database=db2 application_name=pglift-tests-ssl SSL enabled",
    ]
    if pg_version >= "14":
        expected.insert(0, 'connection authenticated: identity="CN=bob,OU=Testing cert')
    with psycopg.connect(**connargs) as conn:  # type: ignore[call-overload]
        cur = conn.execute("SHOW ssl")
        assert cur.fetchone() == ("on",)
        logs = []
        try:
            for line in postgresql.logs(i, timeout=0):
                logs.append(line.rstrip())
        except TimeoutError:
            pass
        for line in logs:
            if expected[0] in line:
                del expected[0]
                continue
            if not expected:
                break
        if expected:
            pytest.fail(f"expected log line(s) {expected} not found in {logs}")

    # Change PostgreSQL settings.
    newconfig = im.settings.copy()
    newconfig["listen_addresses"] = "*"  # requires restart
    newconfig["autovacuum"] = False  # requires reload
    im = im._copy_validate({"settings": newconfig})
    with caplog.at_level(logging.DEBUG, logger="pgflit"):
        result_apply = instances.apply(ctx, im)
        assert result_apply.change_state == interface.ApplyChangeState.changed
    assert (
        f"instance {i} needs restart due to parameter changes: listen_addresses"
        in caplog.messages
    )
    assert postgresql.status(i) == Status.running
    with connect(i) as conn:
        assert instances.pending_restart(conn)

    # Change runtime state again.
    im = im._copy_validate({"state": "stopped"})
    result_apply = instances.apply(ctx, im)
    assert result_apply.change_state == interface.ApplyChangeState.changed
    assert postgresql.status(i) == Status.not_running

    # Delete.
    im = im._copy_validate({"state": "absent"})
    assert instances.apply(ctx, im).change_state == interface.ApplyChangeState.dropped
    with pytest.raises(exceptions.InstanceNotFound):
        i.check()
    with pytest.raises(exceptions.InstanceNotFound):
        base_instance.check()


def test_get(
    ctx: Context,
    instance: system.Instance,
    pgbackrest_available: bool,
    powa_available: bool,
) -> None:
    im = instances.get(ctx, instance)
    assert im is not None
    assert im.name == "test"
    config = im.settings
    assert im.port == instance.port
    assert im.data_directory == instance.datadir  # type: ignore[attr-defined]
    assert im.wal_directory == instance.waldir  # type: ignore[attr-defined]
    # Pop host-dependent values.
    del config["effective_cache_size"]
    del config["shared_buffers"]
    spl = "passwordcheck"
    if powa_available:
        spl += ", pg_qualstats, pg_stat_statements, pg_stat_kcache"
    socket_directory = str(ctx.settings.postgresql.socket_directory).format(
        instance=instance
    )
    expected_config = {
        "cluster_name": "test",
        "lc_messages": "C",
        "lc_monetary": "C",
        "lc_numeric": "C",
        "lc_time": "C",
        "log_destination": "stderr",
        "log_directory": str(ctx.settings.postgresql.logpath),
        "log_filename": f"{instance.qualname}-%Y-%m-%d_%H%M%S.log",
        "logging_collector": True,
        "shared_preload_libraries": spl,
        "unix_socket_directories": socket_directory,
    }
    if pgbackrest_available:
        del config["archive_command"]
        expected_config["archive_mode"] = True
        expected_config["wal_level"] = "replica"
    assert config == expected_config
    assert im.data_checksums is False
    assert im.state.name == "started"
    assert not im.pending_restart


def test_ls(settings: Settings, instance: system.Instance) -> None:
    not_instance_dir = Path(
        str(settings.postgresql.datadir).format(version="12", name="notAnInstanceDir")
    )
    not_instance_dir.mkdir(parents=True)
    try:
        ilist = list(instances.ls(settings))

        for i in ilist:
            assert i.status == Status.running.name
            # this also ensure instance name is not notAnInstanceDir
            assert i.name == "test"

        for i in ilist:
            if (i.version, i.name) == (instance.version, instance.name):
                break
        else:
            pytest.fail(f"Instance {instance.version}/{instance.name} not found")

        iv = next(instances.ls(settings, version=instance.version))
        assert iv == i
    finally:
        not_instance_dir.rmdir()


def test_server_settings(instance: system.Instance) -> None:
    with connect(instance) as conn:
        pgsettings = instances.settings(conn)
    port = next(p for p in pgsettings if p.name == "port")
    assert port.setting == str(instance.port)
    assert not port.pending_restart
    assert port.context == "postmaster"


def test_logs(instance: system.Instance) -> None:
    try:
        for line in postgresql.logs(instance, timeout=0):
            if "database system is ready to accept connections" in line:
                break
        else:
            pytest.fail("expected log line not found")
    except TimeoutError:
        pass


def test_get_locale(instance: system.Instance) -> None:
    assert postgresql.is_running(instance)
    with connect(instance) as conn:
        assert instances.get_locale(conn) == "C"


def test_data_checksums(
    ctx: Context,
    pg_version: str,
    instance_factory: Factory[tuple[interface.Instance, system.Instance]],
    caplog: pytest.LogCaptureFixture,
) -> None:
    manifest, instance = instance_factory(ctx.settings, "datachecksums")

    with postgresql.running(ctx, instance):
        assert execute(instance, "SHOW data_checksums") == [{"data_checksums": "off"}]

    # explicitly enabled
    manifest = manifest._copy_validate({"data_checksums": True})
    with caplog.at_level(logging.INFO, logger="pglift.instances"):
        result_apply = instances.apply(ctx, manifest)
        assert result_apply.change_state == interface.ApplyChangeState.changed
    with postgresql.running(ctx, instance):
        assert execute(instance, "SHOW data_checksums") == [{"data_checksums": "on"}]
    assert "enabling data checksums" in caplog.messages
    caplog.clear()

    assert instances._get(ctx, instance, Status.not_running).data_checksums

    # not explicitly disabled so still enabled
    result_apply = instances.apply(
        ctx, manifest._copy_validate({"data_checksums": None})
    )
    assert result_apply.change_state is None
    with postgresql.running(ctx, instance):
        assert execute(instance, "SHOW data_checksums") == [{"data_checksums": "on"}]

    # explicitly disabled
    with caplog.at_level(logging.INFO, logger="pglift.instances"):
        result_apply = instances.apply(
            ctx, manifest._copy_validate({"data_checksums": False})
        )
        assert result_apply.change_state == interface.ApplyChangeState.changed
    with postgresql.running(ctx, instance):
        assert execute(instance, "SHOW data_checksums") == [{"data_checksums": "off"}]
    assert "disabling data checksums" in caplog.messages
    caplog.clear()
    assert instances._get(ctx, instance, Status.not_running).data_checksums is False

    # re-enabled with instance running
    with postgresql.running(ctx, instance):
        with pytest.raises(
            exceptions.InstanceStateError,
            match="cannot alter data_checksums on a running instance",
        ):
            instances.apply(ctx, manifest._copy_validate({"data_checksums": True}))
    assert instances._get(ctx, instance, Status.not_running).data_checksums is False
