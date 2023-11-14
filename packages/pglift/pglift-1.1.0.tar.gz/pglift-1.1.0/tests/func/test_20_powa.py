from __future__ import annotations

import pytest

from pglift.models import system
from pglift.models.interface import Role

from . import execute


@pytest.fixture(scope="module", autouse=True)
def _powa_available(powa_available: bool) -> None:
    if not powa_available:
        pytest.skip("powa is not available")


def test_powa(
    instance: system.Instance,
    powa_password: str,
) -> None:
    config = instance.config()
    assert (
        config.shared_preload_libraries
        == "passwordcheck, pg_qualstats, pg_stat_statements, pg_stat_kcache"
    )

    powa_settings = instance._settings.powa
    assert powa_settings is not None
    dbname = powa_settings.dbname

    def get_installed_extensions() -> list[str]:
        return [
            r["extname"]
            for r in execute(
                instance,
                "SELECT extname FROM pg_extension",
                dbname=dbname,
            )
        ]

    installed = get_installed_extensions()
    assert "pg_stat_statements" in installed
    assert "btree_gist" in installed
    assert "powa" in installed

    (record,) = execute(
        instance,
        "SELECT datname from powa_databases_src(0) LIMIT 1",
        fetch=True,
        role=Role(name=powa_settings.role, password=powa_password),
        dbname=dbname,
    )
    assert record["datname"] is not None
