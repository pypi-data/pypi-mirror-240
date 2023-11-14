from __future__ import annotations

import functools
from collections.abc import Sequence
from typing import IO, Any

import attrs
import click
import psycopg
from pydantic.utils import deep_update

from .. import databases, postgresql, privileges, task
from ..ctx import Context
from ..models import helpers, interface, system
from .util import (
    Group,
    OutputFormat,
    dry_run_option,
    instance_identifier_option,
    output_format_option,
    pass_ctx,
    pass_instance,
    print_argspec,
    print_json_for,
    print_schema,
    print_table_for,
)


@click.group("database", cls=Group)
@instance_identifier_option
@click.option(
    "--schema",
    is_flag=True,
    callback=functools.partial(print_schema, model=interface.Database),
    expose_value=False,
    is_eager=True,
    help="Print the JSON schema of database model and exit.",
)
@click.option(
    "--ansible-argspec",
    is_flag=True,
    callback=functools.partial(print_argspec, model=interface.Database),
    expose_value=False,
    is_eager=True,
    hidden=True,
    help="Print the Ansible argspec of database model and exit.",
)
def cli(**kwargs: Any) -> None:
    """Manage databases."""


@cli.command("create")
@helpers.parameters_from_model(interface.Database, "create")
@pass_instance
@pass_ctx
def create(
    ctx: Context, instance: system.Instance, database: interface.Database
) -> None:
    """Create a database in a PostgreSQL instance"""
    with ctx.lock, postgresql.running(ctx, instance):
        if databases.exists(ctx, instance, database.name):
            raise click.ClickException("database already exists")
        with task.transaction():
            databases.apply(ctx, instance, database)


@cli.command("alter")
@helpers.parameters_from_model(interface.Database, "update", parse_model=False)
@click.argument("dbname")
@pass_instance
@pass_ctx
def alter(ctx: Context, instance: system.Instance, dbname: str, **changes: Any) -> None:
    """Alter a database in a PostgreSQL instance"""
    with ctx.lock, postgresql.running(ctx, instance):
        values = databases.get(ctx, instance, dbname).dict()
        values = deep_update(values, changes)
        altered = interface.Database.parse_obj(values)
        databases.apply(ctx, instance, altered)


@cli.command("apply", hidden=True)
@click.option("-f", "--file", type=click.File("r"), metavar="MANIFEST", required=True)
@output_format_option
@dry_run_option
@pass_instance
@pass_ctx
def apply(
    ctx: Context,
    instance: system.Instance,
    file: IO[str],
    output_format: OutputFormat,
    dry_run: bool,
) -> None:
    """Apply manifest as a database"""
    database = interface.Database.parse_yaml(file)
    if dry_run:
        ret = interface.ApplyResult(change_state=None)
    else:
        with ctx.lock, postgresql.running(ctx, instance):
            ret = databases.apply(ctx, instance, database)
    if output_format == OutputFormat.json:
        print_json_for(ret)


@cli.command("get")
@output_format_option
@click.argument("name")
@pass_instance
@pass_ctx
def get(
    ctx: Context,
    instance: system.Instance,
    name: str,
    output_format: OutputFormat,
) -> None:
    """Get the description of a database"""
    with postgresql.running(ctx, instance):
        m = databases.get(ctx, instance, name).dict(by_alias=True)
    if output_format == OutputFormat.json:
        print_json_for(m)
    else:
        m.pop("extensions")
        m.pop("schemas")
        print_table_for([m], box=None)


@cli.command("list")
@output_format_option
@click.argument("dbname", nargs=-1)
@pass_instance
@pass_ctx
def ls(
    ctx: Context,
    instance: system.Instance,
    dbname: Sequence[str],
    output_format: OutputFormat,
) -> None:
    """List databases (all or specified ones)

    Only queried databases are shown when DBNAME is specified.
    """

    with postgresql.running(ctx, instance):
        dbs = databases.ls(ctx, instance, dbnames=dbname)
    values = [attrs.asdict(db) for db in dbs]
    if output_format == OutputFormat.json:
        print_json_for(values)
    else:
        print_table_for(values)


@cli.command("drop")
@helpers.parameters_from_model(interface.DatabaseDropped, "create")
@pass_instance
@pass_ctx
def drop(
    ctx: Context, instance: system.Instance, databasedropped: interface.DatabaseDropped
) -> None:
    """Drop a database"""
    with ctx.lock, postgresql.running(ctx, instance):
        databases.drop(ctx, instance, databasedropped)


@cli.command("privileges")
@click.argument("name")
@click.option("-r", "--role", "roles", multiple=True, help="Role to inspect")
@click.option("--default", "defaults", is_flag=True, help="Display default privileges")
@output_format_option
@pass_instance
@pass_ctx
def list_privileges(
    ctx: Context,
    instance: system.Instance,
    name: str,
    roles: Sequence[str],
    defaults: bool,
    output_format: OutputFormat,
) -> None:
    """List privileges on a database."""
    with postgresql.running(ctx, instance):
        databases.get(ctx, instance, name)  # check existence
        try:
            prvlgs = privileges.get(
                ctx, instance, databases=(name,), roles=roles, defaults=defaults
            )
        except ValueError as e:
            raise click.ClickException(str(e)) from None
    values = [attrs.asdict(p) for p in prvlgs]
    if output_format == OutputFormat.json:
        print_json_for(values)
    else:
        print_table_for(values)


@cli.command("run")
@click.argument("sql_command")
@click.option(
    "-d", "--database", "dbnames", multiple=True, help="Database to run command on"
)
@click.option(
    "-x",
    "--exclude-database",
    "exclude_dbnames",
    multiple=True,
    help="Database to not run command on",
)
@output_format_option
@pass_instance
@pass_ctx
def run(
    ctx: Context,
    instance: system.Instance,
    sql_command: str,
    dbnames: Sequence[str],
    exclude_dbnames: Sequence[str],
    output_format: OutputFormat,
) -> None:
    """Run given command on databases of a PostgreSQL instance"""
    with postgresql.running(ctx, instance):
        try:
            result = databases.run(
                ctx,
                instance,
                sql_command,
                dbnames=dbnames,
                exclude_dbnames=exclude_dbnames,
            )
        except psycopg.ProgrammingError as e:
            raise click.ClickException(str(e)) from None
    if output_format == OutputFormat.json:
        print_json_for(result)
    else:
        for dbname, rows in result.items():
            print_table_for(rows, title=f"Database {dbname}")


@cli.command("dump")
@click.argument("dbname")
@pass_instance
@pass_ctx
def dump(ctx: Context, instance: system.Instance, dbname: str) -> None:
    """Dump a database"""
    with postgresql.running(ctx, instance):
        databases.dump(ctx, instance, dbname)
