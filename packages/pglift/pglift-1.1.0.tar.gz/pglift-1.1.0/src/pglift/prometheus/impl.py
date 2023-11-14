from __future__ import annotations

import logging
import shlex
import urllib.parse
from pathlib import Path
from urllib.parse import quote

import psycopg
import psycopg.conninfo
import pydantic
from pgtoolkit.conf import Configuration

from .. import exceptions
from .. import service as service_mod
from ..ctx import Context
from ..models import interface, system
from ..settings import Settings, _prometheus
from ..task import task
from .models import (
    PostgresExporter,
    Service,
    ServiceManifest,
    State,
    default_port,
    service_name,
)

logger = logging.getLogger(__name__)


def available(settings: Settings) -> _prometheus.Settings | None:
    return settings.prometheus


def get_settings(settings: Settings) -> _prometheus.Settings:
    """Return settings for prometheus

    Same as `available` but assert that settings are not None.
    Should be used in a context where settings for the plugin are surely
    set (for example in hookimpl).
    """
    assert settings.prometheus is not None
    return settings.prometheus


def enabled(qualname: str, settings: _prometheus.Settings) -> bool:
    return _configpath(qualname, settings).exists()


def _args(execpath: Path, configpath: Path) -> list[str]:
    varname = "POSTGRES_EXPORTER_OPTS"
    line = config_var(configpath, varname)
    try:
        key, value = line.split("=", 1)
    except ValueError as e:
        raise exceptions.ConfigurationError(
            configpath, f"malformatted {varname} parameter"
        ) from e
    return [str(execpath)] + shlex.split(value[1:-1])


def _configpath(qualname: str, settings: _prometheus.Settings) -> Path:
    return Path(str(settings.configpath).format(name=qualname))


