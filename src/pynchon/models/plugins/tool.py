""" pynchon.models.plugins.tool """
from pynchon import api, cli, events, fleks  # noqa
from pynchon.util import lme, tagging, typing  # noqa

from .cli import CliPlugin  # noqa

LOGGER = lme.get_logger(__name__)


@tagging.tags(cli_label="Tool")
class ToolPlugin(CliPlugin):
    """
    Tool plugins may have their own config,
    but generally should not need project-config.
    """

    cli_label = "Tool"
    contribute_plan_apply = False
    __class_validators__ = [
        # validators.require_conf_key,
        # validators.warn_config_kls,
    ]
