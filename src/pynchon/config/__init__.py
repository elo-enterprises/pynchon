""" pynchon.config
"""
import os
import functools

from pynchon import abcs
from pynchon.util import lme, typing
from pynchon.plugins.git import GitConfig  # noqa
from pynchon.abcs.visitor import JinjaDict
from pynchon.plugins.base.config import BaseConfig as PynchonConfig  # noqa

from .util import config_folders, load_config_from_files, get_config_files, finalize

LOGGER = lme.get_logger(__name__)

git = GIT = abcs.MappingProxyType(GitConfig())

CONFIG_FILES = []
MERGED_CONFIG_FILES = {}
for cfg_src, config in load_config_from_files().items():
    MERGED_CONFIG_FILES = {**MERGED_CONFIG_FILES, **config}
    config and CONFIG_FILES.append(cfg_src)

LOGGER.critical("Building plugins-list & raw-config..")

# NB: this content is potentially templated
pynchon = PYNCHON = PynchonConfig(config_files=CONFIG_FILES,**MERGED_CONFIG_FILES)
RAW = PYNCHON.copy()
PLUGINS = PYNCHON['plugins'] = list(set(PYNCHON.plugins + ['base']))

USER_DEFAULTS = JinjaDict(RAW.copy()).render(dict(pynchon=RAW))
