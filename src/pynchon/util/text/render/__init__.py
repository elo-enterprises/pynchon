""" pynchon.util.text.render
"""
import os

import jinja2
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined

from pynchon import abcs
from pynchon.util import typing, lme
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


def shell_helper(*args, **kwargs) -> typing.StringMaybe:
    """ """
    out = invoke(*args, **kwargs)
    assert out.succeeded
    return out.stdout

import os
import sys
import json

from pynchon import abcs
from pynchon.util import lme, text, typing

LOGGER = lme.get_logger(__name__)


@typing.validate_arguments
def loads_j2_file(
    file: str, context: typing.Dict = {},
        templates: typing.List[str] = ["."],strict: bool = True
) -> str:
    """ """
    # from pynchon.util.text.render import j2_loads
    context = {} if context is None else context
    LOGGER.debug(f"Running with one file: {file} (strict={strict})")
    with open(file, "r") as fhandle:
        content = fhandle.read()
    LOGGER.debug("render context: \n{}".format(text.to_json(context)))
    tmp = list(context.keys())
    LOGGER.debug("Rendering with context:\n{}".format(text.to_json(tmp)))
    content = j2_loads(text=content, context=context, templates=templates)
    return content

@typing.validate_arguments
def jinja(
    text: str = "",
    context: dict = {},
    templates:typing.List[abcs.Path]=[abcs.Path(".")],
    strict: bool = True,
):
    """
    Renders jinja-templates (with support for includes)
    """

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

j2_loads = jinja
