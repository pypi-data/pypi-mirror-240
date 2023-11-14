from __future__ import annotations

import io
import socket
import typing
from dataclasses import dataclass

import port_for
import pydantic
import pytest
import yaml

from pglift import types
from pglift.types import Address, Manifest, PortValidator, StrEnum, field_annotation


@dataclass(frozen=True)
class MyAnnotation:
    x: str


class M(pydantic.BaseModel):
    x: int
    y: typing.Annotated[str, MyAnnotation("a"), ("a", "b")]


def test_field_annotation() -> None:
    assert field_annotation(M.__fields__["x"], MyAnnotation) is None
    assert field_annotation(M.__fields__["y"], dict) is None
    assert field_annotation(M.__fields__["y"], MyAnnotation) == MyAnnotation("a")
    assert field_annotation(M.__fields__["y"], tuple) == ("a", "b")


def test_portvalidator_available() -> None:
    p = port_for.select_random()
    assert PortValidator.available(p)
    with socket.socket() as s:
        s.bind(("", p))
        s.listen()
        assert not PortValidator.available(p)


class Point(Manifest):
    x: float
    y: float


def test_parse_yaml() -> None:
    stream = io.StringIO()
    yaml.dump({"x": 1.2, "y": 3.4}, stream)
    stream.seek(0)
    point = Point.parse_yaml(stream)
    assert point == Point(x=1.2, y=3.4)


def test_yaml() -> None:
    point = Point(x=0, y=1.2)
    s = point.yaml()
    assert s == "---\nx: 0.0\ny: 1.2\n"


def test_copy_validate() -> None:
    class S(Manifest):
        f: str
        g: str = pydantic.Field(default="unset", exclude=True)

    s = S(f="f", g="g")
    assert s._copy_validate({"g": "G"}).g == "G"


def test_strenum() -> None:
    class Pets(StrEnum):
        cat = "cat"

    assert str(Pets.cat) == "cat"


def test_address() -> None:
    class Cfg(pydantic.BaseModel):
        addr: Address

    cfg = Cfg(addr="server:123")
    assert cfg.addr == "server:123"
    assert types.address_host(cfg.addr) == "server"
    assert types.address_port(cfg.addr) == 123

    a = Address("server:123")
    assert types.address_host(a) == "server"
    assert types.address_port(a) == 123

    # no validation
    assert str(Address("server")) == "server"

    with pytest.raises(
        pydantic.errors.StrRegexError, match="string does not match regex"
    ):
        Address.validate("server")
    with pytest.raises(pydantic.ValidationError, match="string does not match regex"):
        Cfg(addr="server")
    with pytest.raises(pydantic.ValidationError, match="string does not match regex"):
        Cfg(addr="server:ab")
