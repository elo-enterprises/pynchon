""" pynchon.models
"""
from memoized_property import memoized_property
from pynchon.util import typing,lme
from pynchon.abcs.plugin import Plugin as BasePlugin
LOGGER = lme.get_logger(__name__)

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

    @typing.classproperty
    def click_entry(kls):
        from pynchon.bin import entry
        return entry.entry

    @staticmethod
    def init_cli(kls):
        from pynchon.bin import common
        def plugin_main():
            pass
        plugin_main.__doc__ = f"""subcommands for `{kls.name}` plugin"""
        plugin_main = common.groop(
            kls.name,
            parent=kls.click_entry)(plugin_main)

        @common.kommand(name='config', parent=plugin_main)
        def config():
            """shows current config for this plugin"""
            LOGGER.debug(kls.config_kls)

        return plugin_main


Plugin = PynchonPlugin
