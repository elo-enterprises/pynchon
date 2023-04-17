""" pynchon.abcs.plugin
"""
from memoized_property import memoized_property

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class PynchonPlugin(object):
    def __init__(self, config=None):
        self.config = config

    def plan(self) -> typing.List:
        raise NotImplementedError()

    def apply(self) -> None:
        raise NotImplementedError()
