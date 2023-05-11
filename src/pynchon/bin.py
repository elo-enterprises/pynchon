"""
pynchon: a utility for docs generation and template-rendering
"""
import collections
from gettext import gettext as _

from pynchon import fleks, cli, shimport

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)

click = cli.click
plugins = shimport.lazy('pynchon.plugins')


class RootGroup(click.Group):
    """ """

    def format_commands(
        self, ctx: click.Context, formatter: click.HelpFormatter
    ) -> None:
        """ """
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
                    if issubclass(plugin_kls, (fleks.Plugin,)):
                        tmp = plugin_kls.cli_label
                        toplevel['plugins'][tmp].append(
                            (f"{subcommand}:", f"{cmd.help}")
                        )
                else:
                    toplevel['core'].append((f"{subcommand}:", f"{cmd.help}"))
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
                with formatter.section(_("Core COMMANDs")):
                    formatter.write_dl(toplevel['core'])

            for label in toplevel['plugins']:
                with formatter.section(_(f"{label.title()} COMMANDs")):
                    formatter.write_dl(toplevel['plugins'][label])

    def format_usage(self, ctx, formatter):
        """ """
        # terminal_width, _ = click.get_terminal_size()
        terminal_width = 30
        click.echo('-' * terminal_width)
        super(RootGroup, self).format_usage(ctx, formatter)

    def parse_args(self, ctx, args):
        originals = [args.copy(), ctx.__dict__.copy()]
        copy = [x for x in args.copy() if x != '--help']
        ctx2 = default.make_context('default', copy)
        with ctx2:
            default.invoke(ctx2)
        return super(click.Group, self).parse_args(ctx, args)


@click.version_option()
@click.option('--plugins', help='shortcut for `--set plugins=...`')
@click.option('--set', 'set_config', help='config overrides')
@click.option('--get', 'get_config', help='config retrieval')
@click.group(
    "pynchon",
    cls=RootGroup,
)
def entry(
    plugins: str = '',
    set_config: str = '',
    get_config: str = '',
):
    """ """


@entry.command(
    'default',
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option('--plugins', help='shortcut for `--set plugins=...`')
@click.option('--set', 'set_config', help='config overrides')
@click.option('--get', 'get_config', help='config retrieval')
@click.argument('extra', nargs=-1)
@click.pass_context
def default(
    ctx, plugins: str = '', set_config: str = '', get_config: str = '', **kwargs  # noqa
):
    LOGGER.critical('top-level')
    setters = ctx.params.get('set_config', []) or []
    plugins = ctx.params.get('plugins', '')
    plugins and setters.append([f'pynchon.plugins={plugins.split(",")}'])
    setters and LOGGER.critical(f'--set: {setters}')
    bootstrap()


def bootstrap():
    from pynchon.app import app
    from pynchon.plugins import registry as plugin_registry

    from pynchon import config  # isort: skip

    events = app.events
    events.lifecycle.send(__name__, stage='Building CLIs from plugins..')
    registry = click_registry = {}
    loop = plugin_registry.items()
    for name, plugin_meta in loop:
        if name not in config.PLUGINS:
            LOGGER.warning(f"skipping `{name}`")
            continue
        plugin_kls = plugin_meta['kls']
        init_fxn = plugin_kls.init_cli
        # LOGGER.critical(f'\t{name}.init_cli: {init_fxn}')
        try:
            p_entry = init_fxn()
        except (Exception,) as exc:
            LOGGER.critical(f"  failed to initialize cli for {plugin_kls.__name__}:")
            LOGGER.critical(f"    {exc}")
            raise
        else:
            registry[name] = dict(plugin=plugin_kls, entry=p_entry)
