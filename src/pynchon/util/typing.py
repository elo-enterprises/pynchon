""" {{pkg}}.util.types

This module collects common imports and annotation-types, i.e.
various optional/composite types used in type-hints, underneath
one convenient namespace.
"""

import typing
from typing import *  # noqa

from types import MappingProxyType  # noqa
from types import FunctionType  # noqa
from types import MethodType  # noqa
# from typing_extensions import Annotated

from pathlib import Path as BasePath

try:
    import pydantic
    validate = pydantic.validate_arguments  # noqa
except (ImportError,):
    validate = lambda fxn: fxn
validate_arguments=validate


Bool = bool
NoneType = type(None)
StringMaybe = typing.Optional[str]
CallableMaybe = typing.Optional[typing.Callable]
DictMaybe = typing.Optional[typing.Dict]
OptionalAny = typing.Optional[typing.Any]
PathType = type(BasePath())

Namespace = typing.Dict[str, typing.Any]
CallableNamespace = typing.Dict[str, typing.Callable]

# i.e. `obj,created = model.objects.get_or_create()`
GetOrCreateResult = typing.Tuple[object, bool]

# isort: off
from .importing import * # noqa
from .oop import * # noqa
# isort: on
