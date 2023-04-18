""" pynchon.util.types

This module collects common imports and annotation-types, i.e.
various optional/composite types used in type-hints, underneath
one convenient namespace.
"""

import typing
from typing import *  # noqa

# from typing_extensions import Annotated

Bool = bool
StringMaybe = typing.Optional[str]
CallableMaybe = typing.Optional[typing.Callable]
DictMaybe = typing.Optional[typing.Dict]
OptionalAny = typing.Optional[typing.Any]

Namespace = typing.Dict[str, typing.Any]
CallableNamespace = typing.Dict[str, typing.Callable]


# i.e. `obj,created = model.objects.get_or_create()`
GetOrCreateResult = typing.Tuple[object, bool]


def is_subclass(x, y, strict=True):
    """ """
    if isinstance(x, (typing.Type)) and issubclass(x, y):
        if strict and x == y:
            return False
        return True
    return False


class classproperty(object):
    """ """

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner) -> OptionalAny:
        return self.f(owner)