def _env(configpath: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for line in configpath.read_text().splitlines():
        key, value = line.split("=", 1)
        if key != "POSTGRES_EXPORTER_OPTS":
            env[key] = value
    return env


def _queriespath(qualname: str, settings: _prometheus.Settings) -> Path | None:
    if settings.queriespath:
        return Path(str(settings.queriespath).format(name=qualname))
    return None


def _pidfile(qualname: str, settings: _prometheus.Settings) -> Path:
    return Path(str(settings.pid_file).format(name=qualname))


def config_var(configpath: Path, varname: str) -> str:
    """Return postgres_exporter configuration file line for given varname.

    :param configpath: the path to the configuration file.
    :param varname: the name of the variable to search for.

    :raises ~exceptions.ConfigurationError: if varname could not be read from
        configuration file.
    :raises ~exceptions.FileNotFoundError: if configuration file is not found.
    """
    if not configpath.exists():
        raise exceptions.FileNotFoundError(
            f"postgres_exporter configuration file {configpath} not found"
        )
    with configpath.open() as f:
        for line in f:
            if line.startswith(varname):
                break
        else:
            raise exceptions.ConfigurationError(configpath, f"{varname} not found")
    return line


def port(name: str, settings: _prometheus.Settings) -> int:
    """Return postgres_exporter port read from configuration file.

    :param name: the name for the service.

    :raises ~exceptions.ConfigurationError: if port could not be read from
        configuration file.
    :raises ~exceptions.FileNotFoundError: if configuration file is not found.
    """
    configpath = _configpath(name, settings)
    varname = "PG_EXPORTER_WEB_LISTEN_ADDRESS"
    line = config_var(configpath, varname)
    try:
        value = line.split("=", 1)[1].split(":", 1)[1]
    except (IndexError, ValueError) as e:
        raise exceptions.ConfigurationError(
            configpath, f"malformatted {varname} parameter"
        ) from e
    return int(value.strip())


def password(name: str, settings: _prometheus.Settings) -> str | None:
    """Return postgres_exporter dsn password read from configuration file.

    :param name: the name for the service.

    :raises ~exceptions.ConfigurationError: if password could not be read from
        configuration file.
    :raises ~exceptions.FileNotFoundError: if configuration file is not found.
    """
    configpath = _configpath(name, settings)
    varname = "DATA_SOURCE_NAME"
    line = config_var(configpath, varname)
    try:
        conninfo = psycopg.conninfo.conninfo_to_dict(line.split("=", 1)[1])
        value: str | None = conninfo.get("password")
    except (IndexError, ValueError, psycopg.ProgrammingError) as e:
        raise exceptions.ConfigurationError(
            configpath, f"malformatted {varname} parameter"
        ) from e
    return value


def make_uri(
    *,
    user: str = "",
    password: str = "",
    port: str = "5432",
    dbname: str = "",
    **kw: str,
) -> str:
    """Return a libpq compatible uri for the given dsn object

    Note: key=value form DSN doesn't work with a unix socket host.
    Also for socket hosts, the host must be given in the uri params
    (after '?').

    >>> make_uri(**{'host': '/socket/path', 'dbname': 'somedb'})
    'postgresql://:5432/somedb?host=%2Fsocket%2Fpath'
    >>> make_uri(**{'host': '/socket/path'})
    'postgresql://:5432?host=%2Fsocket%2Fpath'
    >>> make_uri(**{'host': '/socket/path', 'user': 'someone', 'dbname': 'somedb', 'connect_timeout': '10', 'password': 'secret'})
    'postgresql://someone:secret@:5432/somedb?host=%2Fsocket%2Fpath&connect_timeout=10'
    >>> make_uri(**{'host': '/socket/path', 'user': 'someone', 'dbname': 'somedb', 'password': 'secret@!'})
    'postgresql://someone:secret%40%21@:5432/somedb?host=%2Fsocket%2Fpath'
    """
    userspec = user
    userspec += f":{quote(password)}" if password else ""
    userspec += "@" if userspec else ""
    netloc = f"{userspec}:{port}"
    query = urllib.parse.urlencode(kw)
    return urllib.parse.urlunsplit(("postgresql", netloc, dbname, query, None))


def system_lookup(name: str, settings: _prometheus.Settings) -> Service | None:
    try:
        port_ = port(name, settings)
        passwd_ = password(name, settings)
    except (exceptions.FileNotFoundError, exceptions.ConfigurationError) as exc:
        logger.debug("failed to read postgres_exporter configuration %s: %s", name, exc)
        return None
    else:
        password_ = None
        if passwd_ is not None:
            password_ = pydantic.SecretStr(passwd_)
        return Service(name=name, settings=settings, port=port_, password=password_)


@task
def setup(
    ctx: Context,
    name: str,
    settings: _prometheus.Settings,
    *,
    dsn: str = "",
    password: str | None = None,
    port: int = default_port,
) -> Service:
    """Set up a Prometheus postgres_exporter service for an instance.

    :param name: a (locally unique) name for the service.
    :param dsn: connection info string to target instance.
    :param password: connection password.
    :param port: TCP port for the web interface and telemetry of postgres_exporter.
    """
    uri = make_uri(**psycopg.conninfo.conninfo_to_dict(dsn, password=password))
    config = [f"DATA_SOURCE_NAME={uri}"]
    log_options = ["--log.level=info"]
    opts = " ".join(log_options)
    config.extend(
        [
            f"PG_EXPORTER_WEB_LISTEN_ADDRESS=:{port}",
            f"POSTGRES_EXPORTER_OPTS={opts!r}",
        ]
    )
    if queriespath := _queriespath(name, settings):
        config.append(f"PG_EXPORTER_EXTEND_QUERY_PATH={queriespath}")

    configpath = _configpath(name, settings)
    needs_restart = False
    if service := system_lookup(name, settings):
        assert configpath.exists()
        if configpath.read_text().splitlines() != config:
            logger.info("reconfiguring Prometheus postgresql %s", name)
            configpath.write_text("\n".join(config))
            needs_restart = True
    else:
        logger.info("configuring Prometheus postgresql %s", name)
        configpath.parent.mkdir(mode=0o750, exist_ok=True, parents=True)
        configpath.touch(mode=0o600)
        configpath.write_text("\n".join(config))
        if queriespath and not queriespath.exists():
            queriespath.parent.mkdir(mode=0o750, exist_ok=True, parents=True)
            queriespath.touch()
        service = system_lookup(name, settings)
        assert service is not None

    ctx.hook.enable_service(ctx=ctx, service=service_name, name=name)

    if needs_restart:
        restart(ctx, service)
    return service


@setup.revert(title="deconfiguring Prometheus postgres_exporter {name}")
def revert_setup(
    ctx: Context,
    name: str,
    settings: _prometheus.Settings,
    *,
    dsn: str = "",
    password: str | None = None,
    port: int = default_port,
) -> None:
    ctx.hook.disable_service(ctx=ctx, service=service_name, name=name, now=True)
    _configpath(name, settings).unlink(missing_ok=True)
    if queriespath := _queriespath(name, settings):
        queriespath.unlink(missing_ok=True)


def start(ctx: Context, service: Service, *, foreground: bool = False) -> None:
    logger.info("starting Prometheus postgres_exporter %s", service.name)
    service_mod.start(ctx, service, foreground=foreground)


def stop(ctx: Context, service: Service) -> None:
    logger.info("stopping Prometheus postgres_exporter %s", service.name)
    service_mod.stop(ctx, service)


def restart(ctx: Context, service: Service) -> None:
    logger.info("restarting Prometheus postgres_exporter %s", service.name)
    service_mod.restart(ctx, service)


def apply(
    ctx: Context,
    postgres_exporter: PostgresExporter,
    settings: _prometheus.Settings,
) -> interface.ApplyResult:
    """Apply state described by specified interface model as a postgres_exporter
    service for a non-local instance.

    :raises exceptions.InstanceStateError: if the target instance exists on system.
    """
    try:
        system.PostgreSQLInstance.from_qualname(postgres_exporter.name, ctx.settings)
    except (ValueError, exceptions.InstanceNotFound):
        pass
    else:
        raise exceptions.InstanceStateError(
            f"instance {postgres_exporter.name!r} exists locally"
        )

    exists = enabled(postgres_exporter.name, settings)
    if postgres_exporter.state == State.absent:
        drop(ctx, postgres_exporter.name)
        return interface.ApplyResult(
            change_state=interface.ApplyChangeState.dropped if exists else None
        )
    else:
        password = None
        if postgres_exporter.password:
            password = postgres_exporter.password.get_secret_value()
        service = setup(
            ctx,
            postgres_exporter.name,
            settings,
            dsn=postgres_exporter.dsn,
            password=password,
            port=postgres_exporter.port,
        )
        if postgres_exporter.state == State.started:
            start(ctx, service)
        elif postgres_exporter.state == State.stopped:
            stop(ctx, service)
        return interface.ApplyResult(
            change_state=interface.ApplyChangeState.created
            if not exists
            else interface.ApplyChangeState.changed
        )


def drop(ctx: Context, name: str) -> None:
    """Remove a postgres_exporter service."""
    logger.info("dropping postgres_exporter service '%s'", name)
    settings = get_settings(ctx.settings)
    if (service := system_lookup(name, settings)) is None:
        logger.warning("no postgres_exporter service '%s' found", name)
        return
    stop(ctx, service)
    revert_setup(ctx, name, settings)


def setup_local(
    ctx: Context,
    manifest: interface.Instance,
    settings: _prometheus.Settings,
    instance_config: Configuration,
) -> None:
    """Setup Prometheus postgres_exporter for a local instance."""
    service_manifest = manifest.service_manifest(ServiceManifest)
    rolename = settings.role
    dsn = ["dbname=postgres"]
    if "port" in instance_config:
        dsn.append(f"port={instance_config.port}")
    if host := instance_config.get("unix_socket_directories"):
        dsn.append(f"host={host}")
    dsn.append(f"user={rolename}")
    if not instance_config.get("ssl", False):
        dsn.append("sslmode=disable")

    instance = system.PostgreSQLInstance.system_lookup(
        (manifest.name, manifest.version, ctx.settings)
    )
    configpath = _configpath(instance.qualname, settings)
    password_: str | None = None
    if service_manifest.password:
        password_ = service_manifest.password.get_secret_value()
    elif configpath.exists():
        # Get the password from config file
        password_ = password(instance.qualname, settings)

    setup(
        ctx,
        instance.qualname,
        settings,
        dsn=" ".join(dsn),
        password=password_,
        port=service_manifest.port,
    )
