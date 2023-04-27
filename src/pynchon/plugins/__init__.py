""" pynchon.plugins
"""
# from pynchon import models
# from .jenkins import Jenkins  # noqa
from pynchon import config, models
from pynchon.util import lme, typing

# WARNING: edit src/pynchon/constants.py @ `DEFAULT_PLUGINS`
# from .jenkins import Jenkins  # noqa

from .json import Json  # noqa
from .globals import Globals  # noqa
from .util import get_plugin, get_plugin_obj  # noqa

from .dot import Dot  # noqa
from .git import Git  # noqa
from .base import Base  # noqa

from .fixme import FixMe  # noqa
from .jinja import Jinja  # noqa
from .python import PythonPlatform, PythonAPI, PythonCLI, PyPI  # noqa
from .project import Project  # noqa
from .scaffolding import Scaffolding  # noqa
from .gen import Generators  # noqa
from .render import Renderers  # noqa
from .globals import Globals #
from .files import * # noqa

LOGGER = lme.get_logger(__name__)


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
