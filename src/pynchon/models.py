""" pynchon.models
"""
from pynchon.util import typing, lme  # noqa

from pynchon import shimport
from pynchon.api import project
from pynchon.app import app
from pynchon.bin import entry
from pynchon.cli import click, common
from pynchon.abcs.plugin import Plugin as AbstractPlugin
from pynchon.plugins.util import get_plugin_obj
from pynchon.util.tagging import tags

from pynchon.util import lme, typing  # noqa

config_mod = shimport.lazy(
    'pynchon.config',
)

LOGGER = lme.get_logger(__name__)
events = app.events


@tags(cli_label='<<Abstract>>')
class PynchonPlugin(AbstractPlugin):
    """
    Pynchon-specific plugin-functionality
    """

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


@tags(cli_label='<<Default>>')
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
        cached = kls._finalized_click_groups.get(kls, None)

        if cached is not None:
            return cached

        def plugin_main():
            pass

        plugin_main.__doc__ = (kls.__doc__ or "").lstrip()
        gname = getattr(kls, 'cli_name', kls.name)
        groop = common.groop(gname, parent=kls.click_entry)
        plugin_main = groop(plugin_main)
        kls._finalized_click_groups[kls] = plugin_main
        return plugin_main

    @PynchonPlugin.classmethod_dispatch(click.Group)
    def click_acquire(kls, grp: click.Group):  # noqa F811
        """ """
        parent = kls.click_group
        LOGGER.critical(
            f"{kls.__name__} acquires group@`{grp.name}` to: parent@`{parent.name}`"
        )
        raise NotImplementedError("groups are not supported yet!")

    @PynchonPlugin.classmethod_dispatch(typing.FunctionType)
    def click_acquire(kls, fxn: typing.FunctionType):  # noqa F811
        """ """
        msg = f'{kls.__name__} acquires naked fxn: {fxn.__name__}'
        assert fxn.__annotations__
        cmd_name = f'{fxn.__name__}'.replace('_', '-')
        kls.click_group.add_command(click.command(cmd_name)(fxn))

    @PynchonPlugin.classmethod_dispatch(click.Command)
    def click_acquire(kls, cmd: click.Command):  # noqa F811
        """ """
        parent = kls.click_group
        LOGGER.info(f"{kls.__name__} acquires {cmd.name} to: group@{parent.name}")
        parent.add_command(cmd)
        return parent

    @classmethod
    def init_cli(kls):
        """ """
        LOGGER.info(f"{kls.__name__}.init_cli:")
        from pynchon.plugins.core import Core

        if kls != Core:
            config_mod.finalize()

        obj = kls.instance
        if obj is None:
            err = f"{kls.__name__}.`instance` is not ready?"
            LOGGER.warning(err)
            raise ValueError(err)

        cli_commands = []
        for method_name in kls.__methods__:
            # LOGGER.info(f"  {kls.__name__}.init_cli: {method_name}")
            fxn = obj and getattr(obj, method_name, None)
            if fxn is None:
                msg = f'    retrieved empty `{method_name}` from {obj}!'
                LOGGER.critical(msg)
                raise TypeError(msg)

            tags = getattr(obj, 'tags', None)
            tags = tags.get_tags(fxn) if tags is not None else {}
            click_aliases = tags.get('click_aliases', []) if tags else []

            def wrapper(*args, fxn=fxn, **kwargs):
                LOGGER.debug(f"calling {fxn} from wrapper")
                result = fxn(*args, **kwargs)
                # FIXME: this wraps twice?
                # from rich import print_json
                # print_json(text.to_json(result))
                return result

            commands = [kls.click_create_cmd(fxn, wrapper=wrapper, alias=None)]
            for alias in click_aliases:
                tmp = kls.click_create_cmd(
                    fxn,
                    alias=alias,
                    wrapper=wrapper,
                )
                commands.append(tmp)
            cli_commands += commands

        # if method_name == 'bootstrap':
        msg = [cmd.name for cmd in cli_commands]
        msg = ' | '.join(msg)
        LOGGER.info(f" created commands: '{msg}'")
        kls.init_cli_children()
        return kls.click_group

    @classmethod
    def init_cli_children(kls):
        """ """
        cli_subsumes = getattr(kls, 'cli_subsumes', [])
        cli_subsumes and LOGGER.info(
            f"{kls.__name__} honoring `cli_subsumes`:\n\t{cli_subsumes}"
        )
        for fxn in cli_subsumes:
            kls.click_acquire(fxn)

    @classmethod
    def click_create_cmd(kls, fxn: typing.Callable, wrapper=None, alias: str = None):
        """ """
        assert fxn
        assert wrapper
        name = alias or fxn.__name__
        name = name.replace('_', '-')
        help = f'(alias for `{alias}`)' if alias else (fxn.__doc__ or "")
        help = help.lstrip()
        cmd = common.kommand(
            name,
            help=help,
            alias=alias,
            parent=kls.click_group,
        )(wrapper)
        options = getattr(fxn, '__click_params__', [])
        cmd.params += options
        return cmd


@tags(cli_label='Provider')
class Provider(CliPlugin):
    """
    ProviderPlugin provides context-information, but little other functionality
    """

    cli_label = 'Provider'
    contribute_plan_apply = False
    # class config_class(abcs.Config):
    #     config_key = None


@tags(cli_label='NameSpace')
class NameSpace(CliPlugin):
    """
    `CliNamespace` collects functionality
    from elsewhere under a single namespace
    """

    cli_label = 'NameSpace'
    contribute_plan_apply = False
    priority = -1


@tags(cli_label='Tool')
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


@tags(cli_label='Planner')
class AbstractPlanner(BasePlugin):
    """
    AbstractPlanner is a plugin-type that provides plan/apply basics
    """

    cli_label = 'Planner'

    def plan(self, config=None) -> typing.List:
        """Creates a plan for this plugin"""
        events.lifecycle.send(
            # writes status event (used by the app-console)
            stage=f"Planning for `{self.__class__.name}`"
        )
        self.state = config
        return []

    def apply(self, config=None) -> None:
        """Executes the plan for this plugin"""
        from pynchon.util.os import invoke

        events.lifecycle.send(
            # write status event (used by the app-console)
            stage=f"applying for `{self.__class__.name}`"
        )
        plan = self.plan(config=config)
        return [invoke(p).succeeded for p in plan]


class ShyPlanner(AbstractPlanner):
    """
    ShyPlanner uses plan/apply workflows, but they must be
    executed directly.  ProjectPlugin (or any other parent plugins)
    won't include this as a sub-plan.
    """

    contribute_plan_apply = False


@tags(cli_label='Manager')
class Manager(ShyPlanner):
    cli_label = 'Manager'


class Planner(ShyPlanner):
    """
    Planner uses plan/apply workflows, and contributes it's plans
    to ProjectPlugin (or any other parent plugins).
    """

    contribute_plan_apply = True
