""" pynchon.config
"""
import os
from types import MappingProxyType
from collections import OrderedDict

import pyjson5

from pynchon import abcs
from pynchon.util import lme

# from memoized_property import memoized_property


LOGGER = lme.get_logger(__name__)
initialized = abcs.AttrDict()

from pynchon.plugins.git import GitConfig  # noqa

from .base import BaseConfig as PynchonConfig  # noqa

git = initialized['git'] = MappingProxyType(GitConfig())


def config_folders():
    folders = list(set(filter(None, [os.environ.get("PYNCHON_ROOT"), git["root"]])))
    return [abcs.Path(f) for f in folders]


def load_config():
    """ """
    from pynchon.util import python

    contents = OrderedDict()
    for src in config_sources():
        if not src.exists():
            LOGGER.warning("src@`{src}` doesn't exist")
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


def config_sources():
    """ """
    if os.environ.get('PYNCHON_CONFIG', None):
        return [abcs.Path(os.environ['PYNCHON_CONFIG'])]
    files = ["pynchon.json5", ".pynchon.json5", "pyproject.toml"]
    result = []
    for folder in config_folders():
        for file in files:
            result.append(folder / file)
    # FIXME: handle sub
    # subproject = initialized['project']['subproject']
    # subproject_root = subproject and subproject['root']
    # if subproject_root:
    #     config_candidates += [
    #         subproject_root / "pynchon.json5",
    #         subproject_root / ".pynchon.json5",
    #         subproject_root / "pyproject.toml",
    #     ]
    # config_candidates = [p for p in config_candidates if p.exists()]
    return result


_merged = {}
for _, config in load_config().items():
    _merged = {**_merged, **config}

pynchon = PynchonConfig(**_merged)
assert '{{' in pynchon['jinja']['includes'][0]
# import IPython; IPython.embed()

raw = initialized['pynchon'] = pynchon
pynchon['plugins'] = pynchon.plugins

from pynchon.abcs.visitor import JinjaDict

defaults = JinjaDict(raw.copy()).render(dict(pynchon=raw))

# from pynchon.plugins import registry
# for name,plugin_kls in registry:
# config_classes = [eval(kls_name) for kls_name in dir()]
# config_classes = [
#     kls
#     for kls in config_classes
#     if isinstance(kls, (typing.Type,)) and issubclass(kls, abcs.Config)
# ]
# config_classes = sorted(config_classes, key=lambda kls: kls.priority)
# LOGGER.debug(f"config initialization order: {[k.__name__ for k in config_classes]}")
# for kls in config_classes:
#     parent = getattr(kls, "parent", None)
#     if parent is not None:
#         kls.logger.warning(f"skipping init because parent is set (parent={parent})")
#         continue
#     raw_defaults = initialized.get("pynchon", {}).get(kls.config_key, {})
#     kls_defaults = getattr(kls, "defaults", {})
#     # LOGGER.debug(f"defaults loaded from config: {raw_defaults}")
#     # LOGGER.debug(f"defaults loaded from class: {kls_defaults}")
#     final_defaults = {**kls_defaults, **raw_defaults}
#     if final_defaults and kls.debug:
#         msg = text.to_json(final_defaults)
#         msg = f"using defaults:\n{msg}"
#         kls.logger.info(msg)
#     # conf = kls(**final_defaults)
#     initialized[kls.config_key] = kls(**final_defaults)
#     if kls.config_key=='pynchon':
#         LOGGER.critical('freezing pynchon')
#         initialized[kls.config_key] = dict(initialized[kls.config_key])
#
#     # conf.logger.debug("initialized.")
# for k in initialized:
#     exec(f"{k} = initialized['{k}']")
# initialized=dict(initialized)
# # pynchon = dict(initialized['pynchon'])
# from pynchon.abcs.visitor import JinjaDict
# tmp = JinjaDict(**initialized)
# tmp.render()
# tmp['pynchon'] = pynchon
# initialized = tmp
