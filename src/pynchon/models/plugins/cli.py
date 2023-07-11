""" pynchon.models.plugins.cli """
import functools

from pynchon import api, cli, events, fleks, shimport  # noqa
from pynchon.bin import entry  # noqa
from pynchon.util import lme, tagging, typing  # noqa

from .pynchon import PynchonPlugin  # noqa

LOGGER = lme.get_logger(__name__)
IPython = shimport.lazy("IPython")
classproperty = typing.classproperty
config_mod = shimport.lazy("pynchon.config")


@tagging.tags(cli_label="<<Default>>")
class CliPlugin(PynchonPlugin):
    cli_label = "<<Default>>"
    _finalized_click_groups = dict()

    @typing.classproperty
    def cli_path(kls):
        return f"{kls.click_entry.name} {kls.click_group.name}"

    @typing.classproperty
    def click_entry(kls):
        return entry

    @typing.classproperty
    def click_group(kls):
        cached = kls._finalized_click_groups.get(kls, None)
        grp_name = getattr(kls, "cli_name", kls.name)
        if cached is not None:
            return cached

        def plugin_main():
            pass

        plugin_main.__doc__ = (kls.__doc__ or "").lstrip().split("\n")[0]
        groop = cli.common.groop(
            grp_name,
            parent=kls.click_entry,
        )
        plugin_main = groop(plugin_main)
        kls._finalized_click_groups[kls] = plugin_main

        tags = tagging.tags.get(kls) or {}
        gr_aliases = list(set(tags.get("click_aliases", [])))
        for alias in gr_aliases:
            g2 = cli.click.group_copy(plugin_main, name=alias, hidden=True)
            kls.click_entry.add_command(g2)

        return plugin_main

    @classproperty
    @functools.lru_cache(maxsize=None)
    def click_commands(kls) -> typing.List[str]:
        return [
            name
            for name in dir(kls)
            if name not in kls.__class_properties__
            and all(
                [
                    name not in "click_entry click_group".split(),
                    isinstance(getattr(kls, name), (cli.click.Command,)),
                    not isinstance(getattr(kls, name), (cli.click.Group,)),
                ]
            )
        ]

    @classproperty
    @functools.lru_cache(maxsize=None)
    def click_subgroups(kls) -> typing.List[str]:
        return [
            name
            for name in dir(kls)
            if name not in kls.__class_properties__
            and all(
                [
                    name not in "click_entry click_group".split(),
                    isinstance(getattr(kls, name), (cli.click.Group,)),
                ]
            )
        ]

    @PynchonPlugin.classmethod_dispatch(cli.click.Group)
    def click_acquire(
        kls, group: cli.click.Group, copy: bool = False, **update_kwargs
    ):  # noqa F811
        """
        :param group: cli.click.Group:
        """
        parent = kls.click_group
        LOGGER.info(
            f"{kls.__name__} acquires group@`{group.name}` to: parent@`{parent.name}`"
        )
        if copy:
            group = cli.click.group_copy(group, **update_kwargs)
        return cli.click.group_merge(group, parent)

    @PynchonPlugin.classmethod_dispatch(typing.FunctionType)
    def click_acquire(
        kls,
        fxn: typing.FunctionType,
        copy: bool = False,
        **update_kwargs,
    ):  # noqa F811
        """
        :param kls:
        :param fxn: typing.FunctionType:
        """
        msg = f"{kls.__name__} acquires naked fxn: {fxn.__name__}"
        assert fxn.__annotations__
        cmd_name = f"{fxn.__name__}".replace("_", "-")
        kls.click_group.add_command(cli.click.command(cmd_name)(fxn))

    @PynchonPlugin.classmethod_dispatch(cli.click.Command)
    def click_acquire(
        kls, cmd: cli.click.Command, copy: bool = False, **update_kwargs
    ):  # noqa F811
        """ """
        parent = kls.click_group
        LOGGER.info(f"{kls.__name__} acquires {cmd.name} to: group@{parent.name}")
        if copy:
            cmd = cli.click.group_copy(cmd, **update_kwargs)
        parent.add_command(cmd)
        return parent

    @PynchonPlugin.classmethod_dispatch(typing.MethodType)
    def click_acquire(
        kls,
        cmd: typing.MethodType,
        copy: bool = False,  # irrelevant here
        **update_kwargs,
    ):  # noqa F811
        """ """
        fxn = cmd
        tags = tagging.tags[fxn]
        hidden = tags.get("click_hidden", False)
        click_aliases = tags.get("click_aliases", [])
        click_parent_plugin = tags.get("click_parent_plugin", None)
        publish_to_cli = tags.get("publish_to_cli", True)
        if not publish_to_cli:
            return
        if click_parent_plugin:
            update_kwargs.update(via=kls)
            kls = kls.siblings[click_parent_plugin]

        def wrapper(*args, fxn=fxn, **kwargs):
            LOGGER.critical(f"calling {fxn} from wrapper")
            result = fxn(*args, **kwargs)
            # FIXME: this wraps twice?
            # from rich import print_json
            # print_json(text.to_json(result))
            # if hasattr(result, 'display'):
            from pynchon.util.text import dumps
            # rproto = getattr(result, "__rich__", None)
            # if rproto:
            #     LOGGER.warning(f"rproto {result}")
            #     from pynchon.util.lme import CONSOLE
            print(dumps.json(result))
            #     CONSOLE.print(result)
            # return result
            # if not isinstance(result, (dict,list)):
            #     raise Exception([result, type(result)])
            # elif hasattr(result, "as_dict"):
            #     LOGGER.warning(f"as_dict {result}")
            #     rich.print(result.as_dict())
            # else:
            # return result

        commands = [
            kls.click_create_cmd(
                fxn,
                wrapper=wrapper,
                **{
                    **update_kwargs,
                    **dict(hidden=hidden, alias=None),
                },
            )
        ]
        for alias in click_aliases:
            tmp = kls.click_create_cmd(
                fxn,
                wrapper=wrapper,
                **{
                    **update_kwargs,
                    **dict(hidden=hidden, alias=alias),
                },
            )
            commands.append(tmp)
        return commands

    @classmethod
    def init_cli(kls) -> cli.click.Group:
        """ """
        events.lifecycle.send(kls, plugin="initializing CLI")
        Core = shimport.lazy("pynchon.plugins.core").Core
        if kls != Core:
            # FIXME: this is needed, .. but why?
            config_mod.finalize()

        obj = kls.instance
        if obj is None:
            err = f"{kls.__name__}.`instance` is not ready?"
            LOGGER.warning(err)
            raise ValueError(err)

        cli_commands = []

        for group_name in kls.click_subgroups:
            grp = getattr(obj, group_name)
            cli_commands.append(grp)
            kls.click_acquire(grp)
            tags = tagging.tags.get(grp) or {}
            click_aliases = tags.get("click_aliases", [])
            if click_aliases:
                raise NotImplementedError()

        # create commands from commands
        # these command-callbacks are bound to non-methods,
        # i.e. currently expecting `self` as a first argument
        for cmd_name in kls.click_commands:
            cmd = getattr(obj, cmd_name)
            if isinstance(cmd.callback, (typing.FunctionType,)):
                cmd.callback = typing.bind_method(cmd.callback, obj)
            cli_commands.append(cmd)
            kls.click_acquire(cmd)

        # create commands from methods
        for method_name in kls.__methods__:
            fxn = obj and getattr(obj, method_name, None)
            if fxn is None:
                msg = f"    retrieved empty `{method_name}` from {obj}!"
                LOGGER.critical(msg)
                raise TypeError(msg)
            result = kls.click_acquire(fxn)
            if result is not None:
                cli_commands += result
        msg = [cmd.name for cmd in cli_commands]
        if len(msg) > 1:
            events.lifecycle.send(kls, plugin=f"created {len(msg)} commands")
        kls.init_cli_children()
        return kls.click_group

    @classmethod
    def init_cli_children(kls):
        """
        :param kls:
        """
        cli_subsumes = getattr(kls, "cli_subsumes", [])
        cli_subsumes and LOGGER.info(
            f"{kls.__name__} honoring `cli_subsumes`:\n\t{cli_subsumes}"
        )
        for fxn in cli_subsumes:
            raise Exception(fxn)
            kls.click_acquire(fxn)

    @classmethod
    def click_create_cmd(
        kls,
        fxn: typing.Callable,
        via: typing.Any = None,
        wrapper=None,
        alias: str = None,
        **click_kwargs,
    ) -> cli.click.Command:
        """
        :param kls: param fxn: typing.Callable:
        :param alias: str:  (Default value = None)
        :param fxn: typing.Callable:
        :param **click_kwargs:
        """
        assert fxn
        assert wrapper
        via = via.__name__ if via else ""
        name = click_kwargs.pop("name", alias or fxn.__name__)
        name = name.replace("_", "-")
        alt = f"(alias for `{alias}`)" if alias else ""
        alt = alt or (f"(via {via})" if via else "")
        help = click_kwargs.pop(
            "help",
            (alt if alt else (fxn.__doc__ or "").lstrip().split("\n")[0]),
        )
        help = help.lstrip()
        cmd = cli.common.kommand(
            name, help=help, alias=alias, parent=kls.click_group, **click_kwargs
        )(wrapper)
        options = getattr(fxn, "__click_params__", [])
        cmd.params += options
        return cmd

    @tagging.tags(
        click_aliases=["sh"],
        click_hidden=True,
    )
    @cli.click.option("--command", "-c", default="")
    def shell(self, command: str = "") -> None:
        """drop to debugging shell
        :param command: str:  (Default value = '')
        """
        before = locals()
        if command:
            self.logger.warning(f"executing command: {command} ")
            return eval(command)
        else:
            IPython.embed()
        after = {k: v for k, v in locals().items() if k not in before}
        LOGGER.warning(f"namespace changes: {after}")
