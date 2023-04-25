""" pynchon.bin
"""
from pynchon.bin import api, cli, parse, render  # noqa
from pynchon.util import lme
from pynchon.plugins import registry as plugin_registry

LOGGER = lme.get_logger(__name__)
from pynchon import config

LOGGER.critical('Building CLIs from plugins..')
registry = cli_registry = {}
for name, plugin_meta in plugin_registry.items():
    if name not in config.PLUGINS:
        LOGGER.debug(f"skipping `{name}`")
        continue
    plugin_kls = plugin_meta['kls']
    # LOGGER.critical(f'{name}.init_cli: ')
    init_fxn = getattr(plugin_kls, 'init_cli', None)
    if init_fxn is not None:
        registry[name] = dict(plugin=plugin_kls, entry=init_fxn(plugin_kls))
# LOGGER.info(f'cli_registry: {cli_registry}')
from .entry import entry  # noqa
