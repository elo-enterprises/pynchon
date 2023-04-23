""" pynchon.bin
"""
from pynchon.bin import api, cli, parse, render  # noqa
from pynchon.util import typing, lme
from pynchon.plugins import registry

LOGGER = lme.get_logger(__name__)

for name, plugin_kls in registry.items():
    LOGGER.critical(f'{name}.init_cli: ')
    init_fxn = getattr(
        plugin_kls,
        'init_cli',
        None)
    if init_fxn is not None:
        init_fxn(plugin_kls)

from .entry import entry  # noqa
