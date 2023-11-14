from __future__ import annotations

import logging
import pathlib
from unittest.mock import patch

import attrs
import pytest

from pglift import exceptions, instances, postgresql
from pglift.ctx import Context
from pglift.models.system import Instance, PGSetting
from pglift.settings import Settings
from pglift.types import ConfigChanges


def test_system_list_no_instance(settings: Settings) -> None:
    assert list(instances.system_list(settings)) == []


def test_system_list(settings: Settings, pg_version: str, instance: Instance) -> None:
    assert list(map(str, instances.system_list(settings))) == [f"{pg_version}/test"]


def test_system_list_custom_datadir(tmp_path: pathlib.Path, settings: Settings) -> None:
    datadir = tmp_path / "{name}" / "post" / "gres" / "{version}" / "data"
    object.__setattr__(settings.postgresql, "datadir", datadir)

    i1 = pathlib.Path(str(datadir).format(name="foo", version="15"))
    i1.mkdir(parents=True)
    (i1 / "PG_VERSION").write_text("15\n")
    (i1 / "postgresql.conf").touch()
    i2 = pathlib.Path(str(datadir).format(name="bar", version="13"))
    i2.mkdir(parents=True)
    (i2 / "PG_VERSION").write_text("13\n")
    (i2 / "postgresql.conf").touch()
    assert list(map(str, instances.system_list(settings))) == ["13/bar", "15/foo"]


def test_drop(
    ctx: Context, instance: Instance, caplog: pytest.LogCaptureFixture
) -> None:
    with patch.object(ctx, "confirm", return_value=False, autospec=True) as confirm:
        with pytest.raises(exceptions.Cancelled):
            instances.drop(ctx, instance)
    confirm.assert_called_once_with(
        f"Confirm complete deletion of instance {instance}?", True
    )


def test_env_for(ctx: Context, instance: Instance) -> None:
    expected_env = {
        "PGDATA": str(instance.datadir),
        "PGHOST": "/socks",
        "PGPASSFILE": str(ctx.settings.postgresql.auth.passfile),
        "PGPORT": "999",
        "PGUSER": "postgres",
        "PSQLRC": f"{instance.datadir}/.psqlrc",
        "PSQL_HISTORY": f"{instance.datadir}/.psql_history",
        "PGBACKREST_CONFIG_PATH": f"{ctx.settings.prefix}/etc/pgbackrest",
        "PGBACKREST_STANZA": "test-stanza",
    }
    assert instances.env_for(ctx, instance) == expected_env


def test_exec(ctx: Context, instance: Instance) -> None:
    with patch("os.execve", autospec=True) as patched, patch.dict(
        "os.environ", {"PGUSER": "me", "PGPASSWORD": "qwerty"}, clear=True
    ):
        instances.exec(
            ctx, instance, command=("psql", "--user", "test", "--dbname", "test")
        )
    expected_env = {
        "PGDATA": str(instance.datadir),
        "PGPASSFILE": str(ctx.settings.postgresql.auth.passfile),
        "PGPORT": "999",
        "PGUSER": "me",
        "PGHOST": "/socks",
        "PGPASSWORD": "qwerty",
        "PSQLRC": str(instance.psqlrc),
        "PSQL_HISTORY": str(instance.psql_history),
        "PGBACKREST_CONFIG_PATH": f"{ctx.settings.prefix}/etc/pgbackrest",
        "PGBACKREST_STANZA": "test-stanza",
    }

    bindir = instance.bindir
    cmd = [
        f"{bindir}/psql",
        "--user",
        "test",
        "--dbname",
        "test",
    ]
    patched.assert_called_once_with(f"{bindir}/psql", cmd, expected_env)

    with patch("os.execve", autospec=True) as patched:
        instances.exec(ctx, instance, command=("true",))
    assert patched.called

    with patch("os.execve", autospec=True) as patched, pytest.raises(
        exceptions.FileNotFoundError, match="nosuchprogram"
    ):
        instances.exec(ctx, instance, command=("nosuchprogram",))
    assert not patched.called


