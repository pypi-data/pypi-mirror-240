from __future__ import annotations

import pytest

from pglift import databases, exceptions
from pglift.ctx import Context
from pglift.models.interface import Database, DatabaseDropped
from pglift.models.system import Instance


def test_standby_database_apply(ctx: Context, standby_instance: Instance) -> None:
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby instance$",
    ):
        databases.apply(ctx, standby_instance, Database(name="test"))


def test_standby_database_drop(ctx: Context, standby_instance: Instance) -> None:
    with pytest.raises(
        exceptions.InstanceReadOnlyError,
        match=f"^{standby_instance.version}/standby is a read-only standby instance$",
    ):
        databases.drop(ctx, standby_instance, DatabaseDropped(name="test"))
