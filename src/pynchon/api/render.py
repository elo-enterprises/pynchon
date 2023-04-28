""" pynchon.api.render
"""
import os
import sys
import json

import jinja2
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined

from pynchon import abcs
from pynchon.util import lme, text, typing
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


def loads_j2_file(
    file: str, ctx: typing.Dict = {}, templates: list = ["."], strict: bool = True
) -> str:
    """ """
    LOGGER.debug(f"Running with one file: {file} (strict={strict})")
    with open(file, "r") as fhandle:
        content = fhandle.read()

    LOGGER.debug("render context: \n{}".format(text.to_json(ctx)))
    tmp = list(ctx.keys())
    LOGGER.debug("Rendering with context:\n{}".format(text.to_json(tmp)))
    content = j2_loads(text=content, context=ctx, templates=templates)
    return content


def j2(
    file: str,
    output: str = "",
    in_place: bool = False,
    ctx: dict = {},
    templates: list = ["."],
    strict: bool = True,
) -> str:
    """
    render jinja2 file
    """

    def get_pynchon_ctx():
        from pynchon.api import project

        user_ctx = ctx
        project_config = project.get_config()
        if not isinstance(user_ctx, (dict,)):
            ext = os.path.splitext(ctx)[-1]
            if "{" in user_ctx:
                LOGGER.debug(
                    "found bracket in context, assuming it is data instead of file."
                )
                ctx = json.loads(ctx)  # noqa
            elif ext in ["json"]:
                LOGGER.debug(f"context is json file @ `{ctx}`")
                with open(ctx, "r") as fhandle:
                    ctx = json.loads(fhandle.read())
            else:
                LOGGER.critical(f"unrecognized extension for context file: {ext}")
                raise TypeError(ext)

        return {
            **ctx,
            **project_config,
        }

    final_ctx = get_pynchon_ctx()

    content = loads_j2_file(file=file, context=ctx, templates=templates, strict=strict)

    if in_place:
        assert not output, "cannot use --in-place and --output at the same time"
        output = os.path.splitext(file)
        if output[-1] == ".j2":
            output = output[0]
        else:
            output = "".join(output)
    LOGGER.warning("writing output to {}".format(output or sys.stdout.name))
    test = all([output, output not in ["/dev/stdout", "-"]])
    if test:
        with open(output, "r") as fhandle:
            before = fhandle.read()
    else:
        before = None
    fhandle = open(output, "w") if output else sys.stdout
    content = f"{content}\n"
    fhandle.write(content)
    fhandle.close()
    if before and content == before:
        LOGGER.critical(f"content in {output} did not change")
    return content


def shell_helper(*args, **kwargs) -> str:
    out = invoke(*args, **kwargs)
    assert out.succeeded
    return out.stdout


def j2_loads(
    text: str = "",
    context: dict = {},
    templates=["."],
    strict: bool = True,
):
    """ """
    templates = [abcs.Path(t) for t in templates]
    for template_dir in templates:
        if not template_dir.exists:
            err = f"template directory @ `{template_dir}` does not exist"
            raise ValueError(err)
    if templates:
        LOGGER.critical(f"Templates: {templates}")
    env = Environment(
        loader=FileSystemLoader([str(t) for t in templates]),
        undefined=StrictUndefined,
    )
    env.globals.update(shell=shell_helper, env=os.getenv)

    known_templates = map(abcs.Path, set(env.loader.list_templates()))
    # known_templates = [str(p) for p in known_templates if dot not in p.parents]
    if known_templates:
        from pynchon.util import text as util_text

        msg = "Known templates: "
        msg += "(excluding the ones under working-dir)"
        msg += "\n{}".format(util_text.to_json(known_templates))
        LOGGER.warning(msg)

    template = env.from_string(text)
    context = {**dict(os.environ.items()), **context}

    try:
        return template.render(**context)
    except (jinja2.exceptions.TemplateNotFound,) as exc:
        LOGGER.critical(exc)
        LOGGER.critical(known_templates)
        raise RuntimeError()


__all__ = [
    # "j5",
    "j2"
]
