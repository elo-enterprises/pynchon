"""
"""
import typing
import collections

import pydash

from pynchon import fleks, events, api, cli, shimport
from pynchon.bin import entry
from pynchon.plugins import util as plugins_util

from . import validators

from pynchon.util import typing, tagging, lme  # noqa


config_mod = shimport.lazy(
    'pynchon.config',
)

LOGGER = lme.get_logger(__name__)


@tagging.tags(cli_label='<<Abstract>>')
class PynchonPlugin(fleks.Plugin):
    """
    Pynchon-specific plugin-functionality
    """

    name = '<<Abstract>>'
    cli_label = '<<Abstract>>'
    __class_validators__ = [
        validators.require_conf_key,
        validators.warn_config_kls,
    ]

    @typing.classproperty
    def instance(kls):
        """class-property: the instance for this plugin"""
        return plugins_util.get_plugin_obj(kls.name)

    @typing.classproperty
    def project_config(self):
        """class-property: finalized project-config"""
        return api.project.get_config()

    @classmethod
    def get_config_key(kls):
        """ """
        default = kls.name.replace('-', '_')
        config_kls = getattr(kls, 'config_class', None)
        return getattr(config_kls, 'config_key', default) or default

    @classmethod
    def get_current_config(kls):
        """class-method: get the current config for this plugin"""
        conf_class = getattr(kls, 'config_class', None)
        if conf_class is None:
            return {}
        conf_key = kls.get_config_key()
        result = getattr(config_mod, conf_key)
        return result

    @property
    def plugin_config(self):
        """ """
        return self.get_current_config()

    @property
    def siblings(self):
        """ """
        result = []
        from pynchon.plugins import registry

        for plugin in registry.keys():
            if plugin == self.name:
                continue
            result.append(plugins_util.get_plugin_obj(plugin))
        result = sorted(result, key=lambda p: p.priority)
        return collections.OrderedDict([p.name, p] for p in result)

    def cfg(self):
        """Shows current config for this plugin"""
        kls = self.__class__
        conf_class = getattr(kls, 'config_class', None)
        conf_class_name = conf_class.__name__ if conf_class else '(None)'
        LOGGER.debug(f"config class: {conf_class_name}")
        LOGGER.debug("current config:")
        result = kls.get_current_config()
        return result

    @property
    def config(self):
        """ """
        return self.cfg()

    def __mod__(self, key: str, strict=True):
        """shortcut for accessing global pynchon-config"""
        try:
            return self.project_config[key]
        except (KeyError,) as exc:
            fallback = pydash.get(self.project_config, key, None)
            if fallback:
                return fallback
            else:
                if strict:
                    raise

    def __floordiv__(self, key: str, strict=False):
        """ """
        return self.__mod__(key, strict=strict)

    def __getitem__(self, key: str):
        """shortcut for accessing local plugin-config"""
        if isinstance(key, (slice,)):
            start, stop, step = key.start, key.stop, key.step
            try:
                if start:
                    result = self[start]
                if stop:
                    result = self % stop
            except (KeyError,) as exc:
                if step is not None:
                    return step
                else:
                    raise
            else:
                return result
        else:
            try:
                return self.config[key]
            except (KeyError,) as exc:
                fallback = pydash.get(self.config, key)
                if fallback:
                    return fallback
                else:
                    raise


