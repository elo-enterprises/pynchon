""" pynchon.api.python
"""
from pynchon.util import lme, files, text

LOGGER = lme.get_logger(__name__)


def is_package() -> bool:
    """ """
    from pynchon.config import python

    return python.is_package


def load_setupcfg(file: str = ""):
    """ """
    if not file:
        file = files.get_git_root().parents[0] / 'setup.cfg'
    return text.loadf.ini(file)
    # from pynchon.util import config
    # return config.ini_loads(file)


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
