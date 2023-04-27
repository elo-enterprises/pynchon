""" pynchon.config
"""
import os
import functools

from pynchon import abcs
from pynchon.util import lme, typing
from pynchon.abcs.visitor import JinjaDict

from .util import config_folders, load_config_from_files, get_config_files, finalize

from pynchon.plugins.git import GitConfig  # noqa
from pynchon.plugins.base.config import BaseConfig


LOGGER = lme.get_logger(__name__)

LOGGER.critical("Loading raw-config from OS..")
git = GIT = abcs.MappingProxyType(GitConfig())

LOGGER.critical("Building raw-config from files..")
CONFIG_FILES = []
MERGED_CONFIG_FILES = {}
for cfg_src, config in load_config_from_files().items():
    MERGED_CONFIG_FILES = {**MERGED_CONFIG_FILES, **config}
    config and CONFIG_FILES.append(cfg_src)

# NB: this content is potentially templated
LOGGER.critical("Building plugins-list..")
pynchon = PYNCHON = BaseConfig(
    config_files=CONFIG_FILES,
    **MERGED_CONFIG_FILES)
RAW = PYNCHON.copy()
PLUGINS = PYNCHON['plugins'] = list(set(
    PYNCHON['plugins']
    + PYNCHON.plugins
    + ['base']))
from pynchon.abcs.plugin import Meta
_all_names = PLUGINS+Meta.NAMES

LOGGER.critical("Splitting core config..")
PYNCHON_CORE = dict([[x,PYNCHON[x]] for x in PYNCHON if x not in _all_names])
PYNCHON_CORE = BaseConfig(**PYNCHON_CORE)

LOGGER.critical("Interpolating config..")
USER_DEFAULTS = JinjaDict(RAW.copy()).render(dict(pynchon=RAW))
