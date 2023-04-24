""" pynchon.api.project
"""
from pynchon import abcs, config
from pynchon.util import lme, text, typing

LOGGER = lme.get_logger(__name__)
from types import MappingProxyType


def get_config() -> dict:
    """ """
    from pynchon.plugins import get_plugin

    result = abcs.AttrDict(
        _=config.raw,
        pynchon=MappingProxyType(
            dict([[k, v] for k, v in config.raw.items() if not isinstance(v, (dict,))])
        ),
        git=config.git,
    )
    plugins = [get_plugin(pname) for pname in result.pynchon['plugins']]
    for plugin_kls in plugins:
        # if plugin_kls.name in 'git pynchon'.split():
        #     pass
        LOGGER.debug(f"plugin {plugin_kls.name}: {plugin_kls}")
        LOGGER.debug(f"config {plugin_kls.name}: {plugin_kls.config_kls}")
        pconf_kls = plugin_kls.config_kls
        plugin_defaults = plugin_kls.defaults
        # NB: module access
        user_defaults = config.defaults.get(plugin_kls.name, {})
        plugin_config = pconf_kls(
            **{
                **plugin_defaults,
                **user_defaults,
            }
        )
        conf_key = getattr(
            plugin_kls.config_kls, 'config_key', plugin_kls.name.replace('-', '_')
        )
        setattr(config, conf_key, plugin_config)
        result.update({conf_key: plugin_config})
        # exec(f"{conf_key}=plugin_config")
        plugin_obj = plugin_kls(plugin_config)
        from pynchon.plugins import registry as plugins_registry

        plugins_registry[plugin_kls.name]['obj'] = plugin_obj
    # for k in dir(config):
    #     val = getattr(config, k)
    #     if isinstance(val, (abcs.Config, dict)):
    #         result[k]=getattr(config, k)
    return result


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
