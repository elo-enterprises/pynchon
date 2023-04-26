"""
pynchon: a utility for docs generation and template-rendering
"""
import click


class RootGroup(click.Group):
    def format_commands(
        self, ctx: click.Context, formatter: click.HelpFormatter
    ) -> None:
        """Extra format methods for multi methods that adds all the commands
        after the options.
        """
        from gettext import gettext as _

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

            rows_core = []
            rows_plugins = []
            for subcommand, cmd in commands:
                help = cmd.get_short_help_str(limit)
                if subcommand in plugin_registry:
                    rows_plugins.append((f"{subcommand}", help))
                else:
                    rows_core.append((f"{subcommand}", help))
            if rows_core:
                with formatter.section(_("Core Subcommands")):
                    formatter.write_dl(rows_core)
            if rows_plugins:
                with formatter.section(_("Plugin-entrypoints")):
                    formatter.write_dl(rows_plugins)

    def format_usage(self, ctx, formatter):
        from pynchon.plugins.base import Base

        core_cmds = " | ".join([m.replace('_', '-') for m in Base.__methods__])
        core_cmds = "{ " + core_cmds + " }"
        plugin_cmds = ".."
        cmd = ctx.command
        m_sub = cmd.subcommand_metavar
        m_op = cmd.options_metavar
        tmp = ' '.join(m_sub.split()[1:])
        formatter.write(
            ''.join(
                [
                    __doc__.lstrip(),
                    'Usage:\n',
                    f'\n\t{cmd.name} {m_op} {m_sub}',
                    f'\n\t{cmd.name} {m_op} {core_cmds} {tmp}',
                    f'\n\t{cmd.name} {m_op} PLUGIN_NAME {tmp}',
                ]
            )
        )


@click.version_option()
@click.group("pynchon", cls=RootGroup)
def entry():
    pass
