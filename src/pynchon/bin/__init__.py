""" pynchon.bin
"""
import click
from pynchon.util import lme
from pynchon.plugins import registry as plugin_registry

from pynchon import config  # isort: skip

LOGGER = lme.get_logger(__name__)

LOGGER.critical('Building CLIs from plugins..')
registry = cli_registry = {}

# with click.progressbar(plugin_registry.items()) as bar:
loop = plugin_registry.items()
# loop = tqdm(loop)
for name, plugin_meta in loop:
    # loop.set_description(f'plugin {name}')
    # loop.refresh()
    if name not in config.PLUGINS:
        # LOGGER.warning(f"skipping `{name}`")
        continue
    plugin_kls = plugin_meta['kls']
    # LOGGER.critical(f'{name}.init_cli: ')
    init_fxn = getattr(plugin_kls, 'init_cli', lambda _kls: None)
    try:
        p_entry = init_fxn(plugin_kls)
    except (Exception,) as exc:
        LOGGER.critical(f"failed to initialize cli for {plugin_kls}")
        raise
    registry[name] = dict(plugin=plugin_kls, entry=p_entry)

# LOGGER.info(f'cli_registry: {cli_registry}')
from .entry import entry  # noqa
