""" pynchon.models
"""
# from memoized_property import memoized_property

from pynchon.api import project
from pynchon.app import events
from pynchon.bin import common, entry
from pynchon.util import typing, importing, lme, text
from pynchon.abcs.plugin import Plugin as AbstractPlugin
from pynchon.plugins.util import get_plugin_obj

config_mod = importing.lazy_import(
    'pynchon.config',
)

LOGGER = lme.get_logger(__name__)


class PynchonPlugin(AbstractPlugin):
    """Pynchon-specific plugin-functionality"""

    cli_label = '<<Abstract>>'

    @property
    def plugin_config(self):
        """ """
        return self.get_current_config()

    @typing.classproperty
    def project_config(self):
        """class-property: finalized project-config"""
        return project.get_config()

    @typing.classproperty
    def instance(kls):
        """class-property: the instance for this plugin"""
        return get_plugin_obj(kls.name)

    @classmethod
    def get_current_config(kls):
        """class-method: get the current config for this plugin"""
        assert kls.config_class
        conf_key = getattr(kls.config_class, 'config_key', kls.name)
        assert conf_key
        result = getattr(config_mod, conf_key)
        return result

    def config(self):
        """Shows current config for this plugin"""
        kls = self.__class__
        LOGGER.debug(f"config class: {kls.config_class}")
        LOGGER.debug("current config:")
        result = kls.get_current_config()
        return result


import click


class CliPlugin(PynchonPlugin):
    cli_label = '<<Default>>'
    _finalized_click_groups = dict()

    @typing.classproperty
    def click_entry(kls):
        """ """
        return entry.entry

    @typing.classproperty
    def click_group(kls):
        """ """
        last_group = kls._finalized_click_groups.get(kls, None)

        if last_group is not None:
            return last_group

        def plugin_main():
            pass

        plugin_main.__doc__ = (kls.__doc__ or "").lstrip()
        # f"""subcommands for `{kls.name}` plugin"""
        plugin_main = common.groop(
            getattr(kls, 'cli_name', kls.name), parent=kls.click_entry
        )(plugin_main)
        kls._finalized_click_groups[kls] = plugin_main
        return plugin_main

    @classmethod
    def click_acquire(kls, cmd_or_group: typing.Callable):
        """ """
        parent = kls.click_group
        cmd = cmd_or_group if isinstance(cmd_or_group, click.Command) else None
        grp = cmd_or_group if isinstance(cmd_or_group, click.Group) else None
        fxn = cmd_or_group if isinstance(cmd_or_group, typing.FunctionType) else None
        if grp:
            LOGGER.critical(f"{kls} acquires {grp} to: {parent}")
            # parent.add_group(fxn)
            raise NotImplementedError("groups are not supported yet!")
        elif cmd:
            LOGGER.info(f"{kls} acquires {cmd} to: {parent}")
            parent.add_command(cmd)
            return parent
        elif fxn:
            msg = f'{kls} acquires naked fxn: {fxn}'
            LOGGER.critical(msg)
            assert fxn.__annotations__
            # for k,v in fxn.__annotations__.items()
            #     click.option('--output',)
            parent.add_command(click.command(f'{fxn.__name__}'.replace('_', '-'))(fxn))
        else:
            err = f'{kls} unrecognized type to acquire: {cmd_or_group}'
            LOGGER.critical(err)
            raise TypeError(err)

    @classmethod
    def init_cli(kls):
        """ """
        from pynchon import config
        from pynchon.plugins.core import Core

        if kls != Core:
            config.finalize()

        obj = kls.instance
        for method_name in kls.__methods__:
            fxn = getattr(obj, method_name)
            assert fxn, f'retrieved empty {method_name} from {obj}'
            tags = getattr(obj, 'tags', None)
            tags = tags.get_tags(fxn) if tags is not None else {}
            click_aliases = tags.get('click_aliases', []) if tags else []
            # @functools.wraps(fxn)
            def wrapper(*args, fxn=fxn, **kwargs):
                LOGGER.debug(f"calling {fxn} from wrapper")
                result = fxn(*args, **kwargs)
                from rich import print_json

                print_json(text.to_json(result))
                return result

            kls.click_create_cmd(fxn, wrapper=wrapper)
            for alias in click_aliases:
                kls.click_create_cmd(fxn, wrapper=wrapper, alias=alias)

        cli_includes = getattr(kls, 'cli_includes', [])
        cli_includes and LOGGER.debug(f"{kls} honoring `cli_includes`: {cli_includes}")
        for fxn in cli_includes:
            kls.click_acquire(fxn)

        return kls.click_group

    @classmethod
    def click_create_cmd(kls, fxn: typing.Callable, wrapper=None, alias: str = None):
        """ """
        assert fxn
        assert wrapper
        name = alias or fxn.__name__
        name = name.replace('_', '-')
        help = f'(alias for `{alias}`)' if alias else (fxn.__doc__ or "")
        help = help.lstrip()
        msg = f"creating command `{name}` for {fxn} {'alias' if alias else ''}"
        if typing.new_in_class(fxn.__name__, kls):
            LOGGER.info(msg)
        tmp = common.kommand(
            name,
            parent=kls.click_group,
            help=help,
        )(wrapper)
        return tmp


class Provider(CliPlugin):
    """
    ProviderPlugin provides context-information, but little other functionality
    """

    cli_label = 'Provider'
    contribute_plan_apply = False


class NameSpace(CliPlugin):
    """
    `CliNamespace` collects functionality
    from elsewhere under a single namespace
    """

    cli_label = 'NameSpace'
    contribute_plan_apply = False
    priority = -1


class ToolPlugin(CliPlugin):
    """
    Tool plugins may have their own config, but generally should not need project-config.
    """

    cli_label = 'Tool'
    contribute_plan_apply = False


class BasePlugin(CliPlugin):
    """
    The default plugin-type most new plugins will use
    """

    priority = 10


class AbstractPlanner(BasePlugin):
    """
    AbstractPlanner is a plugin-type that provides plan/apply basics
    """

    cli_label = 'Planner'

    def plan(self, config=None) -> typing.List:
        """Creates a plan for this plugin"""
        # write status event (used by the app-console)
        events.status.update(stage=f"planning for `{self.__class__.name}`")
        self.state = config
        return []

    def apply(self, config=None) -> None:
        """Executes the plan for this plugin"""
        # write status event (used by the app-console)
        events.status.update(stage=f"applying for `{self.__class__.name}`")
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


class Manager(ShyPlanner):
    cli_label = 'Manager'


class Planner(ShyPlanner):
    """
    Planner uses plan/apply workflows, and contributes it's plans
    to ProjectPlugin (or any other parent plugins).
    """

    contribute_plan_apply = True
