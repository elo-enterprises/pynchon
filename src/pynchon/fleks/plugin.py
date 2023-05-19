""" pynchon.fleks.plugin
"""
from memoized_property import memoized_property

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)

from .meta import Meta


class Plugin(metaclass=Meta):
    """ """

    priority = 0

    def __init__(self, final=None) -> typing.NoneType:
        """
        """
        self.final = final

    @classmethod
    def classmethod_dispatch(kls, *args):
        """
        :param kls:
        :param *args:
        """
        from multipledispatch import dispatch

        def dec(fxn):
            return classmethod(dispatch(type(kls), *args)(fxn))

        return dec

    @memoized_property
    def logger(self):
        return lme.get_logger(f"<{self.__class__.__name__} Plugin>")
