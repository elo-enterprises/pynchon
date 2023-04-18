""" pynchon.util.files
"""
from . import lme

LOGGER = lme.get_logger(__name__)
import functools
import glob

from pynchon.abcs import Path


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
