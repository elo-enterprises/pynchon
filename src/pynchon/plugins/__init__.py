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
        return registry[plugin_name]
    except KeyError:
        LOGGER.critical(f"cannot find plugin named `{plugin_name}`")
        LOGGER.critical(f"available plugins: {registry.keys()}")
        raise

registry = [eval(name) for name in dir()]
registry = [kls for kls in registry if typing.is_subclass(kls, Plugin)]
registry = sorted(registry, key=lambda plugin: plugin.priority)
registry = dict([plugin_kls.name, plugin_kls] for plugin_kls in registry)
LOGGER.info(f"prioritized plugin-registry: {registry}")
