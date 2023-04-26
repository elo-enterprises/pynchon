""" pynchon.api.project
"""
from pynchon import config
from pynchon.util import lme, text, typing

LOGGER = lme.get_logger(__name__)


def get_config() -> dict:
    """ """
    from pynchon.config import finalize

    return finalize()


def plan(config: dict = {}) -> dict:
    """ """
    plan = []
    config = config or get_config()
    project = config.project
    from pynchon.plugins import registry

    for plugin_name in config.pynchon["plugins"]:
        assert plugin_name in registry, f"missing required plugin @ {plugin_name}"
        plugin_kls = registry[plugin_name]['kls']
        plugin = plugin_kls()
        plugin.logger.debug("Planning..")
        result = plugin.plan(config)
        msg = "Done planning.  "
        if result:
            msg = msg + "result={}"
            plugin.logger.debug(msg.format(text.to_json(result)))
        else:
            plugin.logger.critical(msg + "But plugin produced an empty plan!")
        assert isinstance(
            result, typing.List
        ), f"plugin @ {plugin_name} generates bad plan {result}"
        plan += result

    return config, plan
