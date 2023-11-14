from __future__ import annotations

import pytest

from pglift import databases, postgresql, privileges
from pglift.ctx import Context
from pglift.models import system
from pglift.models.system import DefaultPrivilege, Privilege

from . import execute
from .conftest import DatabaseFactory, RoleFactory


@pytest.fixture(scope="module", autouse=True)
def _postgresql_running(instance: system.Instance) -> None:
    if not postgresql.is_running(instance):
        pytest.fail("instance is not running")


@pytest.fixture(autouse=True)
def roles_and_privileges(
    ctx: Context,
    instance: system.Instance,
    role_factory: RoleFactory,
    database_factory: DatabaseFactory,
) -> None:
    role_factory("rol1")
    role_factory("rol2")
    database_factory("db1")
    database_factory("db2")
    execute(
        instance,
        "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO rol1",
        fetch=False,
        dbname="db1",
    )
    execute(
        instance,
        "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO rol2",
        fetch=False,
        dbname="db2",
    )


def test_get_default(ctx: Context, instance: system.Instance) -> None:
    expected = [
        DefaultPrivilege(
            database="db1",
            schema="public",
            role="rol1",
            object_type="TABLE",
            privileges=[
                "DELETE",
                "REFERENCES",
                "INSERT",
                "SELECT",
                "TRUNCATE",
                "TRIGGER",
                "UPDATE",
            ],
        ),
        DefaultPrivilege(
            database="db2",
            schema="public",
            role="rol2",
            object_type="FUNCTION",
            privileges=["EXECUTE"],
        ),
    ]
    prvlgs = privileges.get(ctx, instance, defaults=True)
    assert prvlgs == expected
    assert (
        privileges.get(ctx, instance, databases=["db1"], roles=["rol2"], defaults=True)
        == []
    )
    assert (
        privileges.get(ctx, instance, databases=["db2"], roles=["rol2"], defaults=True)
        == expected[-1:]
    )


def test_get_general(ctx: Context, instance: system.Instance, surole_name: str) -> None:
    databases.run(
        ctx,
        instance,
        "CREATE TABLE table1 (x int, y varchar)",
        dbnames=["db1", "db2"],
    )
    databases.run(
        ctx,
        instance,
        "GRANT UPDATE ON table1 TO rol2; GRANT SELECT (x) ON table1 TO rol2",
        dbnames=["db2"],
    )
    expected = [
        Privilege(
            database="db1",
            schema="public",
            object_type="TABLE",
            role=surole_name,
            privileges=[
                "INSERT",
                "UPDATE",
                "SELECT",
                "DELETE",
                "TRUNCATE",
                "TRIGGER",
                "REFERENCES",
            ],
            object_name="table1",
            column_privileges={},
        ),
        Privilege(
            database="db1",
            schema="public",
            object_type="TABLE",
            role="rol1",
            privileges=[
                "SELECT",
                "DELETE",
                "UPDATE",
                "TRUNCATE",
                "REFERENCES",
                "TRIGGER",
                "INSERT",
            ],
            object_name="table1",
            column_privileges={},
        ),
        Privilege(
            database="db2",
            schema="public",
            object_type="TABLE",
            role=surole_name,
            privileges=[
                "INSERT",
                "SELECT",
                "UPDATE",
                "DELETE",
                "TRUNCATE",
                "REFERENCES",
                "TRIGGER",
            ],
            object_name="table1",
            column_privileges={},
        ),
        Privilege(
            database="db2",
            schema="public",
            object_type="TABLE",
            role="rol2",
            privileges=["UPDATE"],
            object_name="table1",
            column_privileges={"x": ["SELECT"]},
        ),
    ]
    prvlgs = [
        p for p in privileges.get(ctx, instance, defaults=False) if p.database != "powa"
    ]

    def sort_key(p: DefaultPrivilege) -> str:
        return p.database + p.role

    assert sorted(prvlgs, key=sort_key) == sorted(expected, key=sort_key)
    assert (
        privileges.get(ctx, instance, databases=["db1"], defaults=False)
        == sorted(expected, key=sort_key)[:-2]
    )
    assert (
        privileges.get(ctx, instance, databases=["db2"], defaults=False)
        == sorted(expected, key=sort_key)[-2:]
    )
