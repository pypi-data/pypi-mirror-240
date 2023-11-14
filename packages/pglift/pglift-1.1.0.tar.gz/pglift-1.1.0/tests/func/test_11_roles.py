from __future__ import annotations

import datetime
import functools
from unittest.mock import patch

import psycopg
import pytest
from pydantic import SecretStr

from pglift import databases, exceptions, postgresql, roles, types
from pglift.ctx import Context
from pglift.models import interface, system
from pglift.settings._postgresql import PostgreSQLVersion

from . import AuthType, connect, execute, role_in_pgpass
from .conftest import DatabaseFactory, RoleFactory


@pytest.fixture(scope="module", autouse=True)
def _postgresql_running(instance: system.Instance) -> None:
    if not postgresql.is_running(instance):
        pytest.fail("instance is not running")


def test_exists(
    ctx: Context, instance: system.Instance, role_factory: RoleFactory
) -> None:
    assert not roles.exists(ctx, instance, "absent")
    role_factory("present")
    assert roles.exists(ctx, instance, "present")


def test_apply(
    ctx: Context, postgresql_auth: AuthType, instance: system.Instance
) -> None:
    rolname = "applyme"
    passfile = ctx.settings.postgresql.auth.passfile

    def _role_in_pgpass(role: types.Role, *, port: int | str | None = None) -> bool:
        if postgresql_auth != AuthType.pgpass:
            return False
        assert passfile is not None
        return role_in_pgpass(passfile, role, port=port)

    role = interface.Role(name=rolname)
    assert not roles.exists(ctx, instance, role.name)
    r = roles.apply(ctx, instance, role)
    assert r.change_state == interface.ApplyChangeState.created
    assert roles.exists(ctx, instance, role.name)
    assert not role.has_password
    assert passfile is None or not _role_in_pgpass(role)
    assert roles.apply(ctx, instance, role).change_state is None  # no-op

    role = interface.Role(name=rolname, state="absent")
    assert roles.exists(ctx, instance, role.name)
    r = roles.apply(ctx, instance, role)
    assert r.change_state == interface.ApplyChangeState.dropped
    assert not roles.exists(ctx, instance, role.name)

    validity = datetime.datetime(2050, 1, 2, tzinfo=datetime.timezone.utc)
    role = interface.Role(
        name=rolname,
        password="passw0rd",
        connection_limit=3,
        validity=validity,
    )
    r = roles.apply(ctx, instance, role)
    assert r.change_state == interface.ApplyChangeState.created
    assert role.has_password
    (row,) = execute(
        instance,
        f"select rolpassword from pg_authid where rolname = {role.name!r}",
    )
    if instance.version >= PostgreSQLVersion.v14:
        assert row["rolpassword"].startswith("SCRAM-SHA-256$4096:")
    else:
        assert row["rolpassword"].startswith("md5")
    assert passfile is None or not _role_in_pgpass(role)
    with pytest.raises(psycopg.OperationalError, match="is not permitted to log in"):
        execute(instance, "select 1", dbname="template1", role=role)
    (record,) = execute(
        instance,
        f"select rolvaliduntil, rolconnlimit from pg_roles where rolname = {role.name!r}",
    )
    assert record["rolvaliduntil"] == validity
    assert record["rolconnlimit"] == 3

    role = interface.Role(
        name=rolname,
        login=True,
        password="passw0rd",
        pgpass=True,
        in_roles=["pg_monitor"],
    )
    r = roles.apply(ctx, instance, role)
    assert r.change_state == interface.ApplyChangeState.changed
    assert role.has_password
    assert passfile is None or _role_in_pgpass(role)
    with connect(instance, role, dbname="template1"):
        pass
    rows = execute(
        instance,
        """
        SELECT
            r.rolname AS role,
            ARRAY_AGG(m.rolname) AS member_of
        FROM
            pg_auth_members
            JOIN pg_authid m ON pg_auth_members.roleid = m.oid
            JOIN pg_authid r ON pg_auth_members.member = r.oid
        GROUP BY
            r.rolname
        """,
    )
    assert {"role": rolname, "member_of": ["pg_monitor"]} in rows

    pwchanged_role = role._copy_validate({"password": "changed"})
    r = roles.apply(ctx, instance, pwchanged_role)
    if passfile is not None:
        assert r.change_state == interface.ApplyChangeState.changed
    else:
        # Password changes in the database are not detected.
        assert r.change_state is None

    nopw_role = role._copy_validate({"password": None})
    r = roles.apply(ctx, instance, nopw_role)
    assert r.change_state is None

    role = interface.Role(
        name=rolname,
        login=True,
        password="passw0rd_changed",
        pgpass=True,
        connection_limit=5,
    )
    r = roles.apply(ctx, instance, role)
    assert r.change_state == interface.ApplyChangeState.changed
    assert role.has_password
    assert passfile is None or _role_in_pgpass(role)
    assert roles.get(ctx, instance, rolname).connection_limit == 5
    with connect(instance, role, dbname="template1"):
        pass

    role = interface.Role(name=rolname, pgpass=False, login=False)
    r = roles.apply(ctx, instance, role)
    assert r.change_state == interface.ApplyChangeState.changed
    with pytest.raises(psycopg.OperationalError, match="is not permitted to log in"):
        execute(
            instance,
            "select 1",
            dbname="template1",
            role=role,
            password="passw0rd_changed",
        )
    assert not role.has_password
    assert passfile is None or not _role_in_pgpass(role)
    assert roles.get(ctx, instance, rolname).connection_limit is None


