""" pynchon.bin.project
"""
import os, glob
import json
import pynchon
from pynchon import (
    util,
)
from .common import kommand
from pynchon.bin import groups, options

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
    return util.load_entrypoints(util.load_setupcfg(file=file))


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
    return dict(
        pynchon_version=util.pynchon_version(),
        package_version=util.project_version(),
        git_hash=util.get_git_hash(),
    )


@kommand(
    name="apply",
    parent=PARENT,
    options=[],
)
def project_apply():
    """
    Apply the plan created by `pynchon project plan`
    """
    config, plan = _project_plan()
    for p in plan:
        util.invoke(p)
    return plan


def _project_plan(config: dict = {}) -> dict:
    """ """
    plan = []
    config = config or util.project_config()
    src_root = util.find_src_root(config)
    project = config["project"]
    cli_gen = project.get("cli_gen", True)
    api_gen = project.get("api_gen", True)
    config["source"] = dict(root=project["src_root"])
    docs_root = project.get("docs_root", os.path.join(src_root, "docs"))
    conf_root = project.get("conf_root", os.path.join(src_root, "config"))
    if project["root"]:
        __main__ = os.path.join(src_root, "**", "__main__.py")
        __main__ = [os.path.relpath(x) for x in glob.glob(__main__, recursive=True)]
        j2s = os.path.join(docs_root, "**", "*.j2")
        j2s = [os.path.relpath(x) for x in glob.glob(j2s, recursive=True)]
        json5s = os.path.join(conf_root, "**", "*.json5")
        json5s = [os.path.relpath(x) for x in glob.glob(json5s, recursive=True)]
        config["source"].update(__main__=__main__, json5=json5s, j2=j2s)
        plan += [
            f"pynchon project version --output {docs_root}/VERSIONS.md",
        ]
        if api_gen:
            api_root = f"{docs_root}/api"
            plan += [
                f'pynchon gen api toc --package {project["api_pkg"]} --output {api_root}/README.md'
            ]
        if cli_gen:
            if __main__:
                LOGGER.warning("ignoring __main__ files")
            cli_root = f"{docs_root}/cli"
            plan += [f"mkdir -p {cli_root}"]
            plan += [f"pynchon gen cli toc --output {cli_root}/README.md"]
            plan += [f"pynchon gen cli all --output-dir {cli_root}"]
    return config, plan


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
    config, plan = _project_plan()
    config["plan"] = plan
    return json.dumps(config, indent=2)
