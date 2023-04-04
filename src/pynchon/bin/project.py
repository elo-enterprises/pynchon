""" pynchon.bin.project
"""
import glob
import json
import os

from pynchon import abcs, constants, util
from pynchon.api import project
from pynchon.bin import groups, options
from pynchon.util import lme

from .common import kommand

LOGGER = lme.get_logger(__name__)
PARENT = groups.project


@kommand(
    name="entrypoints",
    parent=PARENT,
    formatters=dict(markdown=constants.T_TOC_CLI),
    options=[
        options.file_setupcfg,
        options.format,
        options.stdout,
        options.output,
        options.header,
    ],
)
def project_entrypoints(format, file, stdout, output, header) -> None:
    """
    Describe entrypoints for this project (parses setup.cfg)
    """
    config, plan = project.plan()
    return {
        **util.python.load_entrypoints(util.python.load_setupcfg(file=file)),
        **dict(__main__=config.get("source", {}).get("__main__", [])),
    }


@kommand(
    name="version",
    parent=PARENT,
    formatters=dict(markdown=constants.T_VERSION_METADATA),
    options=[
        # FIXME: options.output_with_default('docs/VERSION.md'),
        options.format_markdown,
        options.output,
        options.header,
    ],
)
def project_version(format, output, header) -> None:
    """
    Describes version details for this package (and pynchon itself).
    """
    # from pynchon.api import python #, git
    import pynchon
    from pynchon.config import git, python

    return dict(
        pynchon_version=pynchon.__version__,
        package_version=python.package.version,
        git_hash=git.hash,
    )


@kommand(
    name="config",
    parent=PARENT,
    options=[],
)
def project_config() -> None:
    """
    Describe the config for this project
    """
    tmp = project.get_config()
    print(json.dumps(tmp, cls=abcs.JSONEncoder))


@kommand(
    name="apply",
    parent=PARENT,
    options=[],
)
def project_apply() -> None:
    """
    Apply the plan created by `pynchon project plan`
    """
    config, plan = project.plan()
    for p in plan:
        util.invoke(p)
    return plan


@kommand(
    name="plan",
    parent=PARENT,
    options=[
        options.stdout,
    ],
)
def project_plan(stdout):
    """
    List goals for auto-documenting this project
    """
    config, plan = project.plan()
    config["plan"] = plan
    return json.dumps(config, indent=2, cls=abcs.JSONEncoder)
