"""
pynchon: a utility for docs generation and template-rendering
"""
from gettext import gettext as _

import click

from pynchon import models


class RootGroup(click.Group):
    def format_commands(
        self, ctx: click.Context, formatter: click.HelpFormatter
    ) -> None:
        """Extra format methods for multi methods that adds all the commands
        after the options.
        """
        from pynchon.plugins import registry as plugin_registry

        commands = []
        for subcommand in self.list_commands(ctx):
            cmd = self.get_command(ctx, subcommand)
            # What is this, the tool lied about a command.  Ignore it
            if cmd is None:
                continue
            if cmd.hidden:
                continue

            commands.append((subcommand, cmd))
        # allow for 3 times the default spacing
        if len(commands):
            limit = formatter.width - 6 - max(len(cmd[0]) for cmd in commands)
            plugin_subs = dict(
                [
                    [getattr(v['kls'], 'cli_name', v['kls'].name), v]
                    for k, v in plugin_registry.items()
                ]
            )
            rows_core = []
            rows_plugins = []
            for subcommand, cmd in commands:
                help = cmd.get_short_help_str(limit)
                is_plugin = subcommand in plugin_subs
                label = ''
                if is_plugin:
                    plugin_kls = plugin_subs[subcommand]['kls']
                    if issubclass(plugin_kls, (models.ContextPlugin,)):
                        tmp = plugin_kls.cli_label
                        label = f'({tmp}) '
                    category = rows_plugins
                else:
                    category = rows_core
                category.append((f"{subcommand}", f"{label}{help}"))
            if rows_core:

                def search(rows, term):
                    return [i for i, (subc, subh) in enumerate(rows) if subc == term][0]

                order = ['plan', 'apply', 'config', 'config-raw']
                # rows_core = [
                #     for name in
                # ]
                ordering = []
                for o in order:
                    for subc, subh in rows_core:
                        if subc == o:
                            ordering.append((subc, subh))
                            rows_core.remove((subc, subh))
                rows_core = ordering + rows_core
                with formatter.section(_("Core Subcommands")):
                    formatter.write_dl(rows_core)
            if rows_plugins:
                with formatter.section(_("Plugin-entrypoints")):
                    formatter.write_dl(rows_plugins)

    # def format_usage(self, ctx, formatter):
    #     from pynchon.plugins.base import Base
    #     core_cmds = " | ".join([m.replace('_', '-') for m in Base.__methods__])
    #     core_cmds = "{ " + core_cmds + " }"
    #     plugin_cmds = ".."
    #     cmd = ctx.command
    #     m_sub = cmd.subcommand_metavar
    #     m_op = cmd.options_metavar
    #     tmp = ' '.join(m_sub.split()[1:])
    #     formatter.write(
    #         ''.join(
    #             [
    #                 __doc__.lstrip(),
    #                 'Usage:\n',
    #                 f'\n\t{cmd.name} {m_op} {m_sub}',
    #                 f'\n\t{cmd.name} {m_op} {core_cmds} {tmp}',
    #                 f'\n\t{cmd.name} {m_op} PLUGIN_NAME {tmp}',
    #             ]
    #         )
    #     )


@click.version_option()
@click.group("pynchon", cls=RootGroup)
def entry():
    pass
