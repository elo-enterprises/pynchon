""" pynchon.api.python
"""
import os

import tomli as tomllib  # tomllib only available in py3.11

from pynchon.util import lme, files

LOGGER = lme.get_logger(__name__)


def is_package() -> bool:
    """ """
    from pynchon.config import python

    return python.is_package


def load_setupcfg(path: str = ""):
    """ """
    path = path or os.path.join(files.get_git_root(), "setup.cfg")
    from pynchon.util import config

    return config.ini_loads(path)


def load_pyprojecttoml(path: str = ""):
    """ """
    import tomli

    if not os.path.exists(path):
        err = f"Cannot load config from nonexistent path @ `{path}`"
        LOGGER.critical(err)
        return None, {}
        # raise RuntimeError(err)

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
    return config


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
