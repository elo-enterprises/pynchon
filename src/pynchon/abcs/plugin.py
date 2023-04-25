""" pynchon.abcs.plugin
"""
from memoized_property import memoized_property

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Plugin(object):
    priority = 0

    def __init__(self, config=None):
        self.config = config
        self.state = None

    @memoized_property
    def logger(self):
        return lme.get_logger(f"<{self.__class__.__name__} Plugin>")

    def plan(self, config=None) -> typing.List:
        self.state = config
        return []

    def apply(self, config=None) -> None:
        plan = self.plan(config=config)
        from pynchon.util.os import invoke
        return [invoke(p).succeeded for p in plan]
