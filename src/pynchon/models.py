"""
"""
from memoized_property import memoized_property

from pynchon.abcs.plugin import Plugin as BasePlugin

class PynchonPlugin(BasePlugin):
    priority = 10

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
