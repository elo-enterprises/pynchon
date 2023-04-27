""" pynchon.models
"""
# from memoized_property import memoized_property

from pynchon.bin import common
from pynchon.util import typing, lme, text
from pynchon.abcs.plugin import Plugin as AbstractPlugin

LOGGER = lme.get_logger(__name__)


class PynchonPlugin(AbstractPlugin):
    cli_label = 'abstract'

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

        result = getattr(config_mod, getattr(kls.config_kls, 'config_key', kls.name))
        return result

    @typing.classproperty
    def instance(kls):
        from pynchon.plugins import get_plugin_obj

        return get_plugin_obj(kls.name)

    def config(self):
        """shows current config for this plugin"""
        kls = self.__class__
        LOGGER.debug(f"config class: {kls.config_kls}")
        LOGGER.debug("current config:")
        result = kls.get_current_config()
        return result
        # result = self.final
        # print(text.to_json(result))


class CliPlugin(PynchonPlugin):
    cli_label = 'default'

    @typing.classproperty
    def click_entry(kls):
        from pynchon.bin import entry

        return entry.entry

    @staticmethod
    def init_cli_group(kls):
        def plugin_main():
            pass

        plugin_main.__doc__ = (kls.__doc__ or "").lstrip()
        # f"""subcommands for `{kls.name}` plugin"""
        plugin_main = common.groop(
            getattr(kls, 'cli_name', kls.name), parent=kls.click_entry
        )(plugin_main)
        return plugin_main

    @staticmethod
    def init_cli(kls):
        """ """
        # import functools
        from pynchon import config
        from pynchon.plugins.base import Base

        if kls != Base:
            config.finalize()

        plugin_main = kls.init_cli_group(kls)
        obj = kls.instance
        for method_name in kls.__methods__:
            fxn = getattr(obj, method_name)
            # @functools.wraps(fxn)
            def wrapper(*args, fxn=fxn, **kwargs):
                LOGGER.debug(f"calling {fxn} from wrapper")
                result = fxn(*args, **kwargs)
                print(text.to_json(result))
                return result

            # wrapper = lambda *args, **kargs: print(json.dumps(fxn(*args,**kargs) or {}, indent=2))
            # wrapper.__name__=fxn.__name__
            wrapper.__doc__ = (fxn.__doc__ or "").lstrip()
            # from pynchon.util import tagging

            # import IPython; IPython.embed()
            # tags = tagging.TAGGERS[fxn.__qualname__]
            tmp = common.kommand(
                fxn.__name__.replace('_', '-'),
                parent=plugin_main,
            )(wrapper)
            tags = getattr(obj, 'tags', None)
            tags = tags.get_tags(fxn) if tags is not None else {}
            click_aliases = tags.get('click_aliases', []) if tags else []
            for alias in click_aliases:
                # LOGGER.critical(f"creating alias for {fxn} @ {alias}")
                tmp = common.kommand(
                    alias.replace('_', '-'),
                    parent=plugin_main,
                    help=f'alias for `{alias}`',
                )(wrapper)

        return plugin_main


class ContextPlugin(CliPlugin):
    cli_label = 'provider'
    contribute_plan_apply = False


class BasePlugin(CliPlugin):
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


class ShyPlanner(BasePlugin):
    cli_label = 'planner'
    contribute_plan_apply = False

    def plan(self, config=None) -> typing.List:
        """create plan for this plugin"""
        self.state = config
        return []

    def apply(self, config=None) -> None:
        """executes the plan for this plugin"""
        plan = self.plan(config=config)
        from pynchon.util.os import invoke

        return [invoke(p).succeeded for p in plan]


class Planner(ShyPlanner):
    cli_label = 'planner'
    contribute_plan_apply = True
