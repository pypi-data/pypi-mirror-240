from __future__ import annotations

import concurrent.futures
import getpass
import logging
import pathlib
import platform
import shutil
import socket
import subprocess
from collections.abc import Iterator, Mapping, Sequence
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from typing import Any, Callable, Protocol, TypeVar
from unittest.mock import patch

import pgtoolkit.conf
import psycopg.conninfo
import pytest
from pydantic.utils import deep_update
from typing_extensions import assert_never

from pglift import _install, instances, plugin_manager, postgresql
from pglift.backup import BACKUP_SERVICE_NAME, BACKUP_TIMER_NAME
from pglift.ctx import Context
from pglift.models import interface, system
from pglift.pgbackrest import base as pgbackrest
from pglift.pgbackrest import models as pgbackrest_models
from pglift.postgresql import POSTGRESQL_SERVICE_NAME
from pglift.settings import Settings, _postgresql

from .. import CertFactory
from ..etcd import Etcd
from ..ssh import SSHKeys, add_to_known_hosts
from . import AuthType, PostgresLogger, execute
from .pgbackrest import (
    PgbackrestRepoHost,
    PgbackrestRepoHostSSH,
    PgbackrestRepoHostTLS,
    ServerSSH,
)


def pytest_addoption(parser: Any) -> None:
    parser.addoption(
        "--pg-auth",
        choices=[t.value for t in AuthType],
        default=AuthType.peer.value,
        help="Run tests with PostgreSQL authentication method (default: %(default)s)",
    )
    parser.addoption(
        "--surole-name",
        default="postgres",
        help="Run tests with a specific surole name",
    )
    parser.addoption(
        "--systemd",
        action="store_true",
        default=False,
        help="Run tests with systemd as service manager/scheduler",
    )
    if shutil.which("pgbackrest") is not None:
        parser.addoption(
            "--pgbackrest-repo-host",
            choices=["tls", "ssh"],
            default=None,
            help="Use a dedicated repository host for pgbackrest",
        )


def pytest_report_header(config: Any) -> list[str]:
    systemd = config.option.systemd
    pg_auth = config.option.pg_auth
    surole_name = config.option.surole_name
    pgbackrest_repo_host = config.getoption("pgbackrest_repo_host", False)
    return [
        f"auth method: {pg_auth}",
        f"surole name: {surole_name}",
        f"systemd: {systemd}",
        f"pgbackrest repo host: {pgbackrest_repo_host}",
    ]


def pytest_configure(config: Any) -> None:
    config.addinivalue_line(
        "markers", "standby: mark test as concerning standby instance"
    )


@pytest.fixture(autouse=True)
def journalctl(systemd_requested: bool) -> Iterator[None]:
    journalctl = shutil.which("journalctl")
    if not systemd_requested or journalctl is None:
        yield
        return
    with subprocess.Popen([journalctl, "--user", "-f", "-n0"]) as proc:
        yield
        proc.terminate()


