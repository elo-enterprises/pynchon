""" pynchon.bin
"""
import click
from pynchon.util import lme
from pynchon.plugins import registry as plugin_registry
from pynchon.events import status
from pynchon import config  # isort: skip

LOGGER = lme.get_logger(__name__)

msg='Building CLIs from plugins..'
status.update(stage=msg)
LOGGER.critical(msg)
registry = cli_registry = {}
loop = plugin_registry.items()
for name, plugin_meta in loop:
    if name not in config.PLUGINS:
        LOGGER.warning(f"skipping `{name}`")
        continue
    plugin_kls = plugin_meta['kls']
    init_fxn = plugin_kls.init_cli
    LOGGER.critical(f'\t{name}.init_cli: {init_fxn}')
    try:
        p_entry = init_fxn()
    except (Exception,) as exc:
        LOGGER.critical(f"failed to initialize cli for {plugin_kls}")
        raise
    registry[name] = dict(plugin=plugin_kls, entry=p_entry)

# LOGGER.info(f'cli_registry: {cli_registry}')
from .entry import entry  # noqa
