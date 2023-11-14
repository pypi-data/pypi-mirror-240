from __future__ import annotations

import logging
import socket
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pydantic
import pytest
import yaml
from click.testing import CliRunner

from pglift import exceptions, instances
from pglift.cli.util import CLIContext, Obj
from pglift.ctx import Context
from pglift.models import interface, system
from pglift.patroni import (
    configure_postgresql,
    impl,
    instance_env,
    models,
    systemd_unit_templates,
)
from pglift.patroni.cli import cli as cli
from pglift.settings import Settings, _patroni

from . import click_result_traceback


@pytest.fixture
def patroni_settings(settings: Settings) -> _patroni.Settings:
    assert settings.patroni
    return settings.patroni


@pytest.fixture
def instance_manifest(
    composite_instance_model: type[interface.Instance],
) -> interface.Instance:
    return composite_instance_model.parse_obj(
        {
            "name": "test",
            "version": "12",
            "data_checksums": True,
            "settings": {
                "shared_buffers": "257MB",
                "effective_cache_size": "4 GB",
                "unix_socket_directories": "/tmp/tests",
                "log_connections": "on",
                "log_directory": "/tmp/log",
                "log_filename": "patgres-%Y-%m-%d.log",
                "log_disconnections": "false",
                "log_checkpoints": True,
                "log_min_duration_statement": "3s",
                "shared_preload_libraries": "passwordcheck",
            },
            "surole_password": None,
            "replrole_password": "rrr",
            "patroni": {"cluster": "whatever"},
            "pgbackrest": {"stanza": "test-stanza"},
        }
    )


@pytest.fixture
def instance(
    datadir: Path, patroni_settings: _patroni.Settings, instance: system.Instance
) -> system.Instance:
    patroni_config = impl._configpath(instance.qualname, patroni_settings)
    patroni_config.parent.mkdir(parents=True, exist_ok=True)
    patroni_config.write_text((datadir / "patroni.yaml").read_text())
    impl._pgpass(instance.qualname, patroni_settings.postgresql).write_text("# test\n")
    patroni = models.Service(
        cluster="test-scope",
        node="pg1",
        name=instance.qualname,
        settings=patroni_settings,
    )
    instance.services.append(patroni)
    return instance


def test_servicemanifest_defaults() -> None:
    s = models.ServiceManifest(cluster="cluster", node=None, restapi=None)
    assert s.node == socket.getfqdn()
    assert set(s.restapi.dict()) == {"connect_address", "listen"}


def test_available(settings: Settings) -> None:
    assert impl.available(settings)


def test_systemd_unit_templates(settings: Settings, patroni_execpath: Path) -> None:
    ((name, content),) = list(systemd_unit_templates(settings=settings, content=True))
    assert name == "pglift-patroni@.service"
    assert (
        f"ExecStart={patroni_execpath} {settings.prefix}/etc/patroni/%i.yaml" in content
    )


def test_patroni_incompatible_with_standby(
    composite_instance_model: type[interface.Instance],
) -> None:
    with pytest.raises(pydantic.ValidationError):
        composite_instance_model.parse_obj(
            {
                "name": "invalid",
                "standby": {"primary_conninfo": "port=5444"},
                "patroni": {"cluster": "tests"},
            }
        )


def test_patroni_extra_allow() -> None:
    p = models.Patroni.parse_obj(
        {
            "scope": "foo",
            "name": "bar",
            "postgresql": {
                "connect_address": "db.host:4378",
                "listen": "122.78.9.6:5433",
                "parameters": {"log_connections": True},
                "callbacks": {"on_reload": "/my/scripts/reload.sh"},
            },
            "restapi": {
                "connect_address": "api.server:8088",
                "listen": "122.76.9.1:8808",
                "http_extra_headers": {"X-Frame-Options": "SAMEORIGIN"},
            },
            "tags": {"nosync": True},
        }
    ).dict()
    assert p == {
        "scope": "foo",
        "name": "bar",
        "restapi": {
            "connect_address": "api.server:8088",
            "listen": "122.76.9.1:8808",
            "cafile": None,
            "certfile": None,
            "keyfile": None,
            "verify_client": None,
            "http_extra_headers": {"X-Frame-Options": "SAMEORIGIN"},
        },
        "postgresql": {
            "connect_address": "db.host:4378",
            "listen": "122.78.9.6:5433",
            "parameters": {"log_connections": True},
            "callbacks": {"on_reload": "/my/scripts/reload.sh"},
        },
        "tags": {"nosync": True},
    }


