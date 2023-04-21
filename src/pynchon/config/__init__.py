""" pynchon.config
"""
# from memoized_property import memoized_property

from pynchon import abcs
from pynchon.util import lme, text, typing

LOGGER = lme.get_logger(__name__)
initialized = abcs.AttrDict()
from .git import GitConfig  # noqa
from .base import BaseConfig as PynchonConfig  # noqa
from .jinja import JinjaConfig  # noqa
from .python import PackageConfig, PyPiConfig, PythonConfig  # noqa
from .project import ProjectConfig  # noqa
from frozendict import frozendict

git = initialized['git'] = frozendict(GitConfig())

def config_folders():
    folders = list(set(filter(None,[
        os.environ.get("PYNCHON_ROOT"),
        initialized["git"]["root"]])))
    return [abcs.Path(f) for f in folders]
import pyjson5
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

# toml_path = self.config_folder / "pyproject.toml"
# json5_path = self.config_folder / "pynchon.json5"
# json5_path_hidden = self.config_folder / ".pynchon.json5"
# contents = {}
# for conf in load_config():
#     contents.update(conf)
# contents.update(dict(config_source=self.config_source))
#
# if contents:
#     for k, v in contents.items():
#         self.logger.debug(f"setting `{k}`: {v}")
#         self[k] = v
# else:
#     LOGGER.critical("could not load any configuration!")
import os
from collections import OrderedDict

def config_sources():
    """ """
    if os.environ.get('PYNCHON_CONFIG', None):
        return [abcs.Path(os.environ['PYNCHON_CONFIG'])]
    files = [
        "pynchon.json5",
        ".pynchon.json5",
        "pyproject.toml" ]
    result = []
    for folder in config_folders():
        for file in files:
            result.append(folder/file)
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
for _,config in load_config().items():
    _merged={**_merged,**config}
from pynchon.abcs.visitor import JinjaDict

pynchon = initialized['pynchon'] = PynchonConfig(**_merged)
raw = frozendict(pynchon)
defaults = JinjaDict(raw.copy()).render(dict(pynchon=raw))
jinja = JinjaConfig(**{
        **JinjaConfig.defaults,
        **defaults.get('jinja',{}),
        })

# defaults.pop('p)
# # git = initialized['git'] = frozendict(GitConfig())
# # / = frozendict(raw)
# # jinja = initialized['jinja'] = frozendict(tmp['jinja'])
# for k,v in tmp.items():
#     if k!='pynchon' and not isinstance(v,(str,)):
#         cmd = f"{k} = initialized[k] = tmp[k]"
#         exec(cmd, )
# initialized['for k,v in tmp.items():
#         initialized[k] = v
#
# )
        # exec(f'{k}=initialized["{k}"]=v')
# raise Exception(tmp)
# jinja = initialized['jinja'] = JinjaDict(JinjaConfig(**initialized['pynchon']['jinja'])).render()
# namespace = dict(
#     pychon = raw,
#     jinja
# )
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
#         initialized[kls.config_key] = frozendict(initialized[kls.config_key])
#
#     # conf.logger.debug("initialized.")
# for k in initialized:
#     exec(f"{k} = initialized['{k}']")
# initialized=frozendict(initialized)
# # pynchon = frozendict(initialized['pynchon'])
# from pynchon.abcs.visitor import JinjaDict
# tmp = JinjaDict(**initialized)
# tmp.render()
# tmp['pynchon'] = pynchon
# initialized = tmp
