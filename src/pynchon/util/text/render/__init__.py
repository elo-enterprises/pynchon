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

from pynchon.util.text import loadf as _sibling
from pynchon.cli import click, common, options
from pynchon.util.tagging import tags

LOGGER = lme.get_logger(__name__)


def shell_helper(*args, **kwargs) -> typing.StringMaybe:
    """ """
    out = invoke(*args, **kwargs)
    assert out.succeeded
    return out.stdout


# def json5_loadc(
#     output: str = '',
#     files: typing.List[str] = [],
#     wrapper_key: str = '',
#     pull: str = '',
#     push_data: str = '',
#     push_file_data: str = '',
#     push_json_data: str = '',
#     push_command_output: str = '',
#     under_key: str = '',
# ) -> None:
#     """
#     loads json5 file(s) and outputs json.
#     if multiple files are provided, files will
#     be merged with overwrites in the order provided
#     """
#     out: typing.Dict[str, typing.Any] = {}
#     for file in files:
#         obj = loadf.json5(file=file)
#         out = {**out, **obj}
#
#     push_args = [push_data, push_file_data, push_json_data, push_command_output]
#     if any(push_args):
#         assert under_key
#         assert under_key not in out, f'content already has key@{under_key}!'
#         assert (
#             sum([1 for x in push_args if x]) == 1
#         ), 'only one --push arg can be provided!'
#         if push_data:
#             assert isinstance(push_data, (str,))
#             push = push_data
#         elif push_command_output:
#             cmd = invoke(push_command_output)
#             if cmd.succeeded:
#                 push = cmd.stdout
#             else:
#                 err = cmd.stderr
#                 LOGGER.critical(err)
#                 raise SystemExit(1)
#         elif push_json_data:
#             push = loads.json5(content=push_json_data)
#         elif push_file_data:
#             err = f'file@{push_file_data} doesnt exist'
#             assert os.path.exists(push_file_data), err
#             with open(push_file_data, 'r') as fhandle:
#                 push = fhandle.read()
#         out[under_key] = push
#
#     if wrapper_key:
#         # NB: must remain after push
#         out = {wrapper_key: out}
#
#     return out
#


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

_sibling.jinja = jinja



@options.output
@options.should_print
@options.option_inplace
@options.option_templates
@click.option('--context', help='context file.  must be JSON')
@click.argument("file", nargs=1)
@tags(
    click_aliases=['jinja'],
)
def jinja_file(
    file: str,
    output: str = "",
    should_print: bool = False,
    in_place: bool = False,
    context: dict = {},
    templates: typing.List[str] = ["."],
    strict: bool = True,
) -> str:
    """
    Renders jinja2 file (supports includes, custom filters)
    """
    # def get_pynchon_ctx():
    #     # from pynchon.api import project
    #     # project_config = project.get_config()
    #     project_config={}
    #     user_ctx = context
    #     if not isinstance(user_ctx, (dict,)):
    #         ext = abcs.Path(ctx).splitext()[-1]
    #         if "{" in user_ctx:
    #             LOGGER.debug(
    #                 "found bracket in context, assuming it is data instead of file."
    #             )
    #             ctx = json.loads(ctx)  # noqa
    #         elif ext in ["json"]:
    #             LOGGER.debug(f"context is json file @ `{ctx}`")
    #             with open(ctx, "r") as fhandle:
    #                 ctx = json.loads(fhandle.read())
    #         else:
    #             LOGGER.critical(f"unrecognized extension for context file: {ext}")
    #             raise TypeError(ext)
    #
    #     return {
    #         **ctx,
    #         **project_config,
    #     }

    ctx = final_ctx = context

    content = THIS.loadf_jinja(
        file=file, context=context or {}, templates=[templates], strict=strict
    )

    if in_place:
        # assert not output, "cannot use --in-place and --output at the same time"
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


@options.output
@options.should_print
@click.option('--context', help='context file.  must be JSON')
@click.argument("file", nargs=1)
@tags(
    click_aliases=['j2'],
)
def j2cli(
    output: str, should_print: bool, file: str, context: str, format: str = 'json'
) -> None:
    """
    A wrapper on the `j2` command (j2cli must be installed)
    Renders the named file, using the given context-file.

    NB: No support for jinja-includes or custom filters.
    """
    from pynchon.util.os import invoke

    cmd = f'j2 --format {format} {file} {context}'
    result = invoke(cmd)
    if not result.succeeded:
        LOGGER.critical(f'failed to execute: {cmd}')
        raise SystemExit(1)
    result = result.stdout
    assert result
    tmp = file.replace('.j2', '')
    if tmp.endswith('.json') or tmp.endswith('.json5'):
        LOGGER.debug(f"target @ {file} appears to be specifying json.")
        LOGGER.debug("loading as if json5 before display..")
        result = text.loads.json5(content=result)
        result = text.to_json(result)
    msg = result
    print(msg, file=open(output, 'w'))
    if should_print and output != '/dev/stdout':
        print(msg)
