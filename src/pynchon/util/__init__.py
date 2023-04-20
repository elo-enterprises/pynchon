""" pynchon.util
"""
import os
import sys

# import glob
from pynchon import constants

from . import lme

# from .os import invoke

# import functools

# import tomli as tomllib  # tomllib only available in py3.11


LOGGER = lme.get_logger(__name__)


def get_root(path: str = ".") -> str:
    """ """
    import os

    from pynchon.abcs import Path

    path = Path(path).absolute()
    if (path / ".git").exists():
        return path.relative_to(os.getcwd())
    elif not path:
        return None
    else:
        return get_root(path.parents[0])


def is_python_project() -> bool:
    """ """
    from pynchon.api import git

    return os.path.exists(os.path.join(git.get_root(), constants.PYNCHON_CONFIG_FILE))


def find_src_root(config: dict) -> str:
    """ """
    from pynchon.abcs import Path

    pconf = config.get("project", {})
    LOGGER.debug(f"project config: {pconf}")
    src_root = Path(pconf.get("src_root", "."))
    # src_root = os.path.join(project_root, "src")
    src_root = src_root if src_root.is_dir() else None
    return src_root.relative_to(".")


def click_recursive_help(cmd, parent=None, out={}, file=sys.stdout):
    """ """
    # source: adapted from https://stackoverflow.com/questions/57810659/automatically-generate-all-help-documentation-for-click-commands
    from click.core import Context as ClickContext

    full_name = cmd.name
    pname = getattr(cmd, "parent", None)
    pname = parent and getattr(parent, "name", "") or ""
    ctx = ClickContext(cmd, info_name=cmd.name, parent=parent)
    help_txt = cmd.get_help(ctx)
    invocation_sample = help_txt.split("\n")[0]
    for x in "Usage: [OPTIONS] COMMAND [COMMAND] [ARGS] ...".split():
        invocation_sample = invocation_sample.replace(x, "")
    out = {
        **out,
        **{
            full_name: dict(
                name=cmd.name, invocation_sample=invocation_sample, help=help_txt
            )
        },
    }
    commands = getattr(cmd, "commands", {})
    for sub in commands.values():
        out = {**out, **click_recursive_help(sub, ctx)}
    return out
