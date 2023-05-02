""" pynchon.api.render

    Basically this is core jinja stuff.
    Looking for CLI entrypoints?  See pynchon.util.text.render
    Looking for the JinjaPlugin?  See pynchon.plugins.jinja
"""

import os
import functools

import pynchon
from pynchon import abcs

from pynchon.util import typing, lme  # noqa

LOGGER = lme.get_logger(__name__)
import jinja2  # noqa
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined


def dictionary(input, context):
    """ """
    from pynchon.abcs.visitor import JinjaDict

    return JinjaDict(input).render(context)


@functools.lru_cache(maxsize=None)
def get_jinja_globals():
    """ """

    def invoke_helper(*args, **kwargs) -> typing.StringMaybe:
        """
        A jinja filter/extension
        """
        from pynchon.util.os import invoke

        out = invoke(*args, **kwargs)
        assert out.succeeded
        return out.stdout

    return dict(invoke=invoke_helper, env=os.getenv)


@functools.lru_cache(maxsize=None)
def get_jinja_env(*includes, quiet: bool = False):
    """
    FIXME: Move to pynchon.api.render
    """
    includes = list(includes)
    ptemp = abcs.Path(pynchon.__file__).parents[0] / 'templates' / 'includes'
    includes += [ptemp]
    includes = [abcs.Path(t) for t in includes]

    for template_dir in includes:
        if not template_dir.exists:
            err = f"template directory @ `{template_dir}` does not exist"
            raise ValueError(err)
    # includes and (not quiet) and LOGGER.warning(f"Includes: {includes}")
    env = Environment(
        loader=FileSystemLoader([str(t) for t in includes]),
        undefined=StrictUndefined,
    )

    env.globals.update(**get_jinja_globals())

    known_templates = list(map(abcs.Path, set(env.loader.list_templates())))
    # known_templates = [str(p) for p in known_templates if dot not in p.parents]

    if known_templates:
        from pynchon.util import text as util_text

        msg = "Known template search paths (includes folders only): "
        # LOGGER.warning(msg)
        tmp = list(set([p.parents[0] for p in known_templates]))
        LOGGER.info(msg + util_text.to_json(tmp))
    return env
