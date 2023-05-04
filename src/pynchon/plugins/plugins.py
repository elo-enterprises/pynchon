""" pynchon.plugins.plugins
"""
from pynchon import abcs, cli, models
from pynchon.util.os import invoke

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class PluginsMan(models.Manager):
    """Meta-plugin for managing plugins"""

    name = "plugins"
    cli_name = 'plugins'

    @cli.click.option('--name')
    def new(self, name) -> None:
        """Create new plugin from template (for devs)"""
        plugins_d = abcs.Path(__file__).parents[0]
        template_plugin_f = plugins_d / '__template__.py'
        new_plugin_file = plugins_d / f'{name}.py'
        cmd = f'ls {new_plugin_file} || cp {template_plugin_f} {new_plugin_file} && git status'
        return invoke(cmd, system=True).succeeded

    def status(self) -> typing.Dict:
        """Returns details about all known plugins"""
        result = typing.OrderedDict()
        for p in self.active_plugins:
            result[p.name] = dict(priority=p.priority, key=p.get_config_key())
        return dict(plugins=result)
