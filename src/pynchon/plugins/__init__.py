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

registry = dict(
    [plugin_kls.name, dict(obj=None, kls=plugin_kls)]
    for plugin_kls in sorted(
        module_builder(
            __name__,
            events=events,
            return_objects=True,
            import_children=True,
            # assign_objects= True,
            # return_namespace=False
            # return_module=False
            # filter_failure_raises=True
            # name_filters=[
            # val_filters=[
            # filter_subclass=..
            # file_filters=[
            # mod_filters=[
            name_validators=[
                lambda n: not n.startswith('_'),
                lambda n: n not in 'git'.split(),
            ],
            val_validators=[
                lambda val: typing.is_subclass(val, abcs.Plugin),
                lambda val: val.name in config.PLUGINS,
            ],
            # sort_objects=dict(key=lambda plugin: plugin.priority,)
        ),
        key=lambda plugin: plugin.priority,
    )
)