def test_servicemanifest_extra_forbid() -> None:
    with pytest.raises(pydantic.ValidationError) as excinfo:
        models.ServiceManifest.parse_obj(
            {
                "cluster": "foo",
                "node": "bar",
                "postgresql": {
                    "connect_host": "db.host:4378",
                    "listen": "122.78.9.6:5433",
                    "parameters": {"log_connections": True},
                },
                "restapi": {
                    "connect_address": "api.server:8088",
                    "listen": "122.76.9.1:8808",
                    "http_extra_headers": {"X-Frame-Options": "SAMEORIGIN"},
                },
                "tags": {"nosync": True},
            }
        )
    assert excinfo.value.errors() == [
        {
            "loc": ("restapi", "http_extra_headers"),
            "msg": "extra fields not permitted",
            "type": "value_error.extra",
        },
        {
            "loc": ("postgresql", "listen"),
            "msg": "extra fields not permitted",
            "type": "value_error.extra",
        },
        {
            "loc": ("postgresql", "parameters"),
            "msg": "extra fields not permitted",
            "type": "value_error.extra",
        },
        {
            "loc": ("tags",),
            "msg": "extra fields not permitted",
            "type": "value_error.extra",
        },
    ]


@pytest.fixture
def patroni(
    ctx: Context,
    tmp_path: Path,
    patroni_settings: _patroni.Settings,
    instance: system.Instance,
    instance_manifest: interface.Instance,
) -> models.Patroni:
    m = instance_manifest._copy_validate(
        {
            "data_checksums": True,
            "surole_password": None,
            "replrole_password": "rrr",
        }
    )
    configuration = instances.configuration(ctx, instance_manifest, instance)
    cacert = tmp_path / "cacert.pem"
    cacert.touch()
    cert = tmp_path / "host.pem"
    cert.touch()
    key = tmp_path / "host.key"
    key.touch()

    with patch(
        "socket.gethostbyname",
        side_effect=AssertionError("gethostbyname unexpectedly called"),
        autospec=True,
    ), patch(
        "pglift.pgbackrest.base.backup_info", return_value={"backup": []}, autospec=True
    ) as backup_info:
        svc = models.ServiceManifest.parse_obj(
            {
                "cluster": "whatever, will be overridden",
                "restapi": {"connect_address": "api.server:8999"},
                "postgresql": {
                    "connect_host": "pghost.test",
                    "replication": {
                        "ssl": {"cert": cert, "key": key, "password": "repsslpwd"}
                    },
                },
            }
        )
        p = models.Patroni.build(
            patroni_settings,
            svc,
            instance,
            m,
            configuration,
            scope="test-scope",
            name="pg1",
            etcd3=(
                patroni_settings.etcd.dict(exclude={"v2"})
                | {
                    "protocol": "https",
                    "cacert": "/path/to/cacert.pem",
                    "cert": "/path/to/host.pem",
                    "key": "/path/to/host.key",
                }
            ),
            watchdog={
                "mode": "required",
                "device": "/dev/watchdog",
                "safety_margin": 5,
            },
            restapi={
                "connect_address": "localhost:8080",
                "cafile": cacert,
                "certfile": cert,
                "keyfile": key,
                "verify_client": "optional",
            },
            ctl={
                "certfile": "/path/to/host.pem",
                "keyfile": "/path/to/host.key",
            },
            postgresql={"pgpass": "/path/to/patroni/test.pgpass"},
        )
    assert backup_info.call_count == 1
    return p


def test_yaml(
    patroni: models.Patroni, datadir: Path, write_changes: bool, tmp_path: Path
) -> None:
    def fake_path_encoder(obj: Any) -> Any:
        if isinstance(obj, Path):
            return obj.name
        raise TypeError

    doc = patroni.yaml(encoder=fake_path_encoder)
    fpath = datadir / "patroni.yaml"
    if write_changes:
        fpath.write_text(doc)

    expected = fpath.read_text()
    assert doc == expected


