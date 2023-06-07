""" pynchon.models.plugins.provider """
from pynchon import api, cli, events, fleks, shimport  # noqa
from pynchon.util import lme, tagging, typing  # noqa

from . import validators
from .cli import CliPlugin  # noqa

LOGGER = lme.get_logger(__name__)


@tagging.tags(cli_label="Provider")
class Provider(CliPlugin):
    """ProviderPlugin provides context-information,
    but little other functionality


    """

    cli_label = "Provider"
    contribute_plan_apply = False
    priority = 2
    __class_validators__ = [
        validators.require_conf_key,
        # validators.warn_config_kls,
    ]
