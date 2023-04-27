"""
pynchon: a utility for docs generation and template-rendering
"""
import collections
from gettext import gettext as _

import click

from pynchon import abcs

from pynchon.util import typing

plugins = typing.lazy_import(
    'pynchon.plugins',
)


class RootGroup(click.Group):
    def format_commands(
        self, ctx: click.Context, formatter: click.HelpFormatter
    ) -> None:

        # with try_import() as registry_import:  # use try_import as a context manager
        #     from pynchon.plugins import registry as plugin_registry
        # registry_import.check()  # check if the import was ok or raise a meaningful exception
        commands = []
        for subcommand in self.list_commands(ctx):
            cmd = self.get_command(ctx, subcommand)
            if cmd is None or cmd.hidden:
                continue
            commands.append((subcommand, cmd))
        if len(commands):
            # allow for 3 times the default spacing
            limit = formatter.width - 6 - max(len(cmd[0]) for cmd in commands)
            plugin_subs = dict(
                [
                    [getattr(v['kls'], 'cli_name', v['kls'].name), v]
                    for k, v in plugins.registry.items()
                ]
            )

            toplevel = dict(core=[], plugins=collections.defaultdict(list))
            for subcommand, cmd in commands:
                help = cmd.get_short_help_str(limit)
                is_plugin = subcommand in plugin_subs
                label = ''
                if is_plugin:
                    plugin_kls = plugin_subs[subcommand]['kls']
                    if issubclass(plugin_kls, (abcs.Plugin,)):
                        tmp = plugin_kls.cli_label
                        toplevel['plugins'][tmp].append((subcommand, f"{cmd.help}"))
                else:
                    toplevel['core'].append((f"{subcommand}", f"{cmd.help}"))
                # category.append((f"{subcommand}", f"{label}{help}"))

            if toplevel['core']:

                def search(rows, term):
                    return [i for i, (subc, subh) in enumerate(rows) if subc == term][0]

                order = ['plan', 'apply', 'config', 'config-raw']
                ordering = []
                for o in order:
                    for subc, subh in toplevel['core']:
                        if subc == o:
                            ordering.append((subc, subh))
                            toplevel['core'].remove((subc, subh))
                toplevel['core'] = ordering + toplevel['core']
                with formatter.section(_("Core Subcommands")):
                    formatter.write_dl(toplevel['core'])

            for label in toplevel['plugins']:
                with formatter.section(_(f"{label.title()} Subcommands")):
                    formatter.write_dl(toplevel['plugins'][label])

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
@click.option('--plugins', help='shortcut for `--set plugins=...`')
@click.option('--set', 'set_config', help='config overrides')
@click.group("pynchon", cls=RootGroup)
def entry(plugins:str='', set_config:str=''):
    pass