def test_encrypted_password(ctx: Context, instance: system.Instance) -> None:
    # Already encrypted password should be stored "as is"
    already_encrypted_password = (
        # This is encrypted "scret"
        "SCRAM-SHA-256$4096:kilIxOG9m0wvjkJtBVw+dg==$o2jKTC2nw+"
        "POUAVt5YARHuekubQ+LUeVH1cdCS4bKnw=:6y1eBzBUXITZPEiCb1H"
        "k6AscBq/gmgB5AnFz/57zI/g="
    )
    already_encrypted = interface.Role(
        name="already_encrypted",
        encrypted_password=already_encrypted_password,
        login=True,
    )
    assert (
        roles.apply(ctx, instance, already_encrypted).change_state
        == interface.ApplyChangeState.created
    )
    rows = execute(
        instance,
        "select rolpassword from pg_authid where rolname = 'already_encrypted'",
    )
    assert rows == [{"rolpassword": already_encrypted_password}]

    # We cannot login with an already encrypted password
    with pytest.raises(
        psycopg.OperationalError, match="password authentication failed"
    ):
        execute(
            instance,
            "select 1",
            dbname="template1",
            role=interface.Role(
                name="already_encrypted", password=already_encrypted_password
            ),
        )
    assert execute(
        instance,
        "select 1 as v",
        dbname="template1",
        role=interface.Role(name="already_encrypted", password="scret"),
    ) == [{"v": 1}]


def test_alter_surole_password(
    ctx: Context,
    instance_manifest: interface.Instance,
    instance: system.Instance,
    postgresql_auth: AuthType,
    surole_name: str,
    caplog: pytest.LogCaptureFixture,
) -> None:
    if postgresql_auth == AuthType.peer:
        pytest.skip(f"not applicable for auth:{postgresql_auth}")

    check_connect = functools.partial(connect, instance)
    surole = roles.get(ctx, instance, surole_name)
    surole = surole._copy_validate(
        update={
            "password": instance_manifest.surole(ctx.settings).password,
            "state": "present",
        }
    )
    role = surole._copy_validate(
        update={"password": SecretStr("passw0rd_changed"), "state": "present"}
    )
    caplog.clear()
    r = roles.apply(ctx, instance, role)
    if postgresql_auth == AuthType.pgpass:
        assert r.change_state == interface.ApplyChangeState.changed
    else:
        assert r.change_state is None
    try:
        with check_connect(password="passw0rd_changed"):
            pass
    finally:
        with patch.dict("os.environ", {"PGPASSWORD": "passw0rd_changed"}):
            r = roles.apply(ctx, instance, surole)
        if postgresql_auth == AuthType.pgpass:
            assert r.change_state == interface.ApplyChangeState.changed
        else:
            assert r.change_state is None
        with pytest.raises(
            psycopg.OperationalError, match="password authentication failed"
        ):
            with check_connect(password="passw0rd_changed"):
                pass
        with connect(instance):
            pass


def test_get(
    ctx: Context,
    instance_manifest: interface.Instance,
    instance: system.Instance,
    role_factory: RoleFactory,
    surole_name: str,
) -> None:
    with pytest.raises(exceptions.RoleNotFound, match="absent"):
        roles.get(ctx, instance, "absent")

    role = roles.get(ctx, instance, surole_name)
    assert role is not None
    surole = instance_manifest.surole(ctx.settings)
    assert role.name == surole_name
    if surole.password:
        assert role.has_password
        if ctx.settings.postgresql.surole.pgpass:
            assert role.dict(include={"pgpass"}) == {"pgpass": True}
        assert roles.get(ctx, instance, surole_name, password=False).password is None
    assert role.login
    assert role.superuser
    assert role.replication

    role_factory(
        "r1",
        "LOGIN NOINHERIT CREATEROLE VALID UNTIL '2051-07-29T00:00+00:00' IN ROLE pg_monitor CONNECTION LIMIT 10",
    )
    r1 = roles.get(ctx, instance, "r1")
    assert r1.password is None
    assert not r1.inherit
    assert r1.login
    assert not r1.superuser
    assert not r1.replication
    assert not r1.createdb
    assert r1.createrole
    assert r1.connection_limit == 10
    assert r1.in_roles == ["pg_monitor"]
    assert r1.validity == datetime.datetime(2051, 7, 29, tzinfo=datetime.timezone.utc)


