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

    @staticmethod
    def init_cli(kls):
        from pynchon.bin import common, entry
        def plugin_main():
            pass
        plugin_main.__doc__=f"""subcommands for `{kls.name}` plugin"""
        plugin_main = common.groop(
            kls.name, parent=entry.entry)(plugin_main)
        @common.kommand(name='config', parent=plugin_main)
        def config():
            """shows current config for this plugin"""
            LOGGER.debug(kls.config_kls)

    @memoized_property
    def logger(self):
        return lme.get_logger(f"<{self.__class__.__name__} Plugin>")

    def plan(self, config) -> typing.List:
        self.state = config
        return []

    def apply(self, config) -> None:
        self.state = config
        return []
