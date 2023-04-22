""" pynchon.util.files
"""
import re
import glob
import functools

from pynchon.abcs import Path
from pynchon.util.os import invoke

from . import lme, typing

LOGGER = lme.get_logger(__name__)


def find_suffix(root: str = '', suffix: str = '') -> typing.StringMaybe:
    assert root and suffix
    return invoke(f"{root} -type f -name *.{suffix}").stdout.split("\n")


def get_git_root(path: str = ".") -> str:
    """ """
    path = Path(path).absolute()
    tmp = path / ".git"
    if tmp.exists():
        return tmp
    elif not path:
        return None
    else:
        return get_git_root(path.parents[0])


def find_src(src_root: str, exclude_patterns=[]) -> list:
    """ """
    exclude_patterns = set(list(map(re.compile, exclude_patterns)))
    globs = [
        Path(src_root).joinpath("**/*"),
    ]
    LOGGER.debug(f"finding src under {globs}")
    globs = [glob.glob(str(x), recursive=True) for x in globs]
    matches = functools.reduce(lambda x, y: x + y, globs)
    matches = [str(x.absolute()) for x in map(Path, matches) if not x.is_dir()]
    LOGGER.debug(matches)
    import IPython

    IPython.embed()
    matches = [
        m for m in matches if not any([p.match(str(m)) for p in exclude_patterns])
    ]
    return matches


def find_j2s(conf) -> list:
    """ """
    from pynchon import abcs, config

    project = config.project.get("subproject", config.project)
    project_root = project.get("root", config.git["root"])
    globs = [
        Path(project_root).joinpath("**/*.j2"),
    ]
    LOGGER.debug(f"finding .j2s under {globs}")
    globs = [glob.glob(str(x), recursive=True) for x in globs]
    matches = functools.reduce(lambda x, y: x + y, globs)
    includes = []
    for i, m in enumerate(matches):
        for d in config.jinja.includes:
            if abcs.Path(d).has_file(m):
                includes.append(m)
            # else:
            #     LOGGER.warning(f"'{d}'.has_file('{m}') -> false")
    j2s = []
    for m in matches:
        assert m
        if m not in includes:
            j2s.append(Path(m))
    return j2s


# def find_j2s(conf) -> list:
#     """ """
#     from pynchon import abcs, config
#
#     project = config.project.get("subproject", config.project)
#     project_root = project.get("root", config.git["root"])
#     globs = [
#         Path(project_root).joinpath("**/*.j2"),
#     ]
#     LOGGER.debug(f"finding .j2s under {globs}")
#     globs = [glob.glob(str(x), recursive=True) for x in globs]
#     matches = functools.reduce(lambda x, y: x + y, globs)
#     includes = []
#     for i, m in enumerate(matches):
#         for d in config.jinja.includes:
#             if abcs.Path(d).has_file(m):
#                 includes.append(m)
#             else:
#                 LOGGER.warning(f"'{d}'.has_file('{m}') -> false")
#     j2s = [Path(m).relative_to(".") for m in matches if m not in includes]
#     return j2s
