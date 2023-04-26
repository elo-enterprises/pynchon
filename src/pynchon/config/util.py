"""
"""
import os
import functools
from types import MappingProxyType
from collections import OrderedDict

import pyjson5

from pynchon import abcs
from pynchon.util import lme

LOGGER = lme.get_logger(__name__)


@functools.lru_cache(maxsize=100, typed=False)
def finalize():
    from pynchon import config
    from pynchon.plugins import get_plugin

    result = abcs.AttrDict(
        pynchon=MappingProxyType(
            dict([[k, v] for k, v in config.RAW.items() if not isinstance(v, (dict,))])
        ),
        git=config.GIT,
    )
    plugins = [get_plugin(pname) for pname in result.pynchon['plugins']]
    # raise Exception(plugins)
    for plugin_kls in plugins:
        pconf_kls = plugin_kls.config_kls
        plugin_defaults = plugin_kls.defaults
        # NB: module access
        user_defaults = config.USER_DEFAULTS.get(plugin_kls.name, {})
        plugin_config = pconf_kls(
            **{
                **plugin_defaults,
                **user_defaults,
            }
        )
        conf_key = getattr(
            plugin_kls.config_kls, 'config_key', plugin_kls.name.replace('-', '_')
        )
        from pynchon import config as THIS_MODULE

        setattr(THIS_MODULE, conf_key, plugin_config)
        result.update({conf_key: plugin_config})
        # plugin_obj = plugin_kls(plugin_config)
        plugin_obj = plugin_kls(final=plugin_config)
        from pynchon.plugins import registry as plugins_registry

        plugins_registry[plugin_kls.name]['obj'] = plugin_obj
    return result


def get_config_files():
    """ """

    if os.environ.get('PYNCHON_CONFIG', None):
        return [abcs.Path(os.environ['PYNCHON_CONFIG'])]
    files = ["pynchon.json5", ".pynchon.json5", "pyproject.toml"]
    result = []
    for folder in config_folders():
        for file in files:
            result.append(folder / file)
    # FIXME: handle sub
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

    folders = list(
        set(filter(None, [os.environ.get("PYNCHON_ROOT"), config.GIT["root"]]))
    )
    return [abcs.Path(f) for f in folders]


def load_config_from_files():
    """ """
    from pynchon.util import python

    contents = OrderedDict()
    for src in get_config_files():
        if not src.exists():
            LOGGER.warning(f"src@`{src}` doesn't exist, skipping it")
            continue
        if src.name.endswith('pyproject.toml'):
            LOGGER.debug(f"Loading from toml: {src}")
            tmp = python.load_pyprojecttoml(path=src)
            tmp = tmp.get("tool", {}).get("pynchon", {})
            contents[src] = tmp
        elif src.name.endswith('.json5'):
            LOGGER.debug(f"Loading from json5: {src}")
            with open(src.absolute(), "r") as fhandle:
                # contents.append()
                contents[src] = pyjson5.loads(fhandle.read())
    return contents
