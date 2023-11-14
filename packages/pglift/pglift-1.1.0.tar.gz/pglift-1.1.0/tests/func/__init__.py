from __future__ import annotations

import enum
import pathlib
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Literal, overload
from unittest.mock import patch

import httpx
import psycopg
import pytest
from tenacity import retry
from tenacity.retry import retry_if_exception_type
from tenacity.stop import stop_after_attempt
from tenacity.wait import wait_fixed
from typing_extensions import TypeAlias

from pglift import db, instances, postgresql
from pglift.ctx import Context
from pglift.models import interface, system
from pglift.types import AutoStrEnum, Role, Status

PostgresLogger: TypeAlias = Callable[[system.PostgreSQLInstance], None]


class AuthType(AutoStrEnum):
    peer = enum.auto()
    password_command = enum.auto()
    pgpass = enum.auto()


@contextmanager
def running_instance(ctx: Context, instance: system.Instance) -> Iterator[None]:
    """Context manager to temporarily start an instance and run hooks."""
    if postgresql.status(instance) == Status.running:
        yield
        return

    instances.start(ctx, instance)
    try:
        yield
    finally:
        instances.stop(ctx, instance)


@contextmanager
def postgresql_stopped(
    ctx: Context, instance: system.PostgreSQLInstance
) -> Iterator[None]:
    """Context manager to temporarily stop a PostgreSQL instance."""
    if not postgresql.is_running(instance):
        yield
        return

    postgresql.stop_postgresql(ctx, instance, mode="fast", wait=True)
    try:
        yield
    finally:
        postgresql.start_postgresql(ctx, instance, foreground=False, wait=True)


def connect(
    instance: system.Instance, role: Role | None = None, **connargs: Any
) -> psycopg.Connection[psycopg.rows.DictRow]:
    assert "user" not in connargs
    if role is not None:
        connargs["user"] = role.name
        if role.password:
            assert "password" not in connargs
            connargs["password"] = role.password.get_secret_value()
    else:
        settings = instance._settings.postgresql
        connargs["user"] = settings.surole.name
        if "password" not in connargs:
            connargs["password"] = postgresql.ctl.libpq_environ(
                instance, connargs["user"]
            ).get("PGPASSWORD")
    conninfo = db.dsn(instance, **connargs)
    return psycopg.connect(conninfo, autocommit=True, row_factory=psycopg.rows.dict_row)


@overload
def execute(
    instance: system.Instance,
    *queries: str,
    fetch: Literal[True],
    role: Role | None = None,
    **connargs: Any,
) -> list[Any]:
    ...


@overload
def execute(
    instance: system.Instance,
    *queries: str,
    fetch: bool = False,
    role: Role | None = None,
    **connargs: Any,
) -> list[Any]:
    ...


def execute(
    instance: system.Instance,
    *queries: str,
    fetch: bool = True,
    role: Role | None = None,
    **connargs: Any,
) -> list[Any] | None:
    assert postgresql.is_running(instance), f"instance {instance} is not running"
    if fetch and len(queries) > 1:
        raise ValueError("cannot use fetch=True with multiple queries")
    with connect(instance, role, **connargs) as conn:
        cur = conn.execute("; ".join(queries))
        if fetch:
            return cur.fetchall()
    return None


def check_connect(
    ctx: Context,
    postgresql_auth: AuthType,
    surole_name: str,
    instance_manifest: interface.Instance,
    instance: system.Instance,
) -> None:
    assert postgresql.is_running(instance), f"instance {instance} is not running"
    surole = instance_manifest.surole(ctx.settings)
    port = instance.port
    connargs = {
        "host": str(instance.config().unix_socket_directories),
        "port": port,
        "user": surole.name,
    }
    if postgresql_auth == AuthType.peer:
        pass
    elif postgresql_auth == AuthType.pgpass:
        connargs["passfile"] = str(ctx.settings.postgresql.auth.passfile)
    else:
        with pytest.raises(
            psycopg.OperationalError, match="no password supplied"
        ) as exc_info:
            with patch.dict("os.environ", clear=True):
                psycopg.connect(**connargs).close()  # type: ignore[call-overload]
        assert exc_info.value.pgconn
        assert exc_info.value.pgconn.needs_password
        assert surole.password is not None
        connargs["password"] = surole.password.get_secret_value()
    if surole_name != "postgres":
        connargs["dbname"] = "postgres"
    with psycopg.connect(**connargs) as conn:  # type: ignore[call-overload]
        if postgresql_auth == AuthType.peer:
            assert not conn.pgconn.used_password
        else:
            assert conn.pgconn.used_password


def role_in_pgpass(
    passfile: pathlib.Path,
    role: Role,
    *,
    port: int | str | None = None,
) -> bool:
    if not passfile.exists():
        return False
    password = ""
    if role.password:
        password = role.password.get_secret_value()
    parts = [role.name, password]
    if port is not None:
        parts = [str(port), "*"] + parts
    pattern = ":".join(parts)
    with passfile.open() as f:
        for line in f:
            if pattern in line:
                return True
    return False


@retry(
    reraise=True,
    wait=wait_fixed(2),
    stop=stop_after_attempt(5),
    retry=retry_if_exception_type(httpx.RequestError),
)
def http_get(*args: Any, **kwargs: Any) -> httpx.Response:
    return httpx.get(*args, **kwargs)


def passfile_entries(passfile: Path, *, role: str = "postgres") -> list[str]:
    return [line for line in passfile.read_text().splitlines() if f":{role}:" in line]


def config_dict(configpath: Path) -> dict[str, str]:
    config = {}
    for line in configpath.read_text().splitlines():
        key, value = line.split("=", 1)
        config[key] = value.strip()
    return config
