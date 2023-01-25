""" pynchon.api.project
"""
import os, glob
import json
import pynchon
from pynchon import (
    util,
)
from pynchon.bin import groups, options

# from pynchon.api import project, git, python
# from pynchon.abcs import Config
from pynchon.api import config

LOGGER = pynchon.get_logger(__name__)


def get_config() -> dict:
    """ """
    out = dict(
        pynchon=config.PynchonConfig(),
        git=dict(config.GitConfig()),
        python=config.PythonConfig(),
        project=config.ProjectConfig(),
    )
    return out


def plan(config: dict = {}) -> dict:
    """ """
    plan = []
    config = config or get_config()
    # src_root = util.find_src_root(config)
    # src_root = config['pynchon']['working_dir']
    # raise Exception(src_root)
    project = config["project"]
    gen_instructions = config.get('pynchon', {}).get("generate", [])
    LOGGER.debug(f"parsed generate-instructions: {gen_instructions}")
    render_instructions = config.get('pynchon', {}).get("render", [])
    LOGGER.debug(f"parsed render-instructions: {render_instructions}")
    config["source"] = dict(root=project.get("src_root"))
    # raise Exception(config)
    docs_root = config['pynchon']['docs_root']
    templates_root = f"{config['pynchon']['docs_root']}/templates"
    #config['git']['root']project.get("docs_root", os.path.join(src_root, "docs"))
    # conf_root = project.get("conf_root", os.path.join(src_root, "config"))
    if project["root"]:
        # __main__ = os.path.join(src_root, "**", "__main__.py")
        # __main__ = [os.path.relpath(x) for x in glob.glob(__main__, recursive=True)]
        # __main__ = dict(
        #     [
        #         [
        #             x,
        #             dict(
        #                 path=x,
        #                 dotpath=".".join(
        #                     filter(
        #                         lambda _: _.strip() and _ != "py" and _ != "__main__",
        #                         x.replace(src_root, "").replace("/", ".").split("."),
        #                     )
        #                 ),
        #             ),
        #         ]
        #         for x in __main__
        #     ]
        # )
        # config["source"].update(
            # __main__=__main__,
            # json5=json5s,
            # j2=j2s
            # )
        LOGGER.debug("planning for versioning these docs..")
        plan += [
            f"pynchon project version --output {docs_root}/VERSIONS.md",
        ]
        if "api" in gen_instructions:
            LOGGER.debug("planning for API docs..")
            api_root = f"{docs_root}/api"
            plan += [f"mkdir -p {api_root}"]
            plan += [
                f'pynchon gen api toc --package {config["python"]["package"]["name"]} --output {api_root}/README.md'
            ]
        else:
            LOGGER.warning("skipping plan for API-docs")
        if "cli" in gen_instructions:
            LOGGER.debug("planning for CLI docs..")
            cli_root = f"{docs_root}/cli"
            plan += [f"mkdir -p {cli_root}"]
            plan += [f"pynchon gen cli toc --output {cli_root}/README.md"]
            plan += [f"pynchon gen cli all --output-dir {cli_root}"]
            plan += [
                f"pynchon gen cli main --file {fname} --output-dir {cli_root}"
                for fname in config["python"]["entrypoints"]
            ]
        else:
            LOGGER.warning("skipping plan for CLI-docs")

        if 'j2' in render_instructions:
            j2s = util.find_j2s(config)
            if j2s:
                plan += [
                    f"pynchon render jinja --templates {templates_root} --in-place {fname} "
                    for fname in j2s
                ]
            else:
                LOGGER.critical("`j2` is present in `render` instructions, but found no .j2 files!")
        else:
            LOGGER.warning("skipping plan for rendering j2 files")
        # json5s = os.path.join(conf_root, "**", "*.json5")
        # json5s = [os.path.relpath(x) for x in glob.glob(json5s, recursive=True)]

    return config, plan
