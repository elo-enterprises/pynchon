""" pynchon.config
"""
# from pynchon import abcs
from pynchon.api import render
from pynchon.app import app
from pynchon.core import Config as CoreConfig
from pynchon.util import lme  # typing
from pynchon.abcs.plugin import Meta

from .util import config_folders  # noqa
from .util import load_config_from_files  # noqa
from .util import get_config_files  # noqa
from .util import finalize  # noqa
from pynchon.plugins.git import GitConfig  # noqa

LOGGER = lme.get_logger(__name__)
events = app.events

# FIXME: abstract into phases inside pynchon.app
msg = "Loading raw-config from OS.."
# LOGGER.critical(msg)
events.lifecycle.send(__name__, stage=msg)
git = GIT = GitConfig()

msg = "Building raw-config from files.."
# LOGGER.critical(msg)
events.lifecycle.send(
    __name__,
    msg=msg,
    stage=msg,
)

CONFIG_FILES = []
MERGED_CONFIG_FILES = {}
for cfg_src, config in load_config_from_files().items():
    MERGED_CONFIG_FILES = {**MERGED_CONFIG_FILES, **config}
    config and CONFIG_FILES.append(cfg_src)

# NB: this content is potentially templated
msg = "Building plugins-list.."
events.lifecycle.send(
    __name__,
    msg=msg,
    stage=msg,
)

pynchon = PYNCHON = CoreConfig(config_files=CONFIG_FILES, **MERGED_CONFIG_FILES)
RAW = PYNCHON.copy()
PLUGINS = PYNCHON['plugins'] = list(
    set(PYNCHON['plugins'] + PYNCHON.plugins + ['core'])
)

# FIXME: get from registry
_all_names = PLUGINS + Meta.NAMES

msg = "Splitting core config.."
events.lifecycle.send(
    __name__,
    msg=msg,
    stage=msg,
)
PYNCHON_CORE = dict([[x, PYNCHON[x]] for x in PYNCHON if x not in _all_names])
PYNCHON_CORE = CoreConfig(**PYNCHON_CORE)

msg = "Interpolating config.."
events.lifecycle.send(
    __name__,
    msg=msg,
    stage=msg,
)

USER_DEFAULTS = render.dictionary(input=RAW.copy(), context=dict(pynchon=RAW))
