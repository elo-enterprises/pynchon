""" pynchon.abcs.attrdict
"""

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class AttrDictBase:
    """
    A dictionary with attribute-style access.
    It maps attribute access to the real dictionary.
    """

    def __init__(self, **init: typing.OptionalAny):
        dict.__init__(self, init)

    def __getstate__(self) -> typing.Iterable:
        return self.__dict__.items()

    def __setstate__(self, items: typing.Any) -> None:
        for key, val in items:
            self.__dict__[key] = val

    def __repr__(self) -> str:
        return "%s(%s)" % (self.__class__.__name__, dict.__repr__(self))

    def __setitem__(self, key: str, value: typing.Any) -> typing.Any:
        return super(AttrDictBase, self).__setitem__(key, value)

    def __getitem__(self, name: str) -> typing.Any:
        try:
            return super(AttrDictBase, self).__getitem__(name)
        except (KeyError,) as exc:
            LOGGER.debug(f"AttrDict: KeyError accessing {name}")
            raise

    def __delitem__(self, name: str) -> typing.Any:
        return super(AttrDictBase, self).__delitem__(name)

    __getattr__ = __getitem__
    __setattr__ = __setitem__


class AttrDict(AttrDictBase, dict):
    pass
