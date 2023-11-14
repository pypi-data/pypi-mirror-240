from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, Any
from unittest.mock import MagicMock, patch

import pytest
from pydantic import BaseModel, BaseSettings, Field, ValidationError

from pglift import exceptions
from pglift.settings import (
    Settings,
    SiteSettings,
    _patroni,
    _pgbackrest,
    _postgresql,
    _systemd,
    base,
)


class SubSubSub(BaseModel):
    cfg: Annotated[Path, base.ConfigPath] = Field(default=Path("settings.json"))


class SubSub(BaseModel):
    data: Annotated[Path, base.DataPath] = Field(default=Path("things"))
    config: SubSubSub = SubSubSub()


class Sub(BaseModel):
    sub: SubSub
    pid: Annotated[Path, base.RunPath] = Field(default=Path("pid"))


class S(BaseSettings):
    sub: Sub


def test_prefix_values() -> None:
    bases = {"prefix": Path("/opt"), "run_prefix": Path("/tmp")}
    values = base.prefix_values({"sub": Sub(sub=SubSub())}, bases, S)
    assert S.parse_obj(values).dict() == {
        "sub": {
            "pid": Path("/tmp/pid"),
            "sub": {
                "config": {
                    "cfg": Path("/opt/etc/settings.json"),
                },
                "data": Path("/opt/srv/things"),
            },
        },
    }


