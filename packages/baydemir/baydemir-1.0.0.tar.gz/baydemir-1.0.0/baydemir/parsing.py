"""
Type-directed parsing of JSON-like and YAML-like objects.
"""
# FIXME: Unnecessarily verbose exception traces.

import dataclasses
import enum
import pathlib
import typing
from typing import Any, Literal, Type, TypeVar, Union, cast

import yaml

__all__ = [
    "ParseError",
    #
    "parse",
    "unparse",
    "reparse",
    #
    "load_yaml",
]

T = TypeVar("T")


class ParseError(Exception):
    """
    An object cannot be parsed according to some specification.
    """


def parse(data: Any, spec: Type[T]) -> T:
    """
    Coerces `data` into an object that is compatible with the type `spec`.

    The coercion process is aware of:

      - `dict`, `list`
      - `Any`, `Literal`, `Union` (including `Optional`)
      - data classes
      - enumerations (`data` is passed as-is to the constructor)
    """

    try:
        return cast(T, _parse(data, spec))
    except ParseError as exn:
        raise ParseError(f"Failed to parse {data!r} as {spec!r}") from exn


def _parse(data: Any, spec: Any) -> Any:
    # pylint: disable=too-many-branches,too-many-return-statements
    """
    Implements the core logic of `parse`.

    This implementation allows us to:

      1. Annotate `parse` with a meaningful type. Mypy cannot handle the
         code flow here. The clearest and simplest solution is to `cast` the
         final result and leave everything else dynamically typed.

      2. Percolate errors in a way that provides meaningful context. The
         value that fails to parse might be buried deep in the original data
         structure.
    """

    origin = typing.get_origin(spec)
    args = typing.get_args(spec)

    if origin is dict:
        if isinstance(data, dict):
            new_data = {}

            for (k, v) in data.items():
                new_k = parse(k, args[0])
                new_v = parse(v, args[1])

                new_data[new_k] = new_v

            return new_data

        raise ParseError("Not a dictionary")

    if origin is list:
        if isinstance(data, list):
            return [parse(x, args[0]) for x in data]
        raise ParseError("Not a list")

    if spec is Any:
        return data

    if origin is Literal:
        if data in args:
            return data
        raise ParseError("Not a valid literal")

    if origin is Union:
        for new_spec in args:
            try:
                return parse(data, new_spec)
            except ParseError:
                pass
        raise ParseError("Exhausted the Union's branches")

    if dataclasses.is_dataclass(spec):
        if isinstance(data, dict):
            new_data = {}

            for field in dataclasses.fields(spec):
                if field.name in data:
                    new_data[field.name] = parse(data[field.name], field.type)

            try:
                return spec(**new_data)
            except (TypeError, ValueError) as exn:
                raise ParseError("Failed to construct data class instance") from exn

        raise ParseError("Not a dictionary")

    if isinstance(spec, type) and issubclass(spec, enum.Enum):
        try:
            return spec(data)
        except (TypeError, ValueError) as exn:
            raise ParseError("Failed to construct enumeration member") from exn

    if isinstance(spec, type) and isinstance(data, spec):
        return data

    raise ParseError("Unrecognized object and type")


def unparse(data: Any) -> Any:
    """
    Coerces `data` into a JSON-like or YAML-like object.

    Informally, this function acts as the inverse of `parse`. The order of
    fields in data classes will be preserved if the implementation of `dict`
    preserves the insertion order of keys.
    """

    if isinstance(data, enum.Enum):
        return data.value

    if dataclasses.is_dataclass(data):
        new_data = {}

        for field in dataclasses.fields(data):
            k = field.name
            v = getattr(data, field.name)

            if v is not field.default or field.default is not None:
                new_data[unparse(k)] = unparse(v)

        return new_data

    if isinstance(data, list):
        return [unparse(x) for x in data]

    if isinstance(data, dict):
        return {unparse(k): unparse(v) for (k, v) in sorted(data.items())}

    return data


def reparse(data: Any, spec: Type[T]) -> T:
    """
    Coerces `data` into an object that is compatible with the type `spec`.
    """

    return parse(unparse(data), spec)


def load_yaml(path: pathlib.Path, spec: Type[T]) -> T:
    """
    Loads a single, "safe" YAML object with the given `spec` from a file.
    """

    with open(path, encoding="utf-8") as fp:
        obj = yaml.safe_load(fp)
    return parse(obj, spec)
