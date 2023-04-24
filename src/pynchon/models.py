""" pynchon.models
"""
import json
import functools
from memoized_property import memoized_property

from pynchon.util import typing, lme
from pynchon.abcs.plugin import Plugin as BasePlugin
from pynchon.bin import common

LOGGER = lme.get_logger(__name__)


class PynchonPlugin(BasePlugin):
    priority = 10

    # @memoized_property
    # def render_instructions(self):
    #     result = self.state.pynchon.get("render", [])
    #     # self.logger.debug(f"parsed render-instructions: {result}")
    #     return result
    #
    # @memoized_property
    # def gen_instructions(self):
    #     result = self.state.pynchon.get("generate", [])
    #     # self.logger.info(f"parsed generate-instructions: {result}")
    #     return result

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod
        result = getattr(config_mod, kls.config_kls.config_key)
        return result

    @typing.classproperty
    def click_entry(kls):
        from pynchon.bin import entry

        return entry.entry

    @staticmethod
    def init_cli(kls):
        from pynchon import config
        config.finalize()

        def plugin_main():
            pass

        plugin_main.__doc__ = f"""subcommands for `{kls.name}` plugin"""
        plugin_main = common.groop(
            getattr(kls,'cli_name', kls.name),
            parent=kls.click_entry)(plugin_main)

        @common.kommand(name='config', parent=plugin_main)
        def config():
            """shows current config for this plugin"""
            LOGGER.debug(f"config class: {kls.config_kls}")
            LOGGER.debug(f"current config:")
            result = kls.get_current_config()
            print(json.dumps(result,indent=2))
        from pynchon.plugins import get_plugin_obj
        obj = get_plugin_obj(kls.name)
        FORBIDDEN = 'get_current_config defaults logger init_cli plan apply'.split()
        for method_name in dir(obj):
            if method_name.startswith('_') or method_name in FORBIDDEN:
                continue
            fxn = getattr(obj, method_name)
            if fxn is None or type(fxn).__name__!='method':
                continue
            # LOGGER.critical(f"wrapping {[method_name, type(fxn)]} for CLI..")
            def wrapper(*args, fxn=fxn,**kwargs):
                LOGGER.debug(f"calling {fxn} from wrapper")
                result = fxn(*args, **kwargs)
                print(json.dumps(result, indent=2))
                return result
            # wrapper = lambda *args, **kargs: print(json.dumps(fxn(*args,**kargs) or {}, indent=2))
            # wrapper.__name__=fxn.__name__
            # wrapper.__doc__=fxn.__doc__
            tmp = common.kommand(
                fxn.__name__,
                parent=plugin_main,
            )(wrapper)


        return plugin_main


Plugin = PynchonPlugin
