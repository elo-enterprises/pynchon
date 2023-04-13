""" pynchon.api.python
"""
import ast
import glob
import os
import platform
import subprocess
import sys
from collections import OrderedDict

import griffe
import mccabe
import termcolor
import tomli as tomllib  # tomllib only available in py3.11

import pynchon
from pynchon import constants
from pynchon.util import lme

LOGGER = lme.get_logger(__name__)
from pynchon import annotate, util


def is_package() -> bool:
    """ """
    from pynchon.config import python

    return python.is_package


def load_setupcfg(path: str = ""):
    import configparser

    from pynchon.api import git

    path = path or os.path.join(util.get_root(), "setup.cfg")
    parser = configparser.ConfigParser()
    parser.read(path)
    out = dict()
    for sect in parser.sections():
        # print("Section:", sect)
        out[sect] = dict(parser.items(sect))
    return out


def load_pyprojecttoml(path: str = ""):
    """ """
    from pynchon.api import git

    path = (path or util.get_root()).joinpath(constants.PYNCHON_CONFIG_FILE)
    if not os.path.exists(path):
        err = f"Cannot load config from nonexistent path @ `{path}`"
        LOGGER.critical(err)
        return None, {}
        # raise RuntimeError(err)
    import tomli

    with open(path, "rb") as f:
        try:
            config = tomllib.load(f)
        except (tomli.TOMLDecodeError,) as exc:
            LOGGER.critical(f"cannot decode data from toml @ {f}")
            raise
    # config = {s: dict(config.items(s)) for s in config.sections()}
    pynchon_section = config.get("pynchon", {})
    # pynchon_section['project'] = dict(x.split('=') for x in pynchon_section.get(
    #     'project', '').split('\n') if x.strip())
    # config['tool:pynchon'] = pynchon_section
    return path, config


def load_entrypoints(config=None) -> dict:
    """ """
    if not config:
        LOGGER.critical("no config provided!")
        return {}
    try:
        console_scripts = config["options.entry_points"]["console_scripts"]
    except (KeyError,) as exc:
        LOGGER.critical(
            f'could not load config["options.entry_points"]["console_scripts"] from {config}'
        )
        return {}
    console_scripts = [x for x in console_scripts.split("\n") if x]
    package = config["metadata"]["name"]
    entrypoints = []
    for c in console_scripts:
        tmp = dict(
            package=package,
            bin_name=c.split("=")[0].strip(),
            module=c.split("=")[1].strip().split(":")[0],
            entrypoint=c.split("=")[1].strip().split(":")[1],
        )
        abs_entrypoint = tmp["module"] + ":" + tmp["entrypoint"]
        tmp["setuptools_entrypoint"] = abs_entrypoint
        entrypoints.append(tmp)
    return dict(
        package=package,
        entrypoints=entrypoints,
    )
