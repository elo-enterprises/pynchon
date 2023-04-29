""" pynchon.plugins
"""
# from pynchon import models
# from .jenkins import Jenkins  # noqa
from pynchon import config, abcs
from pynchon.app import events
from pynchon.util import lme, typing
from pynchon.util.importing import module_builder

from .util import get_plugin, get_plugin_obj  # noqa

LOGGER = lme.get_logger(__name__)

mregistry = module_builder(
    __name__,
    import_children=True,
    name_validators=[
        lambda n: not n.startswith('_'),
        lambda n: n not in 'git'.split(),
    ],
    val_validators=[
        lambda val: typing.is_subclass(val, abcs.Plugin),
        lambda val: val.name in config.PLUGINS,
    ],
)
mregistry.initialize(
    events=events,
)


def build_plugin_registry():
    registry = mregistry.namespace.values()
    registry = sorted(registry, key=lambda plugin: plugin.priority)
    registry = dict([plugin_kls.name, dict(kls=plugin_kls)] for plugin_kls in registry)
    return registry


registry = build_plugin_registry()
