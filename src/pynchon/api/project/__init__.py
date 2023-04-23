""" pynchon.api.project
"""
from pynchon import abcs, config
from pynchon.util import lme, text, typing

LOGGER = lme.get_logger(__name__)
from types import MappingProxyType


def get_plugin(plugin_name: str) -> object:
    from pynchon.plugins import registry

    try:
        return registry[plugin_name]
    except KeyError:
        LOGGER.critical(f"cannot find plugin named `{plugin_name}`")
        LOGGER.critical(f"available plugins: {registry.keys()}")
        raise


def get_config() -> dict:
    """ """
    result = abcs.AttrDict(
        _=config.raw,
        pynchon=MappingProxyType(
            dict([[k, v] for k, v in config.raw.items() if not isinstance(v, (dict,))])
        ),
        git=config.git,
    )
    plugins = [get_plugin(p) for p in result.pynchon['plugins']]
    for plugin_kls in plugins:
        if plugin_kls.name in 'git pynchon'.split():
            pass
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
        setattr(config, plugin_kls.name.replace('-', '_'), plugin_config)
        result.update({plugin_kls.name: plugin_config})
        exec(f"{plugin_kls.name.replace('-','_')}=plugin_config")
    # pypi = PyPiConfig

    # result.update(
    #     pypi=config.pypi,
    #     jinja=config.jinja,
    # )
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
        plugin_kls = registry[plugin_name]
        plugin = plugin_kls()
        plugin.logger.debug(f"Planning..")
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
