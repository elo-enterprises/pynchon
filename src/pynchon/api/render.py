""" pynchon.api.render
"""
import os, json, sys
import pyjson5

from jinja2 import (
    Environment, FileSystemLoader,
    StrictUndefined,Template,
    # UndefinedError,
)

import pynchon
from pynchon import (util,)

LOGGER = pynchon.get_logger(__name__)

def rj5(file, output='', in_place=False,):
    """ renders json5 file """
    LOGGER.debug(f"Running with one file: {file}")
    with open(file, 'r') as fhandle:
        data = pyjson5.loads(fhandle.read())
    if in_place:
        assert not output,'cannot use --in-place and --output at the same time'
        output = os.path.splitext(file)[0]
        output = f'{output}.json'
    if output:
        with open(output,'w') as fhandle:
            content = json.dumps(data)
            fhandle.write(f"{content}\n")
    return data

def rj2(file, output='', in_place=False, ctx={}, templates='.', strict:bool=True):
    """ render jinja2 file """
    def load_ctx():
        """ """
        pass
    LOGGER.debug(f"Running with one file: {file}")
    with open(file, 'r') as fhandle:
        content = fhandle.read()
    if in_place:
        assert not output,'cannot use --in-place and --output at the same time'
        output = os.path.splitext(file)
        if output[-1]=='.j2':
            output = output[0]
        else:
            output = ''.join(output)
    if not isinstance(ctx, (dict,)):
        ext = os.path.splitext(ctx)[-1]
        if '{' in ctx:
            LOGGER.debug("found bracket in context, assuming it is data instead of file.")
            ctx = json.loads(ctx)
        elif ext in ['json']:
            LOGGER.debug(f"context is json file @ `{ctx}`")
            with open(ctx,'r') as fhandle:
                ctx = json.loads(fhandle.read())
        else:
            LOGGER.critical(f"unrecognized extension for context file: {ext}")
            raise TypeError(ext)
    tmp = list(ctx.keys())
    LOGGER.debug(f"rendering with context: {tmp}")
    content = _render(text=content, context=ctx, templates=templates)
    fhandle = open(output, 'w')if output else sys.stdout
    fhandle.write(f"{content}\n")
    fhandle.close()
    return content

def _render(text:str='', context:dict={}, templates='.', strict:bool=True,):
    """ """
    # FIXME: support strict
    git_root = util.find_git_root()
    LOGGER.debug(f"found {git_root} for root")
    env = Environment(
            loader=FileSystemLoader([
                os.path.join(git_root, 'docs','templates'),
                os.path.join(git_root, 'docs','includes'),
                ]),
            undefined=StrictUndefined)
    tmp = env.from_string(text)
    context = {
        **dict(os.environ.items()),
        **context
    }
    return tmp.render(**context)
