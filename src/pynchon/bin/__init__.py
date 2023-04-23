""" pynchon.bin
"""
from pynchon.bin import api, cli, parse, render  # noqa
from pynchon.util import typing, lme
from pynchon.plugins import registry

LOGGER = lme.get_logger(__name__)

for name, plugin_kls in registry.items():
    LOGGER.critical(f'{name}.init_cli: ')
    fxn = getattr(plugin_kls, 'init_cli', lambda: plugin_kls)
    fxn()

from .entry import entry  # noqa
