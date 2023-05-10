""" pynchon.plugins.plugins
"""
from pynchon import abcs, cli, models
from pynchon.util.os import invoke

from pynchon.util import lme, typing, tagging  # noqa

LOGGER = lme.get_logger(__name__)


class PluginsMan(models.Manager):
    """Meta-plugin for managing plugins"""

    name = "plugins"
    cli_name = 'plugins'

    @cli.click.option('--name')
    @cli.click.option('--template-skeleton', '-t', is_flag=True, default=False)
    def new(self, name: str = None, template_skeleton: bool = False) -> None:
        """Create new plugin from template (for devs)"""
        # FIXME: use cookie-cutter?
        plugins_d = abcs.Path(__file__).parents[0]
        template_plugin_f = plugins_d / '__template__.py'
        new_plugin_file = plugins_d / f'{name}.py'
        cmd = f'ls {new_plugin_file} || cp {template_plugin_f} {new_plugin_file} && git status'
        result = invoke(cmd, system=True).succeeded
        if template_skeleton:
            raise NotImplementedError()
        return result.succeeded

    @tagging.tags(click_aliases=['st', 'stat'])
    def status(self) -> typing.Dict:
        """Returns details about all known plugins"""
        result = typing.OrderedDict()
        for name, p in self.siblings.items():
            result[name] = dict(priority=p.priority, key=p.get_config_key())
        return dict(plugins=result)
