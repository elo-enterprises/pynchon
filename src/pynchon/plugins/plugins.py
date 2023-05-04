""" pynchon.plugins.plugins
"""
from pynchon import abcs, models

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class PluginsMan(models.Provider):
    """meta-plugin for managing plugins"""

    name = "plugins"
    cli_name = 'plugins'
    cli_label = 'Meta'

    def new(self) -> None:
        """ Create new plugin from template (for devs)"""

    def status(self) -> typing.Dict:
        """ Returns details about all known plugins """
        result = typing.OrderedDict()
        for p in self.active_plugins:
            result[p.name] = dict(priority=p.priority, key=p.get_config_key())
        return dict(plugins=result)
