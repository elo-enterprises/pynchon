""" pynchon.api.project
"""
import glob
import json
import os

import pynchon
from pynchon import abcs, config, util
from pynchon.bin import groups, options
from pynchon.util import lme

LOGGER = lme.get_logger(__name__)


def get_config() -> dict:
    """ """
    return dict(
        [
            [k, getattr(config, k)]
            for k in dir(config)
            if isinstance(getattr(config, k), (abcs.Config,))
        ]
    )


def plan(config: dict = {}) -> dict:
    """ """
    plan = []
    config = config or get_config()
    project = config["project"]
    render_instructions = config.get("pynchon", {}).get("render", [])
    gen_instructions = config.get("pynchon", {}).get("generate", [])
    LOGGER.debug(f"parsed generate-instructions: {gen_instructions}")
    render_instructions = config.get("pynchon", {}).get("render", [])
    LOGGER.debug(f"parsed render-instructions: {render_instructions}")
    # config["source"] = dict(root=project.get("src_root"))
    # raise Exception(config)
    docs_root = config["pynchon"].get(
        "docs_root", os.path.relpath(config["pynchon"]["working_dir"])
    )
    # config['git']['root']project.get("docs_root", os.path.join(src_root, "docs"))
    # conf_root = project.get("conf_root", os.path.join(src_root, "config"))
    # if project["root"]:
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
    LOGGER.debug("planning to ensure docs_root exists..")
    plan += [
        f"mkdir -p {docs_root}",
    ]
    LOGGER.debug("planning for versioning these docs..")
    plan += [
        f"pynchon project version --output {docs_root}/VERSIONS.md",
    ]
    if "dot" in render_instructions:
        LOGGER.debug("planning for rendering for .dot graph files..")
        dot_root = project["root"]
        for line in util.invoke(f"find {dot_root} -type f -name *.dot").stdout.split(
            "\n"
        ):
            line = line.strip()
            if not line:
                continue
            plan += [f"pynchon render dot {line} --in-place"]
    if "dot" in gen_instructions:
        LOGGER.debug("planning generation for .dot graph files..")
        from pathlib import Path

        dot_config = config["pynchon"].get("dot", {})
        script = dot_config.get("script")
        # # assert script, '`"dot" in pynchon.generate` but pynchon.dot.script is not set!'
        # from pynchon.api import render
        #
        # # FIXME: do this substition everywhere!
        # script = render._render(text=script, context=config)
        cmd = "pynchon gen dot files --script {script}"
        plan += [cmd]
    if "fixme" in gen_instructions:
        plan += [f"pynchon gen fixme --output {docs_root}/FIXME.md"]
    if "api" in gen_instructions:
        LOGGER.critical("loading `api` generator..")
        LOGGER.debug("planning for API docs..")
        api_root = f"{docs_root}/api"
        plan += [f"mkdir -p {api_root}"]
        plan += [
            "pynchon gen api toc"
            f' --package {config["python"]["package"]["name"]}'
            f" --output {api_root}/README.md"
        ]
    else:
        LOGGER.warning("skipping plan for API-docs")
    if "cli" in gen_instructions:
        LOGGER.critical("loading cli generator..")
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

    if "j2" in render_instructions:
        LOGGER.critical("loading j2 renderer..")
        templates = config["jinja"].includes
        templates = [t for t in templates]
        # import IPython; IPython.embed()
        templates = [f"--templates {t}" for t in templates]
        templates = " ".join(templates)
        LOGGER.warning(f"j2 templates: {templates}")
        j2s = util.find_j2s(config)
        if j2s:
            plan += [
                f"pynchon render jinja {templates} --in-place {fname} " for fname in j2s
            ]
        else:
            LOGGER.critical(
                "`j2` is present in `render` instructions, but found no .j2 files!"
            )
    else:
        LOGGER.warning("skipping plan for rendering j2 files")
    # json5s = os.path.join(conf_root, "**", "*.json5")
    # json5s = [os.path.relpath(x) for x in glob.glob(json5s, recursive=True)]

    return config, plan
