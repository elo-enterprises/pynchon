""" pynchon.api.project
"""
from frozendict import frozendict
from pynchon import abcs, config
from pynchon.util import lme, text, typing

LOGGER = lme.get_logger(__name__)
def get_plugin(plugin_name:str) ->object:
    from pynchon.plugins import registry
    return registry[plugin_name]

def get_config() -> dict:
    """ """
    result = abcs.AttrDict(
        _=config.raw,
        pynchon=frozendict([[k,v] for k,v in config.raw.items() if not isinstance(v,dict)]),
        git=config.git,
        )
    plugins  = [get_plugin(p) for p in result.pynchon['plugins']]
    for plugin_kls in plugins:
        LOGGER.debug(f"plugin {plugin_kls.name}: {plugin_kls}")
        LOGGER.debug(f"config {plugin_kls.name}: {plugin_kls.config}")
        pconf_kls = plugin_kls.config
        plugin_defaults = plugin_kls.defaults
        #NB: module access 
        user_defaults = config.defaults.get(plugin_kls.name, {})
        plugin_config = pconf_kls(**{
                **plugin_defaults,
                **user_defaults,
                })
        result.update({plugin_kls.name:plugin_config})
# pypi = PyPiConfig

        # result.update(
        #     pypi=config.pypi,
        #     jinja=config.jinja,
        # )
    # for k in dir(config):
    #     val = getattr(config, k)
    #     if isinstance(val, (abcs.Config, frozendict)):
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
        plugin = registry[plugin_name]
        # plugin.logger.debug(f"Planning..")
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
