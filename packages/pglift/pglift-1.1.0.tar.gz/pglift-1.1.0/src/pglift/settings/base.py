import string
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from pathlib import Path, PosixPath
from typing import Any, Final, Union

import pydantic
from pydantic.fields import ModelField

from .. import types
from .._compat import Self


def string_format_variables(fmt: str) -> set[str]:
    return {v for _, v, _, _ in string.Formatter().parse(fmt) if v is not None}


class BaseModel(pydantic.BaseModel):
    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
        smart_union = True


class TemplatedPath(PosixPath):
    @classmethod
    def __get_validators__(cls) -> Iterator[Callable[..., Self]]:
        yield cls.validate

    @classmethod
    def validate(cls, value: Path, field: ModelField) -> Self:
        if not isinstance(value, cls):
            value = cls(value)
        # Ensure all template variables used in default field value are also
        # used in user value and that no unhandled variables are used.
        expected = string_format_variables(str(field.default))
        if expected != string_format_variables(str(value)):
            raise ValueError(
                "value contains unknown or missing template variable(s); "
                f"expecting: {', '.join(sorted(expected)) or 'none'}"
            )
        return value


@dataclass(frozen=True)
class PrefixedPath:
    basedir: Path = Path("")
    key: str = "prefix"

    def prefix(self, value: Path, prefix: Union[str, Path]) -> Path:
        """Return the path prefixed if is not yet absolute.

        >>> PrefixedPath(basedir=Path("alice")).prefix(Path("documents"), "/home")
        PosixPath('/home/alice/documents')
        >>> PrefixedPath(basedir=Path("/uh")).prefix(Path("/root"), Path("/whatever"))
        PosixPath('/root')
        """
        if value.is_absolute():
            return value
        assert Path(prefix).is_absolute(), (
            f"expecting an absolute prefix (got {prefix!r})",
        )
        return prefix / self.basedir / value


ConfigPath: Final = PrefixedPath(Path("etc"))
DataPath: Final = PrefixedPath(Path("srv"))
LogPath: Final = PrefixedPath(Path("log"))
RunPath: Final = PrefixedPath(Path(""), key="run_prefix")


def prefix_values(
    values: dict[str, Any],
    prefixes: dict[str, Path],
    model_type: type[pydantic.BaseModel],
) -> dict[str, Any]:
    for key, value in values.items():
        field = model_type.__fields__[key]
        if isinstance(value, Path):
            if p := types.field_annotation(field, PrefixedPath):
                values[key] = p.prefix(value, prefixes[p.key])
        elif isinstance(value, pydantic.BaseModel):
            child_values = {k: getattr(value, k) for k in value.__fields__}
            child_values = prefix_values(child_values, prefixes, value.__class__)
            # Use .construct() to avoid re-validating child.
            values[key] = value.construct(
                _fields_set=value.__fields_set__, **child_values
            )
    return values


class ServerCert(BaseModel):
    """TLS certificate files for a server."""

    ca_cert: pydantic.FilePath = pydantic.Field(
        description="Certificate Authority certificate to verify client requests."
    )
    cert: pydantic.FilePath = pydantic.Field(
        description="Certificate file for TLS encryption."
    )
    key: pydantic.FilePath = pydantic.Field(
        description="Private key for the certificate."
    )
