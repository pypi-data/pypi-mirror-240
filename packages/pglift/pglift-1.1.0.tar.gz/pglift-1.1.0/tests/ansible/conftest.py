from __future__ import annotations

import os
import pathlib
import secrets
import string
import subprocess
from collections.abc import Iterator
from typing import Callable

import pytest
import yaml


@pytest.fixture(scope="package", autouse=True)
def skip_ansible_test() -> None:
    try:
        from pglift.settings import SiteSettings
    except ImportError:
        return

    if SiteSettings.site_settings():
        pytest.skip("custom site settings are incompatible with ansible tests")


def generate_secret(length: int) -> str:
    return "".join(
        secrets.choice(string.ascii_letters + string.digits) for i in range(length)
    )


@pytest.fixture(autouse=True)
def syslog() -> Iterator[None]:
    """Print syslog messages emitted during each test case."""
    try:
        msgs = open("/var/log/messages")
    except OSError:
        yield
        return
    msgs.read()
    yield
    print(msgs.read().rstrip())
    msgs.close()


@pytest.fixture(scope="session")
def playdir() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent.parent / "docs" / "ansible"


@pytest.fixture
def ansible_env(tmp_path: pathlib.Path) -> dict[str, str]:
    vault_passfile = tmp_path / "vault-pass"
    with vault_passfile.open("w") as f:
        f.write(generate_secret(32))
    return os.environ | {
        "ANSIBLE_VERBOSITY": "3",
        "ANSIBLE_VAULT_PASSWORD_FILE": str(vault_passfile),
    }


@pytest.fixture
def ansible_vault(
    tmp_path: pathlib.Path, ansible_env: dict[str, str]
) -> Callable[[dict[str, str]], pathlib.Path]:
    def mk_vault(secrets: dict[str, str]) -> pathlib.Path:
        vault = tmp_path / "vars"
        with vault.open("w") as f:
            yaml.dump(secrets, f)
        subprocess.check_call(["ansible-vault", "encrypt", str(vault)], env=ansible_env)
        return vault

    return mk_vault
