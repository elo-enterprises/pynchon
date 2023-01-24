""" pynchon.bin.render:
    Option parsing for the `render` subcommand
"""
import sys
import yaml
import pynchon
from pynchon import (
    util,
)
from .common import kommand
from pynchon.bin import groups, options
from pynchon.api import render
import click
import os
import json
import pyjson5

LOGGER = pynchon.get_logger(__name__)
PARENT = groups.render
files_arg = click.argument("files", nargs=-1)


@kommand(
    name="json5",
    parent=PARENT,
    # formatters=dict(),
    options=[
        # options.file,
        # options.stdout,
        options.output,
        options.templates,
        click.option(
            "--in-place",
            is_flag=True,
            default=False,
            help=("if true, writes to {file}.json (dropping any other extensions)"),
        ),
    ],
    arguments=[files_arg],
)
def render_json5(files, output, in_place, templates):
    """
    Render render JSON5 files -> JSON
    """
    assert files, "expected files would be provided"
    # if file:
    #     return render.j5(file, output=output, in_place=in_place)
    # elif files:
    # files = files.split(' ')
    LOGGER.debug(f"Running with many: {files}")
    file = files[0]
    files = files[1:]
    return render.j5(file, output=output, in_place=in_place, templates=templates)


@kommand(
    name="any",
    parent=PARENT,
    formatters=dict(
        # markdown=pynchon.T_TOC_CLI,
    ),
    options=[
        # options.file,
        options.format,
        # options.stdout,
        options.output,
    ],
)
def render_any(format, file, stdout, output):
    """
    Render files with given renderer
    """
    print("hello world")


@kommand(
    name="jinja",
    parent=PARENT,
    options=[
        # options.file,
        options.ctx,
        options.output,
        options.template,
        click.option(
            "--in-place",
            is_flag=True,
            default=False,
            help=(
                "if true, writes to {file}.{ext} (dropping any .j2 extension if present)"
            ),
        ),
    ],
    arguments=[files_arg],
)
def render_j2(files, ctx, output, in_place, templates):
    """
    Render render J2 files with given context
    """
    # assert (file or files) and not (file and files), 'expected files would be provided'
    if not os.path.exists(templates):
        err = f"template directory @ `{templates}` does not exist"
        raise ValueError(err)
    if ctx:
        if "{" in ctx:
            LOGGER.debug("context is inlined JSON")
            ctx = json.loads(ctx)
        elif "=" in ctx:
            LOGGER.debug("context is inlined (comma-separed k=v format)")
            ctx = dict([kv.split("=") for kv in ctx.split(",")])
        else:
            with open(ctx, "r") as fhandle:
                content = fhandle.read()
            if ctx.endswith(".json"):
                LOGGER.debug("context is JSON file")
                ctx = json.loads(content)
            elif ctx.endswith(".json5"):
                LOGGER.debug("context is JSON-5 file")
                ctx = pyjson5.loads(content)
            elif ctx.endswith(".yml") or ctx.endswith(".yaml"):
                LOGGER.debug("context is yaml file")
                ctx = yaml.loads(content)
            else:
                raise TypeError(f"not sure how to load: {ctx}")
    else:
        ctx = {}
    LOGGER.debug("using context: ")
    LOGGER.debug(json.dumps(ctx))
    if files:
        return [
            render.j2(
                file, ctx=ctx, output=output, in_place=in_place, templates=templates
            )
            for file in files
        ]
    # elif files:
    #     LOGGER.debug(f"Running with many: {files}")
    #     return [
    #         render.j2(file, output=output, in_place=in_place, templates=templates)
    #         for file in files ]


# @kommand(
#     name='version', parent=PARENT,
#     # FIXME: formatters=dict(markdown=pynchon.T_VERSION_METADATA),
#     options=[
#         # FIXME: options.output_with_default('docs/VERSION.md'),
#         options.format_markdown,
#         options.stdout, options.header])
# def version(format, file, stdout, output, header):
#     """
#     Describes version details for package (and pynchon itself).
#     """
#     return dict(
#         pynchon_version='..',
#         package_version='..',
#         git_hash='..', )