def test_validate_config(
    patroni: models.Patroni,
    patroni_settings: _patroni.Settings,
    caplog: pytest.LogCaptureFixture,
) -> None:
    with caplog.at_level(logging.WARNING):
        impl.validate_config(patroni.yaml(), patroni_settings)
    (msg,) = caplog.messages
    assert msg.strip() == "invalid Patroni configuration: test test test"


def test_maybe_backup_config(
    instance: system.Instance,
    patroni_settings: _patroni.Settings,
    caplog: pytest.LogCaptureFixture,
) -> None:
    with patch.object(
        impl,
        "cluster_members",
        return_value=[
            models.ClusterMember(
                host="h", name="node", port=8097, role="leader", state="s"
            )
        ],
        autospec=True,
    ):
        with caplog.at_level("WARNING", logger="pglift.patroni"):
            impl.maybe_backup_config(
                instance.qualname, node="node", cluster="clu", settings=patroni_settings
            )
    assert (
        "'node' appears to be the last member of cluster 'clu', saving Patroni configuration file"
        in caplog.messages[0]
    )
    backuppath = next(patroni_settings.configpath.parent.glob("clu-node*.yaml"))
    backupconfig = yaml.safe_load(backuppath.read_text())
    assert backupconfig["etcd3"] == {
        "cacert": "/path/to/cacert.pem",
        "cert": "/path/to/host.pem",
        "hosts": ["etcd1:123", "etcd2:456"],
        "key": "/path/to/host.key",
        "protocol": "https",
    }
    assert backupconfig["restapi"] == {
        "connect_address": "localhost:8080",
        "cafile": "cacert.pem",
        "certfile": "host.pem",
        "keyfile": "host.key",
        "listen": "localhost:8080",
        "verify_client": "optional",
    }
    assert backupconfig["ctl"] == {
        "certfile": "/path/to/host.pem",
        "keyfile": "/path/to/host.key",
    }
    pgpass = next(patroni_settings.configpath.parent.glob("clu-node*.pgpass"))
    assert pgpass.read_text() == "# test\n"


def test_postgresql_service_name(ctx: Context, instance: system.Instance) -> None:
    assert ctx.hook.postgresql_service_name(ctx=ctx, instance=instance) == "patroni"


def test_postgresql_editable_conf(ctx: Context, instance: system.Instance) -> None:
    assert (
        ctx.hook.postgresql_editable_conf(ctx=ctx, instance=instance)
        == "\n".join(
            [
                "archive_command = 'pgbackrest --config-path=/cfg/pgbackrest --stanza=test-stanza --pg1-path=/pg/data archive-push %p'",
                "archive_mode = on",
                "cluster_name = 'test'",
                "effective_cache_size = '4 GB'",
                "lc_messages = 'C'",
                "lc_monetary = 'C'",
                "lc_numeric = 'C'",
                "lc_time = 'C'",
                "log_checkpoints = on",
                "log_connections = on",
                "log_destination = 'syslog'",
                "log_directory = '/tmp/log'",
                "log_disconnections = off",
                "log_filename = 'patgres-%Y-%m-%d.log'",
                "log_min_duration_statement = '3s'",
                "logging_collector = on",
                "shared_buffers = '257MB'",
                "shared_preload_libraries = 'passwordcheck, pg_qualstats, pg_stat_statements, pg_stat_kcache'",
                "syslog_ident = 'postgresql-15-test'",
                "unix_socket_directories = '/tmp/tests'",
                "wal_level = 'replica'",
            ]
        )
        + "\n"
    )


def test_configure_postgresql(
    ctx: Context,
    patroni_settings: _patroni.Settings,
    instance_manifest: interface.Instance,
    instance: system.Instance,
) -> None:
    instance_manifest.settings["work_mem"] = "8MB"
    pgconfig = instances.configuration(ctx, instance_manifest, instance)
    patroni = models.Patroni.get(instance.qualname, patroni_settings)
    postgresql_parameters = patroni.postgresql.parameters.copy()
    assert "work_mem" not in postgresql_parameters
    postgresql_parameters["work_mem"] = "8MB"
    with patch.object(impl, "api_request", autospec=True) as api_request:
        changes = configure_postgresql(ctx, instance_manifest, pgconfig, instance)
    assert changes == {"work_mem": (None, "8MB")}
    (p, verb, endpoint), _ = api_request.call_args
    assert (verb, endpoint) == ("POST", "reload")
    assert p.postgresql.parameters == postgresql_parameters