@pytest.fixture(scope="package")
def systemd_available() -> bool:
    try:
        subprocess.run(
            ["systemctl", "--user", "status"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False
    return True


@pytest.fixture(scope="package")
def postgres_logger(logger: logging.Logger) -> Iterator[PostgresLogger]:
    """Register an 'instance' to stream its log to the test logger."""
    executor = concurrent.futures.ThreadPoolExecutor()

    def submit(instance: system.PostgreSQLInstance) -> None:
        def postgres_logs(instance: system.PostgreSQLInstance) -> None:
            for line in postgresql.logs(instance):
                logger.debug("%s: %s", instance, line.rstrip())

        executor.submit(postgres_logs, instance)

    yield submit

    executor.shutdown(wait=False, cancel_futures=True)


@pytest.fixture(scope="package")
def powa_available(no_plugins: bool, pg_bindir: tuple[pathlib.Path, str]) -> bool:
    if no_plugins:
        return False
    pg_config = pg_bindir[0] / "pg_config"
    result = subprocess.run(
        [pg_config, "--pkglibdir"], stdout=subprocess.PIPE, check=True, text=True
    )
    pkglibdir = pathlib.Path(result.stdout.strip())
    return (
        (pkglibdir / "pg_qualstats.so").exists()
        and (pkglibdir / "pg_stat_kcache.so").exists()
        and (pkglibdir / "powa.so").exists()
    )


@pytest.fixture(scope="package")
def systemd_requested(request: Any, systemd_available: bool) -> bool:
    value = request.config.option.systemd
    assert isinstance(value, bool)
    if value and not systemd_available:
        raise pytest.UsageError("systemd is not available on this system")
    return value


@pytest.fixture(scope="package")
def postgresql_auth(request: Any) -> AuthType:
    return AuthType(request.config.option.pg_auth)


def ssh_command(path: Path, key: Path) -> Path:
    cmdfile = path / "sshcmd"
    with cmdfile.open("w") as f:
        f.write(
            dedent(
                f"""\
                #!/bin/sh
                /usr/bin/ssh -i {key} -o StrictHostKeyChecking=no "$@"
                """
            )
        )
    cmdfile.chmod(0o700)
    return cmdfile


@pytest.fixture(scope="package")
def pgbackrest_repo_host(
    request: Any,
    postgresql_auth: AuthType,
    pgbackrest_execpath: Path | None,
    ca_cert: Path,
    cert_factory: CertFactory,
    tmp_path_factory: pytest.TempPathFactory,
    tmp_port_factory: Iterator[int],
    logger: logging.Logger,
) -> Iterator[PgbackrestRepoHost | None]:
    option = request.config.option.pgbackrest_repo_host
    if not option:
        yield None
        return

    assert pgbackrest_execpath is not None
    repo_path = tmp_path_factory.mktemp("pgbackrest-repo")
    logpath = repo_path / "logs"
    logpath.mkdir()
    hostname = socket.getfqdn()
    if option == "tls":
        repo_cert = cert_factory(common_name=hostname)
        with PgbackrestRepoHostTLS(
            client_configpath=repo_path / "pgbackrest.conf",
            server_configpath=repo_path / "server.conf",
            logpath=logpath,
            port=next(tmp_port_factory),
            path=repo_path / "backups",
            repo_cn=hostname,
            dbhost_cn=hostname,
            ca_file=ca_cert,
            repo_certfile=repo_cert.path,
            repo_keyfile=repo_cert.private_key,
            logger=logger,
        ) as r:
            yield r
    elif option == "ssh":
        if postgresql_auth != AuthType.peer:
            pytest.skip("pgbackrest SSH repository requires 'peer' authentication mode")
        dbhost_port = next(tmp_port_factory)
        dbhost_ssh_path = tmp_path_factory.mktemp("pgbackrest-client") / "ssh"

        # exchange keys
        dbhost_keys = SSHKeys.make(dbhost_ssh_path)
        repo_keys = SSHKeys.make(repo_path)
        (dbhost_ssh_path / "authorized_keys").write_text(
            "no-agent-forwarding,no-X11-forwarding,no-port-forwarding,"
            f"command=\"sh -c '{pgbackrest_execpath} ${{SSH_ORIGINAL_COMMAND#* }}'\" "
            f"{repo_keys.public_key.read_text()}"
        )
        (repo_path / "authorized_keys").write_text(
            "no-agent-forwarding,no-X11-forwarding,no-port-forwarding,"
            f"command=\"sh -c '{pgbackrest_execpath} ${{SSH_ORIGINAL_COMMAND#* }}'\" "
            f"{dbhost_keys.public_key.read_text()}"
        )

        with ServerSSH(
            host_keyfile=dbhost_keys.host_key,
            port=dbhost_port,
            ssh_path=dbhost_ssh_path,
        ):
            add_to_known_hosts(repo_path, hostname, dbhost_port)
            repo_port = next(tmp_port_factory)
            with PgbackrestRepoHostSSH(
                client_configpath=repo_path / "pgbackrest.conf",
                host_keyfile=repo_keys.host_key,
                user_keyfile=repo_keys.private_key,
                logpath=logpath,
                port=repo_port,
                ssh_path=repo_path,
                cmd_ssh=ssh_command(repo_path, repo_keys.private_key),
                dbhost_port=dbhost_port,
                dbhost_user_keyfile=dbhost_keys.private_key,
                dbhost_cmd_ssh=ssh_command(dbhost_ssh_path, dbhost_keys.private_key),
                path=repo_path / "backups",
                dbhost_host=hostname,
                logger=logger,
            ) as r:
                add_to_known_hosts(dbhost_ssh_path, hostname, repo_port)
                yield r
    else:
        assert_never(option)


@pytest.fixture(scope="package")
def site_config(
    site_config: Callable[..., str], postgresql_auth: AuthType
) -> Iterator[Callable[..., str | None]]:
    if postgresql_auth == AuthType.peer:
        datadir = pathlib.Path(__file__).parent / "data" / "peer"
    else:
        datadir = pathlib.Path(__file__).parent / "data" / "base"

    def test_site_config(*args: str) -> str | None:
        """Lookup for configuration files in local data director first."""
        fpath = datadir.joinpath(*args)
        if fpath.exists():
            return fpath.read_text()
        return site_config(*args)

    with patch("pglift.util.site_config", new=test_site_config) as fn:
        yield fn


@pytest.fixture(scope="package")
def postgresql_settings(
    tmp_path_factory: pytest.TempPathFactory,
    postgresql_auth: AuthType,
    surole_name: str,
    surole_password: str | None,
    pgbackrest_password: str | None,
) -> _postgresql.Settings:
    """Factory to create a _postgresql.Settings instance with distinct files
    (.pgpass or password_command file) from other instances.
    """
    auth: dict[str, Any] = {
        "local": "password",
        "passfile": None,
    }
    surole: dict[str, Any] = {"name": surole_name}
    backuprole: dict[str, Any] = {"name": "backup"}
    if postgresql_auth == AuthType.peer:
        pass
    elif postgresql_auth == AuthType.password_command:
        passcmdfile = tmp_path_factory.mktemp("home") / "passcmd"
        auth["password_command"] = [str(passcmdfile), "{instance}", "{role}"]
        with passcmdfile.open("w") as f:
            f.write(
                dedent(
                    f"""\
                    #!/bin/sh
                    instance=$1
                    role=$2
                    if [ ! "$instance" ]
                    then
                        echo "no instance given!!" >&2
                        exit 1
                    fi
                    if [ ! "$role" ]
                    then
                        echo "no role given!!" >&2
                        exit 1
                    fi
                    if [ "$role" = {surole["name"]} ]
                    then
                        echo "retrieving password for $role for $instance..." >&2
                        echo {surole_password}
                        exit 0
                    fi
                    if [ "$role" = {backuprole["name"]} ]
                    then
                        echo "retrieving password for $role for $instance..." >&2
                        echo {pgbackrest_password}
                        exit 0
                    fi
                    """
                )
            )
        passcmdfile.chmod(0o700)
    elif postgresql_auth == AuthType.pgpass:
        passfile = tmp_path_factory.mktemp("home") / ".pgpass"
        passfile.touch(mode=0o600)
        auth["passfile"] = str(passfile)
        surole["pgpass"] = True
        backuprole["pgpass"] = True
    else:
        raise AssertionError(f"unexpected {postgresql_auth}")
    return _postgresql.Settings.parse_obj(
        {
            "auth": auth,
            "surole": surole,
            "backuprole": backuprole,
            "replrole": "replication",
        }
    )


@pytest.fixture(scope="package")
def passfile(
    postgresql_auth: AuthType, postgresql_settings: _postgresql.Settings
) -> pathlib.Path:
    if postgresql_auth != AuthType.pgpass:
        pytest.skip(f"not applicable for auth:{postgresql_auth}")
    p = postgresql_settings.auth.passfile
    assert p is not None
    return p


@pytest.fixture(scope="package")
def settings(
    tmp_path_factory: pytest.TempPathFactory,
    postgresql_settings: _postgresql.Settings,
    systemd_requested: bool,
    systemd_available: bool,
    patroni_execpath: pathlib.Path | None,
    etcd_host: Etcd,
    pgbackrest_execpath: pathlib.Path | None,
    pgbackrest_repo_host: PgbackrestRepoHost | None,
    ca_cert: Path,
    cert_factory: CertFactory,
    prometheus_execpath: pathlib.Path | None,
    powa_available: bool,
    temboard_execpath: pathlib.Path | None,
    tmp_port_factory: Iterator[int],
) -> Settings:
    prefix = tmp_path_factory.mktemp("prefix")
    (prefix / "run" / "postgresql").mkdir(parents=True)
    obj = {
        "prefix": str(prefix),
        "run_prefix": str(tmp_path_factory.mktemp("run")),
        "postgresql": postgresql_settings.dict(),
    }
    if systemd_requested:
        obj.update({"systemd": {}})

    if patroni_execpath:
        host = socket.gethostbyname(socket.gethostname())
        restapi_cert = cert_factory(host)
        ctl_cert = cert_factory(host)
        obj["patroni"] = {
            "execpath": str(patroni_execpath),
            "loop_wait": 1,
            "etcd": {
                "hosts": [etcd_host.endpoint],
                "protocol": "https",
                "cacert": ca_cert,
            },
            "postgresql": {
                "connection": {
                    "ssl": {
                        "mode": "verify-ca",
                        "rootcert": ca_cert,
                    },
                },
            },
            "restapi": {
                "cafile": ca_cert,
                "certfile": restapi_cert.path,
                "keyfile": restapi_cert.private_key,
                "verify_client": "required",
            },
            "ctl": {
                "certfile": ctl_cert.path,
                "keyfile": ctl_cert.private_key,
            },
        }

    if pgbackrest_execpath is not None:
        hostname = socket.getfqdn()
        if isinstance(pgbackrest_repo_host, PgbackrestRepoHostTLS):
            pgbackrest_dbhost_cert = cert_factory(
                common_name=pgbackrest_repo_host.dbhost_cn
            )
            pgbackrest_repository = {
                "mode": "host-tls",
                "host": hostname,
                "host_port": pgbackrest_repo_host.port,
                "host_config": pgbackrest_repo_host.client_configpath,
                "cn": pgbackrest_repo_host.repo_cn,
                "certificate": {
                    "ca_cert": ca_cert,
                    "cert": pgbackrest_dbhost_cert.path,
                    "key": pgbackrest_dbhost_cert.private_key,
                },
                "port": next(tmp_port_factory),
            }
        elif isinstance(pgbackrest_repo_host, PgbackrestRepoHostSSH):
            pgbackrest_repository = {
                "mode": "host-ssh",
                "host": hostname,
                "host_port": pgbackrest_repo_host.port,
                "host_config": pgbackrest_repo_host.client_configpath,
                "host_user": getpass.getuser(),
                "cmd_ssh": pgbackrest_repo_host.dbhost_cmd_ssh,
            }
        else:
            assert pgbackrest_repo_host is None
            pgbackrest_repository = {
                "mode": "path",
                "path": tmp_path_factory.mktemp("backups"),
            }
        obj["pgbackrest"] = {
            "execpath": pgbackrest_execpath,
            "repository": pgbackrest_repository,
        }

    if prometheus_execpath:
        obj["prometheus"] = {"execpath": prometheus_execpath}

    if powa_available:
        obj["powa"] = {}

    if temboard_execpath:
        temboard_signing_key = (
            tmp_path_factory.mktemp("temboard-agent") / "signing-public.pem"
        )
        temboard_cert = cert_factory("0.0.0.0")
        obj["temboard"] = {
            "execpath": temboard_execpath,
            "ui_url": "https://0.0.0.0:8888",
            "signing_key": temboard_signing_key,
            "certificate": {
                "ca_cert": ca_cert,
                "cert": temboard_cert.path,
                "key": temboard_cert.private_key,
            },
            "logmethod": "file",
        }
        temboard_signing_key.write_text(
            "-----BEGIN PUBLIC KEY-----\n"
            "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQChaZFhzRuFgNDLgAJ2+WQsVQ75\n"
            "G9UswuVxTfltxP4mc+ou8lyj7Ck73+M3HkFE2r623g6DZcNYCXqpyNpInsBo68kD\n"
            "IDgwHKaQBTPyve0VhNjkJyqoKIC6AJKv/wixEwsHUm/rNU8cXnY7WCNGjCV+JrEm\n"
            "ekHBWP1X4hFfPKcvvwIDAQAB\n"
            "-----END PUBLIC KEY-----"
        )

    return Settings.parse_obj(obj)


@pytest.fixture
def ctx(settings: Settings) -> Context:
    return Context(settings=settings)


@pytest.fixture(scope="package")
def require_systemd_scheduler(settings: Settings) -> None:
    if settings.scheduler != "systemd":
        pytest.skip("not applicable for scheduler method other than 'systemd'")


@pytest.fixture(scope="package")
def require_pgbackrest_localrepo(
    settings: Settings, pgbackrest_repo_host: PgbackrestRepoHost | None
) -> None:
    if not settings.pgbackrest:
        pytest.skip("not applicable if pgbackrest is not activated")
    elif pgbackrest_repo_host:
        pytest.skip("not applicable for pgbackrest repository host")


@pytest.fixture(autouse=True)
def _hook_logger(settings: Settings, logger: logging.Logger) -> Iterator[None]:
    pm = plugin_manager(settings)
    hook_level = logging.DEBUG - 1
    logging.addLevelName(hook_level, "HOOK")
    logger.setLevel(hook_level)

    def before(
        hook_name: str, hook_impls: Sequence[Any], kwargs: Mapping[str, Any]
    ) -> None:
        if not hook_impls:
            return

        def p(value: Any) -> str:
            s = str(value)
            if len(s) >= 20:
                s = f"{s[:17]}..."
            return s

        logger.log(
            hook_level,
            "calling hook %s(%s) with implementations: %s",
            hook_name,
            ", ".join(f"{k}={p(v)}" for k, v in kwargs.items()),
            ", ".join(i.plugin_name for i in hook_impls),
        )

    def after(
        outcome: Any,
        hook_name: str,
        hook_impls: Sequence[Any],
        kwargs: Mapping[str, Any],
    ) -> None:
        if not hook_impls:
            return
        logger.log(hook_level, "outcome of %s: %s", hook_name, outcome.get_result())

    logger.log(hook_level, "installing hookcall monitoring")
    undo = pm.add_hookcall_monitoring(before, after)
    yield None
    logger.log(hook_level, "uninstalling hookcall monitoring")
    undo()


@pytest.fixture(scope="package", autouse=True)
def _installed(
    settings: Settings,
    systemd_requested: bool,
    tmp_path_factory: pytest.TempPathFactory,
    override_systemd_unit_start_limit: Iterator[None],
) -> Iterator[None]:
    tmp_path = tmp_path_factory.mktemp("config")

    if systemd_requested:
        assert settings.service_manager == "systemd"

    custom_settings = tmp_path / "settings.json"
    custom_settings.write_text(settings.json())
    pm = plugin_manager(settings)
    _install.do(
        pm,
        settings,
        env={"SETTINGS": f"@{custom_settings}"},
        header=f"# ** Test run on {platform.node()} at {datetime.now().isoformat()} **",
    )
    yield
    _install.undo(pm, settings, Context(settings=settings))


@pytest.fixture(scope="package")
def override_systemd_unit_start_limit(systemd_requested: bool) -> Iterator[None]:
    """Override the systemd configuration for the instance to prevent
    errors when too many starts happen in a short amount of time
    """
    if not systemd_requested:
        yield
        return
    units = [
        POSTGRESQL_SERVICE_NAME,
        BACKUP_SERVICE_NAME,
        BACKUP_TIMER_NAME,
    ]
    overrides_dir = Path("~/.config/systemd/user").expanduser()
    overrides = [overrides_dir / f"{unit}.d" / "override.conf" for unit in units]
    for override in overrides:
        override.parent.mkdir(parents=True, exist_ok=True)
        content = """
        [Unit]
        StartLimitIntervalSec=0
        """
        override.write_text(dedent(content))

    yield

    for override in overrides:
        shutil.rmtree(override.parent)


@pytest.fixture(scope="package")
def surole_name(request: Any) -> str:
    return str(request.config.option.surole_name)


@pytest.fixture(scope="package")
def surole_password(postgresql_auth: AuthType) -> str | None:
    if postgresql_auth == AuthType.peer:
        return None
    return "s3kret p@Ssw0rd!"


@pytest.fixture(scope="package")
def replrole_password(settings: Settings) -> str:
    return "r3pl p@Ssw0rd!"


@pytest.fixture(scope="package")
def prometheus_password() -> str:
    # TODO: use a password with blanks when
    # https://github.com/prometheus-community/postgres_exporter/issues/393 is fixed
    return "prom3th3us-p@Ssw0rd!"


@pytest.fixture(scope="package")
def temboard_password() -> str:
    return "tembo@rd p@Ssw0rd!"


@pytest.fixture(scope="package")
def powa_password() -> str:
    return "P0w4 p@Ssw0rd!"


@pytest.fixture(scope="package")
def pgbackrest_password(postgresql_auth: AuthType) -> str | None:
    if postgresql_auth == AuthType.peer:
        return None
    return "b4ckup p@Ssw0rd!"


T_co = TypeVar("T_co", covariant=True)


class Factory(Protocol[T_co]):
    def __call__(self, s: Settings, name: str, state: str = ..., **kwargs: Any) -> T_co:
        ...


@pytest.fixture(scope="package")
def instance_manifest_factory(
    pg_version: str,
    surole_password: str | None,
    replrole_password: str,
    pgbackrest_password: str | None,
    prometheus_password: str,
    temboard_password: str,
    powa_password: str,
    tmp_port_factory: Iterator[int],
) -> Factory[interface.Instance]:
    def factory(
        s: Settings, name: str, state: str = "stopped", **kwargs: Any
    ) -> interface.Instance:
        port = next(tmp_port_factory)
        services = {}
        if s.prometheus:
            services["prometheus"] = {
                "port": next(tmp_port_factory),
                "password": prometheus_password,
            }
        if s.powa:
            services["powa"] = {"password": powa_password}
        if s.temboard:
            services["temboard"] = {
                "password": temboard_password,
                "port": next(tmp_port_factory),
            }
        if s.pgbackrest:
            services["pgbackrest"] = {
                "password": pgbackrest_password,
                "stanza": f"mystanza-{name}",
            }
        m = {
            "name": name,
            "version": pg_version,
            "state": state,
            "port": port,
            "auth": {
                "host": "trust",
            },
            "settings": {
                "shared_preload_libraries": "passwordcheck",
            },
            "surole_password": surole_password,
            "replrole_password": replrole_password,
            "restart_on_changes": True,
            **services,
        }
        m = deep_update(m, kwargs)
        pm = plugin_manager(s)
        return interface.Instance.composite(pm).parse_obj(m)

    return factory


@pytest.fixture(scope="package")
def instance_manifest(
    settings: Settings,
    instance_manifest_factory: Factory[interface.Instance],
) -> interface.Instance:
    return instance_manifest_factory(settings, "test", state="started")


@pytest.fixture
def instance_factory(
    instance_manifest_factory: Factory[interface.Instance],
) -> Iterator[Factory[tuple[interface.Instance, system.Instance]]]:
    values: dict[str, tuple[system.Instance, Context]] = {}

    def factory(
        s: Settings, name: str, state: str = "stopped", **kwargs: Any
    ) -> tuple[interface.Instance, system.Instance]:
        assert name not in values, f"{name} already used"
        m = instance_manifest_factory(s, name, state=state, **kwargs)
        ctx = Context(settings=s)
        result = instances.apply(ctx, m)
        assert result.change_state == interface.ApplyChangeState.created
        i = system.Instance.system_lookup((m.name, m.version, s))
        values[name] = i, ctx
        return m, i

    yield factory

    for i, ctx in values.values():
        _drop_instance_if_exists(i, ctx)


@pytest.fixture(scope="package")
def instance(
    settings: Settings,
    instance_manifest: interface.Instance,
    pgbackrest_repo_host: PgbackrestRepoHost | None,
    pgbackrest_password: str | None,
    postgres_logger: PostgresLogger,
) -> Iterator[system.Instance]:
    ctx = Context(settings=settings)
    assert instances.apply(ctx, instance_manifest)
    instance = system.Instance.system_lookup(
        (instance_manifest.name, instance_manifest.version, settings)
    )
    if settings.pgbackrest and pgbackrest_repo_host is not None:
        svc = instance.service(pgbackrest_models.Service)
        pgbackrest_repo_host.add_stanza(svc.stanza, instance)
        pgbackrest.check(instance, svc, settings.pgbackrest, pgbackrest_password)
    # Limit postgresql.conf to uncommented entries to reduce pytest's output
    # due to --show-locals.
    postgresql_conf = instance.datadir / "postgresql.conf"
    postgresql_conf.write_text(
        "\n".join(
            line
            for line in postgresql_conf.read_text().splitlines()
            if line.strip() and not line.strip().startswith("#")
        )
    )
    postgres_logger(instance)
    yield instance
    _drop_instance_if_exists(instance, ctx)


@pytest.fixture(scope="package")
def instance_primary_conninfo(settings: Settings, instance: system.Instance) -> str:
    return psycopg.conninfo.make_conninfo(
        host=settings.postgresql.socket_directory,
        port=instance.port,
        user=settings.postgresql.replrole,
    )


@pytest.fixture(scope="package")
def standby_manifest(
    settings: Settings,
    replrole_password: str,
    instance_primary_conninfo: str,
    instance_manifest: interface.Instance,
    instance_manifest_factory: Factory[interface.Instance],
    pgbackrest_repo_host: PgbackrestRepoHost | None,
) -> interface.Instance:
    extras = {}
    if settings.pgbackrest:
        extras = {"pgbackrest": {"stanza": f"mystanza-{instance_manifest.name}"}}
    return instance_manifest_factory(
        settings,
        "standby",
        state="started",
        surole_password=None,
        standby={
            "primary_conninfo": instance_primary_conninfo,
            "password": replrole_password,
            "slot": "standby",
        },
        **extras,
    )


@pytest.fixture(scope="package")
def standby_instance(
    settings: Settings,
    standby_manifest: interface.Instance,
    instance: system.Instance,
    pgbackrest_repo_host: PgbackrestRepoHost | None,
    pgbackrest_password: str | None,
    postgres_logger: PostgresLogger,
) -> Iterator[system.Instance]:
    assert postgresql.is_running(instance)
    standby = standby_manifest.standby
    assert standby is not None
    execute(
        instance,
        f"SELECT true FROM pg_create_physical_replication_slot({standby.slot!r})",
        fetch=False,
    )
    ctx = Context(settings=settings)
    instances.apply(ctx, standby_manifest)
    stdby_instance = system.Instance.system_lookup(
        (standby_manifest.name, standby_manifest.version, settings)
    )
    if settings.pgbackrest and pgbackrest_repo_host is not None:
        svc = stdby_instance.service(pgbackrest_models.Service)
        primary_svc = instance.service(pgbackrest_models.Service)
        assert svc.stanza == primary_svc.stanza
        assert svc.path == primary_svc.path
        assert svc.index == 2
        with postgresql.running(ctx, stdby_instance):
            pgbackrest_repo_host.add_stanza(svc.stanza, stdby_instance, index=2)
            pgbackrest.check(
                stdby_instance, svc, settings.pgbackrest, pgbackrest_password
            )
    postgres_logger(stdby_instance)
    yield stdby_instance
    _drop_instance_if_exists(stdby_instance, ctx)


@pytest.fixture(scope="package")
def to_be_upgraded_manifest(
    settings: Settings, instance_manifest_factory: Factory[interface.Instance]
) -> interface.Instance:
    return instance_manifest_factory(settings, "to_be_upgraded")


@pytest.fixture(scope="package")
def to_be_upgraded_instance(
    settings: Settings,
    to_be_upgraded_manifest: interface.Instance,
    pgbackrest_repo_host: PgbackrestRepoHost | None,
    pgbackrest_password: str | None,
) -> Iterator[system.Instance]:
    m = to_be_upgraded_manifest
    ctx = Context(settings=settings)
    assert instances.apply(ctx, m)
    instance = system.Instance.system_lookup((m.name, m.version, settings))
    if settings.pgbackrest and pgbackrest_repo_host is not None:
        svc = instance.service(pgbackrest_models.Service)
        with postgresql.running(ctx, instance):
            pgbackrest_repo_host.add_stanza(svc.stanza, instance)
            pgbackrest.check(instance, svc, settings.pgbackrest, pgbackrest_password)
    yield instance
    _drop_instance_if_exists(instance, ctx)


@pytest.fixture(scope="package")
def upgraded_instance(
    settings: Settings,
    to_be_upgraded_instance: system.Instance,
    tmp_port_factory: Iterator[int],
    pgbackrest_repo_host: PgbackrestRepoHost | None,
    pgbackrest_password: str | None,
) -> Iterator[system.Instance]:
    ctx = Context(settings=settings)
    pm = plugin_manager(settings)
    port = next(tmp_port_factory)
    instance = instances.upgrade(
        ctx,
        to_be_upgraded_instance,
        name="upgraded",
        version=to_be_upgraded_instance.version,
        port=port,
        _instance_model=interface.Instance.composite(pm),
    )
    if settings.pgbackrest and pgbackrest_repo_host is not None:
        svc = instance.service(pgbackrest_models.Service)
        assert svc == to_be_upgraded_instance.service(pgbackrest_models.Service)
        with pgbackrest_repo_host.edit_config() as cfg:
            cfg[svc.stanza]["pg1-path"] = str(instance.datadir)
            cfg[svc.stanza]["pg1-port"] = str(port)
        with postgresql.running(ctx, instance):
            pgbackrest_repo_host.run(
                "stanza-upgrade", "--stanza", svc.stanza, "--no-online"
            )
            pgbackrest.check(instance, svc, settings.pgbackrest, pgbackrest_password)
    yield instance
    _drop_instance_if_exists(instance, ctx)


def _drop_instance(instance: system.Instance) -> pgtoolkit.conf.Configuration:
    config = instance.config()
    _drop_instance_if_exists(instance)
    return config


def _drop_instance_if_exists(
    instance: system.Instance, ctx: Context | None = None
) -> None:
    if ctx is None:
        ctx = Context(settings=instance._settings)
    assert ctx.settings == instance._settings
    if instances.exists(instance.name, instance.version, instance._settings):
        # Do a new system_lookup() in order to get the list of services refreshed.
        instance = system.Instance.system_lookup(instance)
        instances.drop(ctx, instance)


@pytest.fixture(scope="package")
def instance_dropped(instance: system.Instance) -> pgtoolkit.conf.Configuration:
    return _drop_instance(instance)


@pytest.fixture(scope="package")
def standby_instance_dropped(
    standby_instance: system.Instance,
) -> pgtoolkit.conf.Configuration:
    return _drop_instance(standby_instance)


@pytest.fixture(scope="package")
def to_be_upgraded_instance_dropped(
    to_be_upgraded_instance: system.Instance,
) -> pgtoolkit.conf.Configuration:
    return _drop_instance(to_be_upgraded_instance)


@pytest.fixture(scope="package")
def upgraded_instance_dropped(
    upgraded_instance: system.Instance,
) -> pgtoolkit.conf.Configuration:
    return _drop_instance(upgraded_instance)


class RoleFactory(Protocol):
    def __call__(self, name: str, options: str = "") -> None:
        ...


@pytest.fixture()
def role_factory(instance: system.Instance) -> Iterator[RoleFactory]:
    rolnames = set()

    def factory(name: str, options: str = "") -> None:
        if name in rolnames:
            raise ValueError(f"{name!r} name already taken")
        execute(instance, f"CREATE ROLE {name} {options}", fetch=False)
        rolnames.add(name)

    yield factory

    for name in rolnames:
        execute(instance, f"DROP ROLE IF EXISTS {name}", fetch=False)


class TablespaceFactory(Protocol):
    def __call__(self, name: str) -> None:
        ...


@pytest.fixture()
def tablespace_factory(
    instance: system.Instance,
    tmp_path_factory: pytest.TempPathFactory,
    logger: logging.Logger,
) -> Iterator[TablespaceFactory]:
    names = set()

    def factory(name: str) -> None:
        location = tmp_path_factory.mktemp(f"tablespace-{name}")
        execute(
            instance,
            f"CREATE TABLESPACE {name} LOCATION '{location}'",  # noqa: B907
            fetch=False,
        )
        names.add((name, location))

    yield factory

    for name, location in names:
        if content := list(location.iterdir()):
            logger.warning(
                "tablespace %s is not empty: %s", name, ", ".join(map(str, content))
            )
        execute(instance, f"DROP TABLESPACE IF EXISTS {name}", fetch=False)


class DatabaseFactory(Protocol):
    def __call__(self, name: str, *, owner: str | None = None) -> None:
        ...


@pytest.fixture()
def database_factory(instance: system.Instance) -> Iterator[DatabaseFactory]:
    datnames = set()

    def factory(name: str, *, owner: str | None = None) -> None:
        if name in datnames:
            raise ValueError(f"{name!r} name already taken")
        sql = f"CREATE DATABASE {name}"
        if owner:
            sql += f" OWNER {owner}"
        execute(instance, sql, fetch=False)
        datnames.add(name)

    yield factory

    for name in datnames:
        execute(instance, f"DROP DATABASE IF EXISTS {name}", fetch=False)
