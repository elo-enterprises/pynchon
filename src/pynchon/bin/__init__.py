""" pynchon.bin
"""
from pynchon.app import app
from pynchon.util import lme
from pynchon.plugins import registry as plugin_registry

from pynchon import config  # isort: skip
from .entry import entry  # noqa isort: skip

LOGGER = lme.get_logger(__name__)
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
        if name == 'core':
            raise
    else:
        registry[name] = dict(plugin=plugin_kls, entry=p_entry)
