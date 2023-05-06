""" pynchon.plugins
"""
from pynchon import fleks, shimport, config, abcs, events  # noqa

from pynchon.util import lme, typing  # noqa
from .util import get_plugin, get_plugin_obj  # noqa

LOGGER = lme.get_logger(__name__)
registry = (
    shimport.wrap(__name__, import_children=True)
    .prune(
        exclude_names='git'.split(),  # FIXME: hack
        types_in=[fleks.Plugin],
        filter_vals=[
            lambda val: val.name in config.PLUGINS,
        ],
    )
    .namespace
).items()
import collections

registry = collections.OrderedDict(sorted(registry, key=lambda x: x[1].priority))
registry = collections.OrderedDict(
    [
        [plugin_kls.name, dict(obj=None, kls=plugin_kls)]
        for k, plugin_kls in registry.items()
    ]
)
registry['core']['obj'] = registry['core']['kls']()
events.lifecycle.send(__name__, msg='Finished creating plugin registry')