@tagging.tags(cli_label='<<Default>>')
class CliPlugin(PynchonPlugin):
    cli_label = '<<Default>>'
    _finalized_click_groups = dict()

    @typing.classproperty
    def click_entry(kls):
        """ """
        return entry

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
        groop = cli.common.groop(gname, parent=kls.click_entry)
        plugin_main = groop(plugin_main)
        kls._finalized_click_groups[kls] = plugin_main
        return plugin_main

    @PynchonPlugin.classmethod_dispatch(cli.click.Group)
    def click_acquire(kls, group: cli.click.Group):  # noqa F811
        """ """
        parent = kls.click_group
        LOGGER.info(
            f"{kls.__name__} acquires group@`{group.name}` to: parent@`{parent.name}`"
        )
        return cli.click.group_merge(group, parent)

    @PynchonPlugin.classmethod_dispatch(typing.FunctionType)
    def click_acquire(kls, fxn: typing.FunctionType):  # noqa F811
        """ """
        msg = f'{kls.__name__} acquires naked fxn: {fxn.__name__}'
        assert fxn.__annotations__
        cmd_name = f'{fxn.__name__}'.replace('_', '-')
        kls.click_group.add_command(cli.click.command(cmd_name)(fxn))

    @PynchonPlugin.classmethod_dispatch(cli.click.Command)
    def click_acquire(kls, cmd: cli.click.Command):  # noqa F811
        """ """
        parent = kls.click_group
        LOGGER.info(f"{kls.__name__} acquires {cmd.name} to: group@{parent.name}")
        parent.add_command(cmd)
        return parent

    @classmethod
    def init_cli(kls):
        """ """
        events.lifecycle.send(kls, plugin='initializing CLI')

        from pynchon.plugins.core import Core  # noqa

        if kls != Core:
            config_mod.finalize()

        obj = kls.instance
        if obj is None:
            err = f"{kls.__name__}.`instance` is not ready?"
            LOGGER.warning(err)
            raise ValueError(err)

        cli_commands = []
        group_names = [
            name
            for name in dir(kls)
            if name not in 'click_entry click_group'.split()
            and isinstance(getattr(kls, name), (cli.click.Group,))
        ]
        cmd_names = [
            name
            for name in dir(kls)
            if name not in 'click_entry click_group'.split()
            and isinstance(getattr(kls, name), (cli.click.Command,))
        ]
        for group_name in group_names:
            gr = getattr(obj, group_name)
            cli_commands.append(gr)
            kls.click_acquire(gr)

        for cmd_name in cmd_names:
            gr = getattr(obj, cmd_name)
            cli_commands.append(gr)
            kls.click_acquire(gr)

        for method_name in kls.__methods__:
            # LOGGER.info(f"  {kls.__name__}.init_cli: {method_name}")
            fxn = obj and getattr(obj, method_name, None)
            if fxn is None:
                msg = f'    retrieved empty `{method_name}` from {obj}!'
                LOGGER.critical(msg)
                raise TypeError(msg)

            # tags = getattr(obj, 'tags', {})
            # tags = tags.get(fxn) if tags else {}
            tags = {}
            if not tags and type(fxn) == typing.MethodType:
                cfxn = getattr(fxn.__self__.__class__, fxn.__name__)
                tags = tagging.tags.get(cfxn, {})
            hidden = tags.get('click_hidden', False) if tags else False
            click_aliases = tags.get('click_aliases', []) if tags else []
            publish_to_cli = tags.get('publish_to_cli', True)
            if not publish_to_cli:
                continue

            def wrapper(*args, fxn=fxn, **kwargs):
                LOGGER.debug(f"calling {fxn} from wrapper")
                result = fxn(*args, **kwargs)
                # FIXME: this wraps twice?
                # from rich import print_json
                # print_json(text.to_json(result))
                # if hasattr(result, 'display'):
                rproto = getattr(result, '__rich__', None)
                if rproto:
                    from pynchon.util.lme import CONSOLE

                    CONSOLE.print(result)
                return result

            commands = [
                kls.click_create_cmd(fxn, wrapper=wrapper, hidden=hidden, alias=None)
            ]
            for alias in click_aliases:
                tmp = kls.click_create_cmd(
                    fxn, alias=alias, wrapper=wrapper, hidden=hidden
                )
                commands.append(tmp)
            cli_commands += commands

        msg = [cmd.name for cmd in cli_commands]
        if len(msg) > 1:
            events.lifecycle.send(kls, plugin=f'created {len(msg)} commands')
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
    def click_create_cmd(
        kls, fxn: typing.Callable, wrapper=None, alias: str = None, **click_kwargs
    ) -> cli.click.Command:
        """ """
        assert fxn
        assert wrapper
        name = alias or fxn.__name__
        name = name.replace('_', '-')
        help = f'(alias for `{alias}`)' if alias else (fxn.__doc__ or "")
        help = help.lstrip()
        cmd = cli.common.kommand(
            name, help=help, alias=alias, parent=kls.click_group, **click_kwargs
        )(wrapper)
        options = getattr(fxn, '__click_params__', [])
        cmd.params += options
        return cmd

    @tagging.tags(
        click_aliases=['sh'],
        click_hidden=True,
    )
    @cli.click.option('--command', '-c', default='')
    def shell(self, command: str = '') -> None:
        """drop to debugging shell"""
        before = locals()
        if command:
            self.logger.warning(f'executing command: {command} ')
            return eval(command)
        else:
            import IPython

            IPython.embed()  # noqa
        after = dict([[k, v] for k, v in locals().items() if k not in before])
        LOGGER.warning(f"namespace changes: {after}")


@tagging.tags(cli_label='Provider')
class Provider(CliPlugin):
    """
    ProviderPlugin provides context-information,
    but little other functionality
    """

    cli_label = 'Provider'
    contribute_plan_apply = False
    priority = 2
    __class_validators__ = [
        validators.require_conf_key,
        # validators.warn_config_kls,
    ]


@tagging.tags(cli_label='Tool')
class ToolPlugin(CliPlugin):
    """
    Tool plugins may have their own config,
    but generally should not need project-config.
    """

    cli_label = 'Tool'
    contribute_plan_apply = False
    __class_validators__ = [
        # validators.require_conf_key,
        # validators.warn_config_kls,
    ]


class BasePlugin(CliPlugin):
    """
    The default plugin-type most new plugins will use
    """

    priority = 10


@tagging.tags(cli_label='NameSpace')
class NameSpace(CliPlugin):
    """
    `CliNamespace` collects functionality
    from elsewhere under a single namespace
    """

    cli_label = 'NameSpace'
    contribute_plan_apply = False
    priority = 1
