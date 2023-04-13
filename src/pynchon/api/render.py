""" pynchon.api.render
"""
import json
import os
import sys

import pyjson5
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined

from pynchon import abcs, util
from pynchon.util import lme

LOGGER = lme.get_logger(__name__)


def dot(file: str, output: str = "", in_place: bool = False, output_mode: str = "png"):
    """renders .dot file to png"""
    if in_place:
        assert not output
        output = os.path.splitext(file)[0] + ".png"
    # Using https://github.com/nickshine/dot
    DOT_DOCKER_IMG = "nshine/dot"
    util.invoke(
        f"cat {file} | docker run --rm --entrypoint dot -i {DOT_DOCKER_IMG} -T{output_mode} > {output}"
    )
    return dict(output=output)


def j5(
    file,
    output="",
    in_place=False,
):
    """renders json5 file"""
    LOGGER.debug(f"Running with one file: {file}")
    with open(file, "r") as fhandle:
        data = pyjson5.loads(fhandle.read())
    if in_place:
        assert not output, "cannot use --in-place and --output at the same time"
        output = os.path.splitext(file)[0]
        output = f"{output}.json"
    if output:
        with open(output, "w") as fhandle:
            content = json.dumps(data)
            fhandle.write(f"{content}\n")
    return data


def j2(
    file: str,
    output: str = "",
    in_place: bool = False,
    ctx: dict = {},
    templates: list = ["."],
    strict: bool = True,
):
    """render jinja2 file"""
    templates = [abcs.Path(t) for t in templates]
    for template_dir in templates:
        if not template_dir.exists:
            err = f"template directory @ `{template_dir}` does not exist"
            raise ValueError(err)

    LOGGER.debug(f"Running with one file: {file} (strict={strict})")
    with open(file, "r") as fhandle:
        content = fhandle.read()
    if in_place:
        assert not output, "cannot use --in-place and --output at the same time"
        output = os.path.splitext(file)
        if output[-1] == ".j2":
            output = output[0]
        else:
            output = "".join(output)
    if not isinstance(ctx, (dict,)):
        ext = os.path.splitext(ctx)[-1]
        if "{" in ctx:
            LOGGER.debug(
                "found bracket in context, assuming it is data instead of file."
            )
            ctx = json.loads(ctx)
        elif ext in ["json"]:
            LOGGER.debug(f"context is json file @ `{ctx}`")
            with open(ctx, "r") as fhandle:
                ctx = json.loads(fhandle.read())
        else:
            LOGGER.critical(f"unrecognized extension for context file: {ext}")
            raise TypeError(ext)
    tmp = list(ctx.keys())
    LOGGER.debug(f"Templates: {templates}")
    LOGGER.debug(f"Rendering with context: {tmp}")
    content = _render(text=content, context=ctx, templates=templates)
    LOGGER.warning(f"writing output to {output or sys.stdout.name}")
    before = None
    if output:
        with open(output, "r") as fhandle:
            before = fhandle.read()
    fhandle = open(output, "w") if output else sys.stdout
    content = f"{content}\n"
    fhandle.write(content)
    fhandle.close()
    if before and content == before:
        LOGGER.critical(f"content in {output} did not change")
    return content


def _render(
    text: str = "",
    context: dict = {},
    templates=".",
    strict: bool = True,
):
    """ """
    # LOGGER.debug(f"_render with templates={templates}")
    # FIXME: support strict
    # git_root = util.find_git_root()
    # LOGGER.debug(f"found {git_root} for root")
    env = Environment(
        loader=FileSystemLoader([str(t) for t in templates]),
        undefined=StrictUndefined,
    )
    LOGGER.warning("known templates:")
    LOGGER.warning(env.loader.list_templates())
    template = env.from_string(text)
    context = {**dict(os.environ.items()), **context}
    return template.render(**context)


__all__ = ["j5", "j2"]
