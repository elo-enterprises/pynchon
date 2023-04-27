""" pynchon.models
"""
# from memoized_property import memoized_property

from pynchon.bin import common, entry
from pynchon.util import typing, lme, text
from pynchon.abcs.plugin import Plugin as AbstractPlugin
from pynchon.events import status
from pynchon.api import project
from pynchon.plugins.util import get_plugin_obj

config_mod = typing.lazy_import(
    'pynchon.config',
)

LOGGER = lme.get_logger(__name__)


class PynchonPlugin(AbstractPlugin):
    """ Pynchon-specific plugin-functionality """
    cli_label = 'abstract'

    @property
    def plugin_config(self):
        """ """
        return self.get_current_config()

    @typing.classproperty
    def project_config(self):
        """ class-property: finalized project-config """
        return project.get_config()

    @typing.classproperty
    def instance(kls):
        """ class-property: the instance for this plugin """
        return get_plugin_obj(kls.name)

    @classmethod
    def get_current_config(kls):
        """ class-method: get the current config for this plugin """
        result = getattr(config_mod, getattr(kls.config_kls, 'config_key', kls.name))
        return result

    def config(self):
        """ Shows current config for this plugin """
        kls = self.__class__
        LOGGER.debug(f"config class: {kls.config_kls}")
        LOGGER.debug("current config:")
        result = kls.get_current_config()
        return result


class CliPlugin(PynchonPlugin):
    cli_label = 'default'

    @typing.classproperty
    def click_entry(kls):
        """ """
        return entry.entry

    @staticmethod
    def init_cli_group(kls):
        """ """
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
    """
    ProviderPlugin provides context-information, but little other functionality
    """
    cli_label = 'provider'
    contribute_plan_apply = False
Provider = ContextPlugin

class CliAliases(CliPlugin):
    """
    CliAliases collect functionality from elsewhere under a namespace
    """
    cli_label = 'Aliased'
    priority = -1

class ToolPlugin(CliPlugin):
    """
    Tool plugins may have their own config, but generally should not need project-config.
    """
    cli_label = 'tool'

class BasePlugin(CliPlugin):
    """
    The default plugin-type most new plugins will use
    """
    priority = 10

class AbstractPlanner(BasePlugin):
    """
    AbstractPlanner is a plugin-type that provides plan/apply basics
    """
    cli_label = 'planner'

    def plan(self, config=None) -> typing.List:
        """Creates a plan for this plugin """
        # write status event (used by the app-console)
        status.update(stage=f"planning for `{self.__class__.name}`")
        self.state = config
        return []

    def apply(self, config=None) -> None:
        """ Executes the plan for this plugin """
        # write status event (used by the app-console)
        status.update(stage=f"applying for `{self.__class__.name}`")
        plan = self.plan(config=config)
        from pynchon.util.os import invoke

        return [invoke(p).succeeded for p in plan]

class ShyPlanner(AbstractPlanner):
    """
    ShyPlanner uses plan/apply workflows, but they must be
    executed directly.  ProjectPlugin (or any other parent plugins)
    won't include this as a sub-plan.
    """
    contribute_plan_apply = False


class Planner(ShyPlanner):
    """
    Planner uses plan/apply workflows, and contributes it's plans
    to ProjectPlugin (or any other parent plugins).
    """
    contribute_plan_apply = True
