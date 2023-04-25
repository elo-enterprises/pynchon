""" pynchon.models
"""
import json

from memoized_property import memoized_property

from pynchon.bin import common
from pynchon.util import typing, lme, text
from pynchon.abcs.plugin import Plugin as BasePlugin

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
    @property
    def plugin_config(self):
        return self.get_current_config()


    @typing.classproperty
    def project_config(self):
        from pynchon.api import project

        return project.get_config()

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod

        result = getattr(config_mod,
            getattr(kls.config_kls,'config_key', kls.name))
        return result

    @typing.classproperty
    def click_entry(kls):
        from pynchon.bin import entry

        return entry.entry

    @staticmethod
    def init_cli_group(kls):
        def plugin_main():
            pass
        plugin_main.__doc__ = f"""subcommands for `{kls.name}` plugin"""
        plugin_main = common.groop(
            getattr(kls, 'cli_name', kls.name), parent=kls.click_entry
        )(plugin_main)
        return plugin_main

    @typing.classproperty
    def instance(kls):
        from pynchon.plugins import get_plugin_obj
        return get_plugin_obj(kls.name)

    @typing.classproperty
    def instance_methods(kls):
        FORBIDDEN = [
            'get_current_config',
            'defaults',
            'logger',
            'init_cli',
            'instance',
            'instance_methods',
            # 'plan', 'apply'
        ]
        result = []
        obj = kls.instance
        for method_name in dir(kls):
            if method_name.startswith('_') or method_name in FORBIDDEN:
                continue
            # print(method_name)
            # import IPython; IPython.embed()
            fxn = getattr(obj, method_name)
            if fxn is None or type(fxn).__name__ != 'method':
                continue
            result.append(method_name)
        return result

    @staticmethod
    def init_cli(kls):
        from pynchon import config
        config.finalize()

        plugin_main = kls.init_cli_group(kls)

        if not callable(getattr(kls.instance,'config')):

            @common.kommand(name='config', parent=plugin_main)
            def config():
                """shows current config for this plugin"""
                LOGGER.debug(f"config class: {kls.config_kls}")
                LOGGER.debug(f"current config:")
                result = kls.get_current_config()
                print(text.to_json(result))

        obj = kls.instance
        for method_name in kls.instance_methods:
            # LOGGER.critical(f"wrapping {[method_name, type(fxn)]} for CLI..")
            fxn = getattr(obj, method_name)
            import functools
            # @functools.wraps(fxn)
            def wrapper(*args, fxn=fxn, **kwargs):
                LOGGER.debug(f"calling {fxn} from wrapper")
                result = fxn(*args, **kwargs)
                print(text.to_json(result))
                return result

            # wrapper = lambda *args, **kargs: print(json.dumps(fxn(*args,**kargs) or {}, indent=2))
            # wrapper.__name__=fxn.__name__
            wrapper.__doc__=fxn.__doc__
            tmp = common.kommand(
                fxn.__name__.replace('_', '-'),
                # help=fxn.__doc__,
                parent=plugin_main,
            )(wrapper)

        return plugin_main

Plugin = PynchonPlugin
