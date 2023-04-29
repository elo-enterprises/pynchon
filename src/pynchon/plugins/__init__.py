""" pynchon.plugins
"""
# from .jenkins import Jenkins  # noqa
from pynchon import config, abcs
from pynchon.app import events
from pynchon.util import lme, typing, importing

from .util import get_plugin, get_plugin_obj  # noqa

LOGGER = lme.get_logger(__name__)

registry = importing.registry_builder(
    __name__,

    # kwargs for reg-builder
    itemizer = lambda plugin_kls: [plugin_kls.name, dict(obj=None, kls=plugin_kls)],
    # kwargs for mod-builder
    return_objects=True,
    assign_objects=True,
    sort_objects=dict(
        key=lambda plugin: plugin.priority,
    ),
    import_children=True,
    exclude_names='git'.split(),  # FIXME: hack
    init_hooks=[
        lambda msg: [LOGGER.critical(msg), events.status.update(stage=msg)]
    ],
    filter_types=[abcs.Plugin],
    fitler_vals=[
        lambda val: val.name in config.PLUGINS,
    ],
)