def test_ls(
    ctx: Context,
    instance_manifest: interface.Instance,
    instance: system.Instance,
    role_factory: RoleFactory,
) -> None:
    roles.apply(
        ctx,
        instance,
        interface.Role.parse_obj({"name": "r1", "password": "secret"}),
    )
    role_factory(
        "r2",
        "LOGIN NOINHERIT CREATEDB VALID UNTIL '2051-07-29T00:00+00:00' IN ROLE pg_monitor CONNECTION LIMIT 10",
    )
    rls = roles.ls(ctx, instance)
    roles.drop(ctx, instance, interface.RoleDropped(name="r1"))
    assert {"r1", "r2"} & {r.name for r in rls}
    r1 = next(r for r in rls if r.name == "r1").dict(include={"has_password"})
    r2 = next(r for r in rls if r.name == "r2").dict(exclude={"pgpass"})
    assert r1 == {"has_password": True}
    assert r2 == {
        "connection_limit": 10,
        "has_password": False,
        "in_roles": ["pg_monitor"],
        "inherit": False,
        "login": True,
        "name": "r2",
        "replication": False,
        "superuser": False,
        "createdb": True,
        "createrole": False,
        "validity": datetime.datetime(2051, 7, 29, 0, 0, tzinfo=datetime.timezone.utc),
    }


def test_drop(
    ctx: Context, instance: system.Instance, role_factory: RoleFactory
) -> None:
    with pytest.raises(exceptions.RoleNotFound, match="dropping_absent"):
        roles.drop(ctx, instance, interface.Role(name="dropping_absent"))
    role_factory("dropme")
    roles.drop(ctx, instance, interface.Role(name="dropme"))
    assert not roles.exists(ctx, instance, "dropme")


def test_drop_reassign_owned(
    ctx: Context, instance: system.Instance, database_factory: DatabaseFactory
) -> None:
    role1 = interface.Role(name="owner1", password="password", login=True)
    assert (
        roles.apply(ctx, instance, role1).change_state
        == interface.ApplyChangeState.created
    )
    assert roles.exists(ctx, instance, role1.name)

    role2 = interface.Role(name="owner2", password="password", login=True)
    assert (
        roles.apply(ctx, instance, role2).change_state
        == interface.ApplyChangeState.created
    )
    assert roles.exists(ctx, instance, role2.name)

    schema = "myschema"
    execute(instance, f"CREATE SCHEMA {schema}", fetch=False, dbname="postgres")
    execute(
        instance,
        f"GRANT ALL ON SCHEMA {schema} TO PUBLIC",
        fetch=False,
        dbname="postgres",
    )

    tablename = "myapp"
    execute(
        instance,
        f"CREATE TABLE {schema}.{tablename} (id INT)",
        fetch=False,
        dbname="postgres",
        role=role1,
    )
    r = execute(
        instance,
        f"SELECT tableowner FROM pg_catalog.pg_tables WHERE tablename = {tablename!r}",
        dbname="postgres",
        role=role1,
    )
    assert {"tableowner": role1.name} in r
    with pytest.raises(
        exceptions.DependencyError,
        match=r'role "owner1" cannot be dropped .* \(detail: owner of table myschema.myapp\)',
    ):
        roles.drop(ctx, instance, role1)

    role1 = role1._copy_validate(
        update={"reassign_owned": role2.name, "state": "absent"}
    )
    roles.apply(ctx, instance, role1)
    assert not roles.exists(ctx, instance, role1.name)
    r = execute(
        instance,
        f"SELECT tableowner FROM pg_catalog.pg_tables WHERE tablename = {tablename!r}",
    )
    assert {"tableowner": role2.name} in r

    database_factory("db_owned", owner=role2.name)

    role2 = role2._copy_validate(update={"drop_owned": True, "state": "absent"})
    roles.apply(ctx, instance, role2)
    assert not roles.exists(ctx, instance, role2.name)
    r = execute(
        instance,
        f"SELECT EXISTS (SELECT FROM pg_tables WHERE tablename = {tablename!r})",
    )
    assert {"exists": False} in r
    assert not databases.exists(ctx, instance, "db_owned")
