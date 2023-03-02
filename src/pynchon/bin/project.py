""" pynchon.bin.project
"""
import os, glob
import json
import pynchon

from pynchon import (abcs, util,)
from .common import kommand
from pynchon.bin import groups, options
from pynchon.api import project

LOGGER = pynchon.get_logger(__name__)
PARENT = groups.project


@kommand(
    name="entrypoints",
    parent=PARENT,
    formatters=dict(markdown=pynchon.T_TOC_CLI),
    options=[
        options.file_setupcfg,
        options.format,
        options.stdout,
        options.output,
        options.header,
    ],
)
def project_entrypoints(format, file, stdout, output, header):
    """
    Describe entrypoints for this project (parses setup.cfg)
    """
    config, plan = project.plan()
    return {
        **util.load_entrypoints(util.load_setupcfg(file=file)),
        **dict(__main__=config.get("source", {}).get("__main__", [])),
    }


@kommand(
    name="version",
    parent=PARENT,
    formatters=dict(markdown=pynchon.T_VERSION_METADATA),
    options=[
        # FIXME: options.output_with_default('docs/VERSION.md'),
        options.format_markdown,
        options.output,
        options.header,
    ],
)
def project_version(format, output, header):
    """
    Describes version details for this package (and pynchon itself).
    """
    from pynchon.api import python, git

    return dict(
        pynchon_version=util.pynchon_version(),
        package_version=python.get_package_version(),
        git_hash=git.get_hash(),
    )


@kommand(
    name="config",
    parent=PARENT,
    options=[],
)
def project_config():
    """
    Describe the config for this project
    """
    tmp = project.get_config()
    LOGGER.debug(json.dumps(tmp, indent=2, cls=abcs.JSONEncoder))


@kommand(
    name="apply",
    parent=PARENT,
    options=[],
)
def project_apply():
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
