""" pynchon.plugins
"""
from pynchon.util import lme, typing
from pynchon.models import Plugin

from .dot import Dot  # noqa
from .git import Git  # noqa
from .base import Base  # noqa
from .fixme import FixMe  # noqa
from .jinja import Jinja  # noqa
from .python import Python, PythonAPI, PythonCLI, PyPI  # noqa
from .project import Project  # noqa
from .scaffolding import Scaffolding  # noqa

# from .jenkins import Jenkins  # noqa

LOGGER = lme.get_logger(__name__)


def get_plugin(plugin_name: str) -> object:
    """ """
    from pynchon.plugins import registry
    try:
        return registry[plugin_name]['kls']
    except KeyError:
        LOGGER.critical(f"cannot find plugin named `{plugin_name}`")
        LOGGER.critical(f"available plugins: {registry.keys()}")
        raise

def get_plugin_obj(plugin_name:str) -> object:
    """ """
    plugin_meta = registry[plugin_name]
    try:
        return plugin_meta['obj']
    except KeyError:
        LOGGER.critical(f"cannot retrieve object for {plugin_name}, is config finalized?")
        raise

registry = [eval(name) for name in dir()]
registry = [kls for kls in registry if typing.is_subclass(kls, Plugin)]
registry = sorted(registry, key=lambda plugin: plugin.priority)
registry = dict([plugin_kls.name, dict(kls=plugin_kls)] for plugin_kls in registry)
# for plugin_name, plugin_meta in registry.items()
# registry[plug]
LOGGER.info(f"prioritized plugin-registry: {registry}")
