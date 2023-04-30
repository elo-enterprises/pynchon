""" pynchon.util.text.loadf

    Helpers for loading data structures from files
"""
import os

import jinja2
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined

from pynchon import abcs
from pynchon.cli import click, options
from pynchon.util import typing, lme, text
from pynchon.util.os import invoke
from pynchon.util.text import loads

LOGGER = lme.get_logger(__name__)


@click.argument("file", nargs=1)
def json5(file: str = '') -> dict:
    """
    loads json5 from filezzz
    """
    assert file
    if not os.path.exists(file):
        raise ValueError(f'file @ {file} is missing!')
    with open(file, 'r') as fhandle:
        content = fhandle.read()
    data = loads.json5(content)
    return data


def shell_helper(*args, **kwargs) -> typing.StringMaybe:
    """ """
    out = invoke(*args, **kwargs)
    assert out.succeeded
    return out.stdout


@click.option(
    '--wrap-with-key',
    'wrapper_key',
    help='when set, wraps output as `{WRAPPER_KEY:output}`',
    # var='WRAPPER_KEY',
    default='',
)
@options.output
@options.should_print
@click.option('--pull', help='when provided, this key will be output', default='')
@click.option(
    '--push-data', help='(string) this raw data will be added to output', default=''
)
@click.option(
    '--push-file-data',
    help='(filename) contents of file will be added to output',
    default='',
)
@click.option(
    '--push-json-data',
    help='(string) jsonified data will be added to output',
    default='',
)
@click.option(
    '--push-command-output', help="command's stdout will be added to output", default=''
)
@click.option('--under-key', help='required with --push commands', default='')
@click.argument("files", nargs=-1)
def json5_load(
    output: str = '',
    should_print: bool = False,
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
    out = text.json5_loadc(
        files=files,
        wrapper_key=wrapper_key,
        pull=pull,
        push_data=push_data,
        push_file_data=push_file_data,
        push_json_data=push_json_data,
        push_command_output=push_command_output,
        under_key=under_key,
    )
    if pull:
        out = out[pull]
        # similar to `jq -r`.
        # we don't want quoted strings, but
        # if the value is complex, we need json-encoding
        if not isinstance(out, (str,)):
            msg = text.to_json(out)
        else:
            msg = str(out)
    else:
        msg = text.to_json(out)
    print(msg, file=open(output, 'w'))
    if should_print and output != '/dev/stdout':
        print(msg)


def json(file: str = '', content: str = '') -> dict:
    """
    loads json to python dictionary from given file or string
    """
    if file:
        assert not content
        if not os.path.exists(file):
            raise ValueError(f'file @ {file} is missing!')
        with open(file, 'r') as fhandle:
            content = fhandle.read()
    try:
        data = loads.json(content)
        # data = pyjson5.loads(content)
    # except (pyjson5.Json5EOF,) as exc:
    except (ValueError,) as exc:
        LOGGER.critical(f"Cannot parse json from {file}!")
        raise
    return data


@typing.validate_arguments
def loads_j2_file(
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
