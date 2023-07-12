""" pynchon.models.plugins
"""
import typing

import fleks

from pynchon import api, cli, events  # noqa
from pynchon.util import lme, tagging, typing  # noqa

from . import validators  # noqa
from .cli import CliPlugin  # noqa
from .provider import Provider  # noqa
from .pynchon import PynchonPlugin  # noqa
from .tool import ToolPlugin  # noqa

LOGGER = lme.get_logger(__name__)
classproperty = fleks.util.typing.classproperty


class BasePlugin(CliPlugin):
    """The default plugin-type most new plugins will use"""

    priority = 10


@tagging.tags(cli_label="NameSpace")
class NameSpace(CliPlugin):
    """`CliNamespace` collects functionality
    from elsewhere under a single namespace


    """

    cli_label = "NameSpace"
    contribute_plan_apply = False
    priority = 1
