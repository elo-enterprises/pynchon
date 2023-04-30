""" pynchon.plugins.util
"""
from pynchon.util import lme, typing  # noqa

# , importing

# from .exceptions import * # noqa
LOGGER = lme.get_logger(__name__)

# importing.module_builder(__name__, ...)
class PluginNotInitialized(RuntimeError):
    pass


class PluginNotRegistered(RuntimeError):
    pass


class PluginNotConfigured(RuntimeError):
    pass


def get_plugin_meta(plugin_name: str) -> typing.Dict:
    from pynchon.plugins import registry

    try:
        return registry[plugin_name]
    except KeyError:
        # LOGGER.critical(f"available plugins: {registry.keys()}")
        raise PluginNotRegistered(plugin_name)


def get_plugin_class(plugin_name: str) -> typing.Type:
    """ """
    meta = get_plugin_meta(plugin_name)
    try:
        return meta['kls']
    except KeyError:
        raise PluginNotRegistered(plugin_name)


get_plugin = get_plugin_class


def get_plugin_obj(plugin_name: str) -> object:
    """ """
    meta = get_plugin_meta(plugin_name)
    try:
        return meta['obj']
    except KeyError:
        # LOGGER.critical(
        #     f"cannot retrieve ['obj'] for `{plugin_name}` from registry; is config finalized?"
        # )
        # import IPython; IPython.embed()
        raise PluginNotInitialized(plugin_name)
