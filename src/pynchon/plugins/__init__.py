""" pynchon.plugins
"""
# from pynchon import models
from pynchon.util import lme, typing

# from .jenkins import Jenkins  # noqa
from .util import get_plugin, get_plugin_obj  # noqa

from .dot import Dot  # noqa
from .gen import Generators  # noqa
from .git import Git  # noqa
from .base import Base  # noqa

from .fixme import FixMe  # noqa
from .jinja import Jinja  # noqa
from .python import Python, PythonAPI, PythonCLI, PyPI  # noqa
from .project import Project  # noqa
from .scaffolding import Scaffolding  # noqa
from .globals import Globals
# from .jenkins import Jenkins  # noqa

LOGGER = lme.get_logger(__name__)

from pynchon import config

LOGGER.critical("Building plugin registry..")
registry = [
    eval(name)
    for name in dir()
    if not name.startswith('_') and name not in 'git'.split()
]
from pynchon import abcs

registry = [kls for kls in registry if typing.is_subclass(kls, abcs.Plugin)]
registry = [kls for kls in registry if kls.name in config.PLUGINS]
registry = sorted(registry, key=lambda plugin: plugin.priority)
registry = dict([plugin_kls.name, dict(kls=plugin_kls)] for plugin_kls in registry)
# FIXME: why doesn't this happen already?
# registry[Base.name] = dict(kls=Base, obj=Base())
