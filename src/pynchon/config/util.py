""" pynchon.config.util
"""
import functools
import collections
from types import MappingProxyType

from pynchon import constants, abcs, events
from pynchon import config as config_module
from pynchon.util import typing, lme
from pynchon.util.text import loadf, loads
from pynchon.plugins.util import PluginNotRegistered, get_plugin

LOGGER = lme.get_logger(__name__)


@functools.lru_cache(maxsize=100, typed=False)
def finalize():
    """ """
    result = abcs.AttrDict(
        pynchon=MappingProxyType(
            dict(
                [
                    [k, v]
                    for k, v in config_module.RAW.items()
                    if not isinstance(v, (dict,))
                ]
            )
        ),
        git=config_module.GIT,
    )
    plugins = []

    pnames = result.pynchon['plugins']
    for pname in pnames:
        try:
            tmp = get_plugin(pname)
        except (PluginNotRegistered,) as exc:
            LOGGER.critical(f"PluginNotRegistered: {exc}")
            continue
        else:
            plugins.append(tmp)

    for plugin_kls in plugins:
        pconf_kls = getattr(plugin_kls, 'config_class', None)
        conf_key = plugin_kls.get_config_key()
        if pconf_kls is None:
            plugin_config = abcs.Config()
        else:
            user_defaults = (
                config_module.PYNCHON_CORE
                if plugin_kls.name == 'base'
                else config_module.USER_DEFAULTS.get(plugin_kls.name, {})
            )
            plugin_config = pconf_kls(
                **{
                    # **plugin_defaults,
                    **user_defaults,
                }
            )
        setattr(config_module, conf_key, plugin_config)
        result.update({conf_key: plugin_config})

        plugin_obj = plugin_kls(final=plugin_config)
        from pynchon.plugins import registry as plugins_registry

        # plugins_registry.register(plugin_obj)
        plugins_registry[plugin_kls.name]['obj'] = plugin_obj
        events.lifecycle.send(plugin_obj, plugin=f'finalized {plugin_kls.__name__}')
    return result


def get_config_files():
    """ """
    if constants.PYNCHON_CONFIG:
        return [abcs.Path(constants.PYNCHON_CONFIG)]
    result = []
    for folder in config_folders():
        for file in constants.CONF_FILE_SEARCH_ORDER:
            result.append(folder / file)
    # FIXME: handle overrides from subproject
    # subproject = project['subproject']
    # subproject_root = subproject and subproject['root']
    # if subproject_root:
    #     config_candidates += [
    #         subproject_root / "pynchon.json5",
    #         subproject_root / ".pynchon.json5",
    #         subproject_root / "pyproject.toml",
    #     ]
    # config_candidates = [p for p in config_candidates if p.exists()]
    return result


def config_folders():
    from pynchon import config

    folders = list(set(filter(None, [constants.PYNCHON_ROOT, config.GIT["root"]])))
    return [abcs.Path(f) for f in folders]


def load_config_from_files() -> typing.Dict[str, str]:
    """ """
    contents = collections.OrderedDict()
    for config_file in get_config_files():
        if not config_file.exists():
            LOGGER.warning(f"config_file@`{config_file}` doesn't exist, skipping it")
            continue
        elif config_file.name.endswith('pyproject.toml'):
            LOGGER.info(f"Loading from toml: {config_file}")
            tmp = loadf.toml(config_file)
            tmp = tmp.get("tool", {})
            tmp = tmp.get("pynchon", {})
            contents[config_file] = tmp
        elif config_file.name.endswith('.json5'):
            LOGGER.info(f"Loading from json5: {config_file}")
            with open(config_file.absolute(), "r") as fhandle:
                contents[config_file] = loads.json5(fhandle.read())
        else:
            err = f"don't know how to load config from {config_file}"
            raise NotImplementedError(err)
    return contents
