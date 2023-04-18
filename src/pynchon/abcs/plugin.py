""" pynchon.abcs.plugin
"""
from memoized_property import memoized_property

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class BasePlugin(object):
    priority = 0
    def __init__(self, config=None):
        self.config = config
        self.state = None

    @memoized_property
    def logger(self):
        return lme.get_logger(f"<{self.__class__.__name__} Plugin>")

    def plan(self, config) -> typing.List:
        self.state = config
        return []

    def apply(self, config) -> None:
        self.state = config
        return []


class PynchonPlugin(BasePlugin):
    priority=10
    @memoized_property
    def render_instructions(self):
        result = self.state.pynchon.get("render", [])
        # self.logger.debug(f"parsed render-instructions: {result}")
        return result

    @memoized_property
    def gen_instructions(self):
        result = self.state.pynchon.get("generate", [])
        # self.logger.info(f"parsed generate-instructions: {result}")
        return result


Plugin = PynchonPlugin
