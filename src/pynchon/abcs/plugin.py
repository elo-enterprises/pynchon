""" pynchon.abcs.plugin
"""
from memoized_property import memoized_property

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)

from .meta import Meta


class Plugin(object, metaclass=Meta):
    priority = 0

    def __init__(self, final=None) -> typing.NoneType:
        """ """
        self.final = final
        # self.config = config
        # self.state = None

    @memoized_property
    def logger(self):
        return lme.get_logger(f"<{self.__class__.__name__} Plugin>")
