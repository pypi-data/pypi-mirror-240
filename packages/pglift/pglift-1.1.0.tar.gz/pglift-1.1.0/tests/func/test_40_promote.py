from __future__ import annotations

from collections.abc import Iterator

import psycopg
import pytest

from pglift import instances, postgresql
from pglift.ctx import Context
from pglift.models import interface, system

from . import AuthType, execute

pytestmark = pytest.mark.standby


@pytest.fixture(scope="module")
def promoted_instance(
    instance: system.Instance, standby_instance: system.Instance
) -> Iterator[system.Instance]:
    assert postgresql.is_running(standby_instance)
    with instances.stopped(Context(settings=instance._settings), instance):
        ctx = Context(settings=standby_instance._settings)
        instances.promote(ctx, standby_instance)
        yield standby_instance


def test_promoted(
    promoted_instance: system.Instance, instance_manifest: interface.Instance
) -> None:
    assert not promoted_instance.standby
    settings = promoted_instance._settings
    replrole = instance_manifest.replrole(settings)
    assert execute(
        promoted_instance,
        "SELECT * FROM pg_is_in_recovery()",
        role=replrole,
        dbname="template1",
    ) == [{"pg_is_in_recovery": False}]


def test_connect(
    promoted_instance: system.Instance,
    postgresql_auth: AuthType,
    surole_password: str | None,
) -> None:
    """Check that we can connect to the promoted instance."""
    settings = promoted_instance._settings
    connargs = {
        "host": str(promoted_instance.config().unix_socket_directories),
        "port": promoted_instance.port,
        "user": settings.postgresql.surole.name,
        "dbname": "postgres",
    }
    if postgresql_auth != AuthType.peer:
        connargs["password"] = surole_password
    with psycopg.connect(**connargs) as conn:  # type: ignore[call-overload]
        if postgresql_auth == AuthType.peer:
            assert not conn.pgconn.used_password
        else:
            assert conn.pgconn.used_password
