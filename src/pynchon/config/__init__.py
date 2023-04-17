""" pynchon.config
"""
import glob
import os
import platform

from memoized_property import memoized_property

from pynchon import __version__, abcs, util
from pynchon.util import lme, python, text, typing
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)
initialized = {}
from .base import BaseConfig as PynchonConfig
from .git import GitConfig
from .jinja import JinjaConfig
from .project import ProjectConfig
from .python import PackageConfig, PyPiConfig, PythonConfig

config_classes = [eval(kls_name) for kls_name in dir()]
config_classes = [
    kls
    for kls in config_classes
    if isinstance(kls, (typing.Type,)) and issubclass(kls, abcs.Config)
]
config_classes = sorted(config_classes, key=lambda kls: kls.priority)
LOGGER.debug(f"config initialization order: {[k.__name__ for k in config_classes]}")
for kls in config_classes:
    parent = getattr(kls, "parent", None)
    if parent is not None:
        kls.logger.warning(f"skipping init because parent is set (parent={parent})")
        continue
    config_defaults = initialized.get("pynchon", {}).get(kls.config_key, {})
    kls_defaults = getattr(kls, "defaults", {})
    # LOGGER.debug(f"defaults loaded from config: {config_defaults}")
    # LOGGER.debug(f"defaults loaded from class: {kls_defaults}")
    final_defaults = {**kls_defaults, **config_defaults}
    if final_defaults:
        msg = text.to_json(final_defaults)
        msg = f"using defaults:\n{msg}"
        kls.logger.debug(msg)
    initialized[kls.config_key] = conf = kls(**final_defaults)
    # conf.logger.debug("initialized.")
for k, v in initialized.items():
    exec(f"{k}=v")
