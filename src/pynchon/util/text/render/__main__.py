""" pynchon.util.text.render CLI
"""
import os
import sys

from pynchon import click
from pynchon.cli import options
from pynchon.util import text, typing, lme

LOGGER = lme.get_logger(__name__)

from pynchon.util.text import render as THIS


def entry() -> typing.NoneType:
    pass


entry.__doc__ = __doc__ or ""


@options.output
@options.should_print
@options.option_inplace
@options.option_templates
@click.option('--context', help='context file.  must be JSON')
@click.argument("file", nargs=1)
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


entry = click.group('render')(entry)

entry.command('j2cli')(j2cli)
entry.command('j2')(j2cli)
entry.command('jinja')(jinja_file)
entry.command('jinja-file')(jinja_file)

if __name__ == '__main__':
    entry()