def test_env(settings: Settings, instance: system.Instance, pg_version: str) -> None:
    assert instance_env(instance) == {
        "PATRONICTL_CONFIG_FILE": f"{settings.prefix}/etc/patroni/{pg_version}-test.yaml",
        "PATRONI_NAME": "pg1",
        "PATRONI_SCOPE": "test-scope",
    }


def test_api_request(patroni: models.Patroni, tmp_path: Path) -> None:
    with patch("httpx.request", autospec=True) as request:
        impl.api_request(patroni, "GET", "readiness")
    request.assert_called_once_with(
        "GET",
        "https://localhost:8080/readiness",
        verify=str(tmp_path / "cacert.pem"),
        cert=(str(tmp_path / "host.pem"), str(tmp_path / "host.key")),
    )


def test_check_api_status(settings: Settings, instance: system.Instance) -> None:
    assert settings.patroni
    assert not impl.check_api_status(instance.qualname, settings.patroni)


def test_promote_postgresql(ctx: Context, instance: system.Instance) -> None:
    assert ctx.settings.patroni
    with pytest.raises(exceptions.UnsupportedError):
        ctx.hook.promote_postgresql(ctx=ctx, instance=instance)


@pytest.mark.usefixtures("installed")
def test_cli_patroni_logs(settings: Settings, instance: system.Instance) -> None:
    runner = CliRunner()
    ctx = CLIContext(settings=settings)
    obj = Obj(context=ctx)
    with patch.object(
        impl, "logs", return_value=["l1\n", "l2\n"], autospec=True
    ) as logs:
        result = runner.invoke(cli, ["-i", str(instance), "logs"], obj=obj)
    assert result.exit_code == 0, click_result_traceback(result)
    logs.assert_called_once_with(instance.qualname, ctx.settings.patroni)
    assert result.output == "l1\nl2\n"


def test_preserve_configuration_edits(
    ctx: Context,
    patroni_settings: _patroni.Settings,
    instance: system.Instance,
    instance_manifest: interface.Instance,
) -> None:
    svc = models.ServiceManifest(cluster="test-scope", node="pg1")

    configpath = impl._configpath(instance.qualname, patroni_settings)
    config = yaml.safe_load(configpath.read_text())
    config["bootstrap"]["dcs"]["loop_wait"] = 42

    # Override a managed field already in settings
    config["restapi"]["verify_client"] = "required"
    # Add an unmanaged "extra" field.
    config["restapi"]["http_extra_headers"] = "Custom-Header-Name: Custom Header Value"

    # PostgreSQL settings only defined in actual Patroni configuration file
    # are preserved.
    assert "work_mem" not in config["postgresql"]["parameters"]
    config["postgresql"]["parameters"]["work_mem"] = "16MB"
    config["postgresql"]["pgpass"] = "/home/db/pgpass"
    with configpath.open("w") as f:
        yaml.safe_dump(config, f)
    m = instance_manifest._copy_validate(update={"port": 5467})
    configuration = instances.configuration(ctx, m, instance)
    with impl.setup(
        ctx, instance, m, svc, patroni_settings, configuration, validate=True
    ) as patroni:
        p = patroni.dict()
        assert p["bootstrap"]["dcs"]["loop_wait"] == 42
        assert p["restapi"]["verify_client"] == "required"
        assert (
            p["restapi"]["http_extra_headers"]
            == "Custom-Header-Name: Custom Header Value"
        )
        assert patroni.postgresql.parameters["work_mem"] == "16MB"
        assert patroni.postgresql.parameters["port"] == 5467
        assert patroni.postgresql.listen == "*:5467"
    config = yaml.safe_load(configpath.read_text())
    assert config["postgresql"]["parameters"]["work_mem"] == "16MB"
    assert config["postgresql"]["pgpass"] == "/home/db/pgpass"

    # PostgreSQL settings from instance manifest take precedence over those
    # defined in actual Patroni configuration file.
    configuration["work_mem"] = "42kB"
    with impl.setup(
        ctx, instance, m, svc, patroni_settings, configuration, validate=True
    ) as patroni:
        assert patroni.postgresql.parameters["work_mem"] == "42kB"
    config = yaml.safe_load(configpath.read_text())
    assert config["postgresql"]["parameters"]["work_mem"] == "42kB"
