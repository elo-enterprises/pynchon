""" pynchon.config
"""
import time

from pynchon import abcs
from pynchon.util import lme  # typing
from pynchon.bin.common import status
from pynchon.abcs.plugin import Meta
from pynchon.abcs.visitor import JinjaDict
from pynchon.plugins.base.config import BaseConfig

from .util import config_folders  # noqa
from .util import load_config_from_files  # noqa
from .util import get_config_files  # noqa
from .util import finalize  # noqa

from pynchon.plugins.git import GitConfig  # noqa

LOGGER = lme.get_logger(__name__)

msg = "Loading raw-config from OS.."
LOGGER.critical(msg)
status.update(stage=msg)

git = GIT = GitConfig()
msg = "Building raw-config from files.."
LOGGER.critical(msg)
status.update(stage=msg)

CONFIG_FILES = []
MERGED_CONFIG_FILES = {}
for cfg_src, config in load_config_from_files().items():
    MERGED_CONFIG_FILES = {**MERGED_CONFIG_FILES, **config}
    config and CONFIG_FILES.append(cfg_src)

# NB: this content is potentially templated
msg = "Building plugins-list.."
LOGGER.critical(msg)
status.update(stage=msg)

pynchon = PYNCHON = BaseConfig(config_files=CONFIG_FILES, **MERGED_CONFIG_FILES)
RAW = PYNCHON.copy()
PLUGINS = PYNCHON['plugins'] = list(
    set(PYNCHON['plugins'] + PYNCHON.plugins + ['base'])
)

_all_names = PLUGINS + Meta.NAMES

msg = "Splitting core config.."
LOGGER.critical(msg)
status.update(stage=msg)

PYNCHON_CORE = dict([[x, PYNCHON[x]] for x in PYNCHON if x not in _all_names])
PYNCHON_CORE = BaseConfig(**PYNCHON_CORE)

msg = "Interpolating config.."
LOGGER.critical(msg)
status.update(stage=msg)

USER_DEFAULTS = JinjaDict(RAW.copy()).render(dict(pynchon=RAW))
