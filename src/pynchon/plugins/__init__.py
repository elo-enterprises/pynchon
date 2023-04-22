""" pynchon.plugins
"""
from pynchon.util import lme, typing
from pynchon.abcs.plugin import Plugin

from .dot import Dot  # noqa
from .git import Git  # noqa
from .fixme import FixMe  # noqa
from .jinja import Jinja  # noqa
from .python import PythonAPI, PythonCLI, PyPI  # noqa
from .project import Project  # noqa
from .scaffolding import Scaffolding  # noqa

LOGGER = lme.get_logger(__name__)

registry = [eval(name) for name in dir()]
registry = [kls for kls in registry if typing.is_subclass(kls, Plugin)]
registry = sorted(registry, key=lambda plugin: plugin.priority)
registry = dict([plugin.name, plugin] for plugin in registry)
LOGGER.info(f"prioritized plugin-registry: {registry}")