def test_json_config_settings_source(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    settings = tmp_path / "settings.json"
    pgbindir = tmp_path / "postgres" / "bin"
    pgbindir.mkdir(parents=True)
    json_settings = json.dumps(
        {
            "postgresql": {
                "versions": [{"version": "15", "bindir": str(pgbindir)}],
                "datadir": "/mnt/postgresql/{version}/{name}/data",
            }
        }
    )
    settings.write_text(json_settings)
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", f"@{settings}")
        s = SiteSettings()
    assert s.postgresql.datadir == Path("/mnt/postgresql/{version}/{name}/data")
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", json_settings)
        s = SiteSettings()
    assert s.postgresql.datadir == Path("/mnt/postgresql/{version}/{name}/data")
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", f"@{tmp_path / 'notfound'}")
        with pytest.raises(FileNotFoundError):
            SiteSettings()


def test_yaml_settings(site_settings: MagicMock, tmp_path: Path) -> None:
    bindir = tmp_path / "pgbin"
    bindir.mkdir()
    configdir = tmp_path / "pglift"
    configdir.mkdir()
    settings_fpath = configdir / "settings.yaml"
    settings_fpath.write_text(
        "\n".join(
            [
                "prefix: /tmp",
                "postgresql:",
                "  versions:",
                "    - version: 15",
                f"      bindir: {bindir}",
            ]
        )
    )
    site_settings.return_value = settings_fpath
    s = SiteSettings()
    assert str(s.prefix) == "/tmp"

    settings_fpath.write_text("hello")
    site_settings.return_value = settings_fpath
    with pytest.raises(exceptions.SettingsError, match="expecting an object"):
        SiteSettings()


def test_custom_sources_order(
    site_settings: MagicMock, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    bindir = tmp_path / "bin"
    bindir.mkdir()
    configdir = tmp_path / "pglift"
    configdir.mkdir()
    settings_fpath = configdir / "settings.yaml"
    settings_fpath.write_text("prefix: /tmp")
    site_settings.return_value = settings_fpath

    with monkeypatch.context() as m:
        m.setenv(
            "SETTINGS",
            json.dumps(
                {
                    "prefix": "/tmp/foo",
                    "postgresql": {
                        "versions": [
                            {"version": 14, "bindir": str(bindir)},
                        ]
                    },
                }
            ),
        )
        s = SiteSettings()
    assert str(s.prefix) == "/tmp/foo"


def test_postgresqlsettings_bindir() -> None:
    with pytest.raises(
        ValidationError, match="missing '{version}' template placeholder"
    ):
        _postgresql.Settings.parse_obj({"bindir": "xxx"})


def test_postgresqlsettings_versions(tmp_path: Path) -> None:
    with pytest.raises(ValidationError, match="either a value is required"):
        _postgresql.Settings.parse_obj({"versions": [], "bindir": None})
    with pytest.raises(ValidationError, match="no value could be inferred"):
        _postgresql.Settings.parse_obj(
            {"versions": [], "bindir": str(tmp_path / "{version}" / "bin")}
        )
    bindir = str(tmp_path / "{version}" / "bin")
    bindir_15 = tmp_path / "15" / "bin"
    bindir_15.mkdir(parents=True)
    s = _postgresql.Settings.parse_obj({"versions": [], "bindir": bindir})
    assert [v.dict() for v in s.versions] == [
        {"bindir": bindir_15, "version": _postgresql.PostgreSQLVersion.v15}
    ]


def test_postgresqlsettings_default_version(tmp_path: Path) -> None:
    with pytest.raises(
        ValidationError, match="value must be amongst declared 'versions': 12"
    ):
        _postgresql.Settings.parse_obj(
            {
                "versions": [{"version": "12", "bindir": str(tmp_path)}],
                "default_version": "13",
                "bindir": str(tmp_path / "{version}" / "bin"),
            }
        )


def test_role_pgpass(bindir_template: str) -> None:
    base = {"bindir": bindir_template}
    with pytest.raises(
        ValidationError, match="cannot set 'pgpass' without 'auth.passfile'"
    ):
        _postgresql.Settings.parse_obj(
            {"auth": {"passfile": None}, "surole": {"pgpass": True}} | base
        )
    assert not _postgresql.Settings.parse_obj(
        {"auth": {"passfile": None}} | base
    ).surole.pgpass


def test_settings(tmp_path: Path, bindir_template: str) -> None:
    s = Settings(prefix="/", postgresql={"bindir": bindir_template})
    assert hasattr(s, "postgresql")
    assert hasattr(s.postgresql, "datadir")
    assert s.postgresql.datadir == Path("/srv/pgsql/{version}/{name}/data")
    assert s.cli.logpath == Path("/log")

    datadir = tmp_path / "{version}" / "{name}"
    s = Settings.parse_obj(
        {
            "prefix": "/prefix",
            "run_prefix": "/runprefix",
            "postgresql": {"bindir": bindir_template, "datadir": str(datadir)},
        }
    )
    assert s.postgresql.datadir == datadir


def test_settings_nested_prefix(
    tmp_path: Path, pgbackrest_execpath: Path, bindir_template: str
) -> None:
    f = tmp_path / "f"
    f.touch()
    s = Settings.parse_obj(
        {
            "run_prefix": "/test",
            "postgresql": {"bindir": bindir_template},
            "pgbackrest": {
                "execpath": str(pgbackrest_execpath),
                "repository": {
                    "mode": "host-tls",
                    "host": "repo",
                    "cn": "test",
                    "certificate": {"ca_cert": f, "cert": f, "key": f},
                    "pid_file": "backrest.pid",
                },
            },
        }
    )
    assert str(s.dict()["pgbackrest"]["repository"]["pid_file"]) == "/test/backrest.pid"


def test_validate_templated_path(bindir_template: str) -> None:
    obj = {"postgresql": {"datadir": "/var/lib/{name}", "bindir": bindir_template}}
    with pytest.raises(
        ValidationError,
        match=r"value contains unknown or missing template variable\(s\); expecting: name, version",
    ):
        Settings.parse_obj(obj)


def test_settings_validate_prefix(postgresql_settings: _postgresql.Settings) -> None:
    with pytest.raises(ValueError, match="expecting an absolute path"):
        Settings(prefix="x", postgresql=postgresql_settings)


def test_settings_validate_service_manager_scheduler(
    postgresql_settings: _postgresql.Settings,
) -> None:
    with pytest.raises(
        ValueError, match="cannot use systemd, if 'systemd' is not enabled globally"
    ):
        Settings(
            service_manager="systemd", postgresql=postgresql_settings
        ).service_manager


@pytest.mark.usefixtures("run_as_root")
def test_settings_as_root() -> None:
    with pytest.raises(
        exceptions.UnsupportedError, match="pglift cannot be used as root"
    ):
        Settings()


def test_postgresql_versions(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    base_bindir = tmp_path / "postgresql"
    base_bindir.mkdir()
    for v in range(13, 16):
        (base_bindir / str(v) / "bin").mkdir(parents=True)
    other_bindir = tmp_path / "pgsql-12" / "bin"
    other_bindir.mkdir(parents=True)
    config: dict[str, Any] = {
        "postgresql": {
            "bindir": str(base_bindir / "{version}" / "bin"),
            "versions": [
                {
                    "version": "12",
                    "bindir": str(other_bindir),
                },
            ],
        },
    }
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(config))
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", f"@{config_path}")
        s = SiteSettings()
    pgversions = s.postgresql.versions
    assert {v.version for v in pgversions} == {"12", "13", "14", "15"}
    assert next(v.bindir for v in pgversions if v.version == "12") == other_bindir
    assert (
        next(v.bindir for v in pgversions if v.version == "13")
        == base_bindir / "13" / "bin"
    )
    config["postgresql"]["default_version"] = "7"
    config_path.write_text(json.dumps(config))
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", f"@{config_path}")
        with pytest.raises(
            ValidationError, match="value is not a valid enumeration member; permitted:"
        ):
            SiteSettings()

    config["postgresql"]["default_version"] = "13"
    config_path.write_text(json.dumps(config))
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", f"@{config_path}")
        s = SiteSettings()
    assert s.postgresql.default_version == "13"

    config["postgresql"]["default_version"] = 7
    config_path.write_text(json.dumps(config))
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", f"@{config_path}")
        with pytest.raises(
            ValidationError, match="value is not a valid enumeration member; permitted:"
        ):
            SiteSettings()

    config["postgresql"]["default_version"] = 13
    config_path.write_text(json.dumps(config))
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", f"@{config_path}")
        s = SiteSettings()
    assert s.postgresql.default_version == "13"


def test_postgresql_dump_restore_commands(bindir_template: str) -> None:
    with pytest.raises(ValidationError) as excinfo:
        _postgresql.Settings.parse_obj(
            {
                "bindir": bindir_template,
                "dump_commands": [
                    ["{bindir}/pg_dump", "--debug"],
                    ["/no/such/file", "{conninfo}"],
                ],
                "restore_commands": [
                    ["not-an-absolute-path", "{dbname}"],
                    ["{bindir}/pg_restore", "ah"],
                ],
            }
        )
    assert excinfo.value.errors() == [
        {
            "loc": ("dump_commands",),
            "msg": "program '/no/such/file' from command #2 does not exist",
            "type": "value_error",
        },
        {
            "loc": ("restore_commands",),
            "msg": "program 'not-an-absolute-path' from command #1 is not an absolute path",
            "type": "value_error",
        },
    ]


def test_systemd_systemctl() -> None:
    with patch("shutil.which", return_value=None, autospec=True) as which:
        with pytest.raises(ValidationError, match="systemctl command not found"):
            _systemd.Settings()
    which.assert_called_once_with("systemctl")


@pytest.mark.usefixtures("systemctl")
def test_systemd_sudo_user() -> None:
    with pytest.raises(ValidationError, match="cannot be used with 'user' mode"):
        _systemd.Settings(user=True, sudo=True)


def test_systemd_disabled(postgresql_settings: _postgresql.Settings) -> None:
    with pytest.raises(ValidationError, match="cannot use systemd"):
        Settings(scheduler="systemd", postgresql=postgresql_settings)
    with pytest.raises(ValidationError, match="cannot use systemd"):
        Settings(service_manager="systemd", postgresql=postgresql_settings)


@pytest.mark.usefixtures("systemctl")
def test_systemd_service_manager_scheduler(
    postgresql_settings: _postgresql.Settings,
) -> None:
    assert (
        Settings(systemd={}, postgresql=postgresql_settings).service_manager
        == "systemd"
    )
    assert (
        Settings(
            systemd={}, service_manager="systemd", postgresql=postgresql_settings
        ).service_manager
        == "systemd"
    )
    assert (
        Settings(
            systemd={}, service_manager=None, postgresql=postgresql_settings
        ).service_manager
        is None
    )


def test_pgbackrest_repository(
    tmp_path: Path, pgbackrest_execpath: Path, bindir_template: str
) -> None:
    f = tmp_path / "f"
    f.touch()
    s = _pgbackrest.Settings.parse_obj(
        {
            "execpath": str(pgbackrest_execpath),
            "repository": {
                "mode": "host-tls",
                "host": "repo",
                "cn": "test",
                "certificate": {"ca_cert": f, "cert": f, "key": f},
            },
        }
    )
    assert isinstance(s.repository, _pgbackrest.HostRepository)

    s = _pgbackrest.Settings.parse_obj(
        {
            "execpath": str(pgbackrest_execpath),
            "repository": {"mode": "path", "path": str(tmp_path)},
        }
    )
    assert isinstance(s.repository, _pgbackrest.PathRepository)

    with pytest.raises(ValidationError, match="repository -> PathRepository -> foo"):
        _pgbackrest.Settings.parse_obj(
            {
                "execpath": str(pgbackrest_execpath),
                "repository": {"mode": "path", "path": str(tmp_path), "foo": 1},
            }
        )
    with pytest.raises(ValidationError, match="repository -> TLSHostRepository -> foo"):
        _pgbackrest.Settings.parse_obj(
            {
                "execpath": str(pgbackrest_execpath),
                "repository": {
                    "mode": "host-tls",
                    "host": "repo",
                    "cn": "test",
                    "certificate": {"ca_cert": f, "cert": f, "key": f},
                    "foo": "bar",
                },
            }
        )


def test_patroni_pgpass(bindir_template: str) -> None:
    with pytest.raises(
        ValidationError,
        match="'patroni.postgresql.passfile' must be different from 'postgresql.auth.passfile'",
    ):
        Settings.parse_obj(
            {
                "postgresql": {
                    "auth": {"passfile": "~/{name}/pgpass"},
                    "bindir": bindir_template,
                },
                "patroni": {"postgresql": {"passfile": "~/{name}/pgpass"}},
            }
        )


def test_patroni_requires_replrole(bindir_template: str) -> None:
    with pytest.raises(
        ValidationError,
        match="'postgresql.replrole' must be provided to use 'patroni'",
    ):
        Settings.parse_obj(
            {
                "postgresql": {
                    "bindir": bindir_template,
                },
                "patroni": {},
            }
        )


def test_patroni_etcd_cert_and_protocol(tmp_path: Path) -> None:
    cacert = tmp_path / "ca.pem"
    cacert.touch()
    with pytest.raises(ValidationError, match="'https' protocol is required"):
        _patroni.Etcd(cacert=cacert)
    _patroni.Etcd(cacert=cacert, protocol="https")
    _patroni.Etcd(protocol="https")


def test_patroni_restapi_verify_client(tmp_path: Path) -> None:
    with pytest.raises(ValidationError, match="requires 'certfile' to enable TLS"):
        _patroni.RESTAPI(verify_client="required")

    certfile = tmp_path / "cert.pem"
    certfile.touch()
    _patroni.RESTAPI(certfile=certfile, verify_client="required")


def test_patroni_restapi_verify_client_ctl(
    bindir_template: str, tmp_path: Path
) -> None:
    certfile = tmp_path / "cert.pem"
    certfile.touch()
    cert = tmp_path / "host.pem"
    cert.touch()
    key = tmp_path / "host.key"
    key.touch()
    with pytest.raises(
        ValidationError,
        match="'ctl' must be provided",
    ):
        _patroni.Settings.parse_obj(
            {
                "restapi": {
                    "certfile": certfile,
                    "verify_client": "required",
                },
            }
        )

    _patroni.Settings.parse_obj(
        {
            "restapi": {
                "certfile": certfile,
                "verify_client": "required",
            },
            "ctl": {
                "certfile": cert,
                "keyfile": key,
            },
        }
    )
