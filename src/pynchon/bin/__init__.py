""" pynchon.bin
"""
from pynchon.bin import api, cli, parse, render  # noqa
from pynchon.util import typing, lme
from pynchon.plugins import registry as plugin_registry

LOGGER = lme.get_logger(__name__)

LOGGER.critical('creating cli registry')
registry = cli_registry = {}
for name, plugin_kls in plugin_registry.items():
    LOGGER.critical(f'{name}.init_cli: ')
    init_fxn = getattr(plugin_kls, 'init_cli', None)
    if init_fxn is not None:
        registry[name] = dict(
            plugin=plugin_kls,
            entry=init_fxn(plugin_kls))
LOGGER.debug(f'cli_registry: {cli_registry}')
from .entry import entry  # noqa
