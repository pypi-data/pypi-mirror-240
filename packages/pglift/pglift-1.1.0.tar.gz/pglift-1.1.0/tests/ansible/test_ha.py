from __future__ import annotations

import json
import os
import pathlib
import socket
import subprocess
from collections.abc import Iterator
from typing import Callable

import psycopg
import pytest
import yaml
from psycopg.rows import dict_row

from ..etcd import Etcd


@pytest.fixture(scope="package")
def patroni_execpath(patroni_execpath: pathlib.Path | None) -> pathlib.Path:
    if patroni_execpath:
        return patroni_execpath
    pytest.skip("Patroni is not available")


@pytest.fixture(scope="module", autouse=True)
def _etcd_running(etcd_host: Etcd) -> Iterator[None]:
    with etcd_host.running():
        yield None


@pytest.fixture
def site_settings(
    tmp_path: pathlib.Path,
    patroni_execpath: pathlib.Path,
    etcd_host: Etcd,
    ca_cert: pathlib.Path,
) -> Iterator[pathlib.Path]:
    settings = {
        "prefix": str(tmp_path),
        "run_prefix": str(tmp_path / "run"),
        "patroni": {
            "execpath": str(patroni_execpath),
            "loop_wait": 1,
            "etcd": {
                "hosts": [etcd_host.endpoint],
                "protocol": "https",
                "cacert": str(ca_cert),
            },
        },
        "postgresql": {
            "replrole": "replication",
        },
    }

    settings_f = tmp_path / "config.json"
    with settings_f.open("w") as f:
        json.dump(settings, f)

    env = os.environ.copy()
    env["SETTINGS"] = f"@{settings_f}"
    subprocess.run(
        ["pglift", "--debug", "site-configure", "install"],
        capture_output=True,
        check=True,
        env=env,
    )
    yield settings_f
    subprocess.run(
        ["pglift", "--non-interactive", "--debug", "site-configure", "uninstall"],
        capture_output=True,
        check=True,
        env=env,
    )


@pytest.fixture
def call_playbook(
    tmp_path: pathlib.Path,
    ansible_env: dict[str, str],
    playdir: pathlib.Path,
    site_settings: pathlib.Path,
    tmp_port_factory: Iterator[int],
) -> Iterator[Callable[[str], None]]:
    env = ansible_env.copy()

    env["SETTINGS"] = f"@{site_settings}"

    src = pathlib.Path(__file__).parent / "data"
    env["PGLIFT_CONFIG_PATH"] = str(src)

    vars = tmp_path / "vars"
    host = socket.gethostbyname(socket.gethostname())
    with vars.open("w") as f:
        yaml.safe_dump(
            {
                "primary_rest_api": f"{host}:{next(tmp_port_factory)}",
                "replica_rest_api": f"{host}:{next(tmp_port_factory)}",
            },
            f,
        )

    def call(playname: str) -> None:
        subprocess.check_call(
            [
                "ansible-playbook",
                "--extra-vars",
                f"@{vars}",
                playdir / playname,
            ],
            env=env,
        )

    yield call

    call("ha-delete.yml")


def test(call_playbook: Callable[[str], None]) -> None:
    call_playbook("ha-setup.yml")

    # test connection to the primary instance
    primary_dsn = "host=/tmp user=postgres dbname=postgres port=5432"
    with psycopg.connect(primary_dsn, row_factory=dict_row) as cnx:
        row = cnx.execute("SHOW work_mem").fetchone()
    assert row is not None

    # test connection to the replica instance
    replica_dsn = "host=/tmp user=postgres dbname=postgres port=5433"
    with psycopg.connect(replica_dsn, row_factory=dict_row) as cnx:
        row = cnx.execute("SHOW work_mem").fetchone()
    assert row is not None
