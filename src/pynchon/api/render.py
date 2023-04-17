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
    from pynchon.api import project

    config = project.get_config()
    ctx = {
        **ctx,
        **config,
    }
    from pynchon.util import text

    LOGGER.debug("render context: \n{}".format(text.to_json(ctx)))
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

    LOGGER.critical(f"Templates: {templates}")
    LOGGER.debug("Rendering with context:\n{}".format(json.dumps(tmp, indent=2)))
    content = _render(text=content, context=ctx, templates=templates)
    LOGGER.warning("writing output to {}".format(output or sys.stdout.name))
    before = None
    if output and output not in ["/dev/stdout", "-"]:
        with open(output, "r") as fhandle:
            before = fhandle.read()
    fhandle = open(output, "w") if output else sys.stdout
    content = f"{content}\n"
    fhandle.write(content)
    fhandle.close()
    if before and content == before:
        LOGGER.critical(f"content in {output} did not change")
    return content


def shell_helper(*args, **kwargs) -> str:
    from pynchon.util.os import invoke

    out = invoke(*args, **kwargs)
    assert out.succeeded
    return out.stdout


def _render(
    text: str = "",
    context: dict = {},
    templates=".",
    strict: bool = True,
):
    """ """
    env = Environment(
        loader=FileSystemLoader([str(t) for t in templates]),
        undefined=StrictUndefined,
    )
    env.globals.update(shell=shell_helper)

    known_templates = map(abcs.Path, set(env.loader.list_templates()))
    known_templates = [str(p) for p in known_templates if dot not in p.parents]
    msg = "Known templates: "
    msg += "(excluding the ones under working-dir)"
    msg += "\n{}".format(json.dumps(known_templates, indent=2))
    LOGGER.warning(msg)

    template = env.from_string(text)
    context = {**dict(os.environ.items()), **context}
    import jinja2

    try:
        return template.render(**context)
    except (jinja2.exceptions.TemplateNotFound,) as exc:
        LOGGER.critical(exc)
        LOGGER.critical(known_templates)
        raise RuntimeError()

        # raise


__all__ = ["j5", "j2"]
