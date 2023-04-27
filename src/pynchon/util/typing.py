""" pynchon.util.types

This module collects common imports and annotation-types, i.e.
various optional/composite types used in type-hints, underneath
one convenient namespace.
"""

import typing

from types import MappingProxyType  # noqa
from types import FunctionType  # noqa
from types import MethodType  # noqa
from typing import *  # noqa

# from typing_extensions import Annotated

Bool = bool
NoneType = type(None)
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

    def __init__(self, fxn):
        self.fxn = fxn

    def __get__(self, obj, owner) -> OptionalAny:
        return self.fxn(owner)


CLASSPROP_CACHES = {}


class classproperty_cached(classproperty):
    def __get__(self, obj, owner) -> OptionalAny:
        result = CLASSPROP_CACHES.get(self.fxn, self.fxn(owner))
        CLASSPROP_CACHES[self.fxn] = result
        return CLASSPROP_CACHES[self.fxn]


import importlib


def lazy_import(
    importer_name,
):
    """Return the importing module and a callable for lazy importing.

    The module named by importer_name represents the module performing the
    import to help facilitate resolving relative imports.

    to_import is an iterable of the modules to be potentially imported (absolute
    or relative). The `as` form of importing is also supported,
    e.g. `pkg.mod as spam`.

    This function returns a tuple of two items. The first is the importer
    module for easy reference within itself. The second item is a callable to be
    set to `__getattr__`.
    """

    class fakemod:
        """ """

        def __init__(self, name):
            self.name = name

        def __getattr__(self, name):
            module = importlib.import_module(self.name)
            return getattr(module, name)

    return fakemod(importer_name)
