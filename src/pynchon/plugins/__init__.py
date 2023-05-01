""" pynchon.plugins
"""
import blinker

# from .jenkins import Jenkins  # noqa
from pynchon import shimport, config, abcs

# from pynchon.app import app

from pynchon.util import lme, typing  # noqa

from .util import get_plugin, get_plugin_obj  # noqa

events = blinker.signal(f'lifecycle-{__name__}')
LOGGER = lme.get_logger(__name__)
registry = (
    shimport.wrap(__name__, import_children=True)
    .prune(
        exclude_names='git'.split(),  # FIXME: hack
        types_in=[abcs.Plugin],
        filter_vals=[
            lambda val: val.name in config.PLUGINS,
        ],
        rekey=lambda plugin_kls: [plugin_kls.name, dict(obj=None, kls=plugin_kls)],
    )
    .namespace
)  # .assign_back()

# import IPython; IPython.embed()
# registry.assign_back()
#     assign_objects=True,
#     init_hooks=[lambda msg: [app.events.lifecycle.send(msg=msg, stage=msg)]],
#
#     # return_objects=True,
#     # sort_objects=dict(
#     #     key=lambda plugin: plugin.priority,
#     # ),
# ).filter(
# )
