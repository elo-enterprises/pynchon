""" pynchon.util.text.render

    Helpers for rendering content
"""
import os

import jinja2
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined

from pynchon import abcs
from pynchon.util import typing, lme, text
from pynchon.util.os import invoke
from pynchon.util.text import loadf, loads

LOGGER = lme.get_logger(__name__)


def shell_helper(*args, **kwargs) -> typing.StringMaybe:
    """ """
    out = invoke(*args, **kwargs)
    assert out.succeeded
    return out.stdout


def json5_loadc(
    output: str = '',
    files: typing.List[str] = [],
    wrapper_key: str = '',
    pull: str = '',
    push_data: str = '',
    push_file_data: str = '',
    push_json_data: str = '',
    push_command_output: str = '',
    under_key: str = '',
) -> None:
    """
    loads json5 file(s) and outputs json.
    if multiple files are provided, files will
    be merged with overwrites in the order provided
    """
    out: typing.Dict[str, typing.Any] = {}
    for file in files:
        obj = loadf.json5(file=file)
        out = {**out, **obj}

    push_args = [push_data, push_file_data, push_json_data, push_command_output]
    if any(push_args):
        assert under_key
        assert under_key not in out, f'content already has key@{under_key}!'
        assert (
            sum([1 for x in push_args if x]) == 1
        ), 'only one --push arg can be provided!'
        if push_data:
            assert isinstance(push_data, (str,))
            push = push_data
        elif push_command_output:
            cmd = invoke(push_command_output)
            if cmd.succeeded:
                push = cmd.stdout
            else:
                err = cmd.stderr
                LOGGER.critical(err)
                raise SystemExit(1)
        elif push_json_data:
            push = loads.json5(content=push_json_data)
        elif push_file_data:
            err = f'file@{push_file_data} doesnt exist'
            assert os.path.exists(push_file_data), err
            with open(push_file_data, 'r') as fhandle:
                push = fhandle.read()
        out[under_key] = push

    if wrapper_key:
        # NB: must remain after push
        out = {wrapper_key: out}

    return out


@typing.validate_arguments
def loadf_jinja(
    file: str,
    context: typing.Dict = {},
    templates: typing.List[str] = ["."],
    strict: bool = True,
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
    templates: typing.List[abcs.Path] = [abcs.Path(".")],
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