def test_env(ctx: Context, instance: Instance) -> None:
    bindir = instance.bindir
    with patch.dict("os.environ", {"PATH": "/pg10/bin"}):
        expected_env = [
            f"export PATH={bindir}:/pg10/bin",
            f"export PGBACKREST_CONFIG_PATH={ctx.settings.prefix}/etc/pgbackrest",
            "export PGBACKREST_STANZA=test-stanza",
            f"export PGDATA={instance.datadir}",
            "export PGHOST=/socks",
            f"export PGPASSFILE={ctx.settings.postgresql.auth.passfile}",
            "export PGPORT=999",
            "export PGUSER=postgres",
            f"export PSQLRC={instance.psqlrc}",
            f"export PSQL_HISTORY={instance.psql_history}",
        ]
        assert instances.env(ctx, instance) == "\n".join(expected_env)


def test_exists(settings: Settings, instance: Instance) -> None:
    assert instances.exists(instance.name, instance.version, settings)
    assert not instances.exists("doesnotexists", instance.version, settings)


def test_upgrade_forbid_same_instance(ctx: Context, instance: Instance) -> None:
    with pytest.raises(
        exceptions.InvalidVersion,
        match=f"Could not upgrade {instance.version}/test using same name and same version",
    ):
        instances.upgrade(ctx, instance, version=instance.version)


def test_upgrade_target_instance_exists(ctx: Context, instance: Instance) -> None:
    orig_instance = attrs.evolve(instance, name="old")
    with pytest.raises(exceptions.InstanceAlreadyExists):
        instances.upgrade(
            ctx, orig_instance, version=instance.version, name=instance.name
        )


def test_upgrade_confirm(ctx: Context, instance: Instance, pg_version: str) -> None:
    with patch.object(ctx, "confirm", return_value=False, autospec=True) as confirm:
        with pytest.raises(exceptions.Cancelled):
            instances.upgrade(ctx, instance, name="new", version=pg_version)
    confirm.assert_called_once_with(
        f"Confirm upgrade of instance {instance} to version {pg_version}?",
        True,
    )


def test_standby_upgrade(ctx: Context, standby_instance: Instance) -> None:
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby instance$",
    ):
        instances.upgrade(
            ctx, standby_instance, version=str(int(standby_instance.version) + 1)
        )


def test_non_standby_promote(ctx: Context, instance: Instance) -> None:
    with pytest.raises(
        exceptions.InstanceStateError,
        match=f"^{instance.version}/test is not a standby$",
    ):
        instances.promote(ctx, instance)


def test_check_pending_actions(
    ctx: Context,
    instance: Instance,
    caplog: pytest.LogCaptureFixture,
) -> None:
    _settings = [
        PGSetting(
            name="needs_restart",
            context="postmaster",
            setting="somevalue",
            pending_restart=False,
        ),
        PGSetting(
            name="needs_reload",
            context="sighup",
            setting="somevalue",
            pending_restart=False,
        ),
    ]
    changes: ConfigChanges = {
        "needs_restart": ("before", "after"),
        "needs_reload": ("before", "after"),
    }

    restart_on_changes = True
    with patch.object(
        postgresql, "is_running", return_value=True, autospec=True
    ), patch("pglift.db.connect", autospec=True) as db_connect, patch.object(
        instances, "settings", return_value=_settings, autospec=True
    ) as settings, patch.object(
        instances, "reload", autospec=True
    ) as reload, patch.object(
        ctx, "confirm", return_value=False, autospec=True
    ) as confirm, caplog.at_level(
        logging.INFO
    ):
        instances.check_pending_actions(ctx, instance, changes, restart_on_changes)
    db_connect.assert_called_once_with(instance, ctx=ctx)
    confirm.assert_called_once_with(
        "PostgreSQL needs to be restarted; restart now?", restart_on_changes
    )
    settings.assert_called_once()
    assert (
        f"instance {instance} needs restart due to parameter changes: needs_restart"
        in caplog.messages
    )
    assert (
        f"instance {instance} needs reload due to parameter changes: needs_reload"
        in caplog.messages
    )
    reload.assert_called_once_with(ctx, instance)
