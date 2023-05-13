""" pynchon.api.render

    Basically this is core jinja stuff.
    Looking for CLI entrypoints?  See pynchon.util.text.render
    Looking for the JinjaPlugin?  See pynchon.plugins.jinja
"""

import os
import functools

import pynchon
from pynchon import abcs, events

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)
import jinja2  # noqa
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined


def dictionary(input, context):
    """

    :param input: param context:
    :param context:

    """
    from pynchon.abcs.visitor import JinjaDict

    return JinjaDict(input).render(context)


@functools.lru_cache(maxsize=None)
def get_jinja_globals():
    """ """
    events.lifecycle.send(__name__, msg="finalizing jinja globals")
    # FIXME: use shimport.filter_module('..')
    from pynchon.util.os import invoke

    def invoke_helper(*args, **kwargs) -> typing.StringMaybe:
        """A jinja filter/extension

        :param *args:
        :param **kwargs:

        """
        out = invoke(*args, **kwargs)
        assert out.succeeded
        return out.stdout

    def markdown_toc(fname: str, level=None):
        """

        :param fname: str:
        :param level: Default value = None)
        :param fname: str:

        """
        fname = abcs.Path(fname)
        assert fname.exists()

        script = abcs.Path(pynchon.__file__).parents[0] / "scripts" / "gh-md-toc.sh"
        result = invoke(f"cat {fname} | bash {script} -")
        assert result.succeeded
        return result.stdout

    return dict(
        sh=invoke_helper,
        bash=invoke_helper,
        invoke=invoke_helper,
        map=map,
        markdown_toc=markdown_toc,
        eval=eval,
        env=os.getenv,
    )


from pynchon import constants


def get_jinja_includes(*includes):
    includes = list(includes)
    includes += list(constants.PYNCHON_CORE_INCLUDES_DIRS)

    return [abcs.Path(t) for t in includes]


@functools.lru_cache(maxsize=None)
def get_jinja_env(*includes, quiet: bool = False):
    """

    :param *includes:
    :param quiet: bool:  (Default value = False)

    """
    events.lifecycle.send(__name__, msg="finalizing jinja-Env")
    includes = get_jinja_includes(*includes)
    for template_dir in includes:
        if not template_dir.exists:
            err = f"template directory @ `{template_dir}` does not exist"
            raise ValueError(err)
    # includes and (not quiet) and LOGGER.warning(f"Includes: {includes}")
    env = Environment(
        loader=FileSystemLoader([str(t) for t in includes]),
        undefined=StrictUndefined,
    )
    env.pynchon_includes = includes

    env.globals.update(**get_jinja_globals())

    known_templates = list(map(abcs.Path, set(env.loader.list_templates())))

    if known_templates:
        from pynchon.util import text as util_text

        msg = "Known template search paths (includes folders only): "
        tmp = list({p.parents[0] for p in known_templates})
        LOGGER.info(msg + util_text.to_json(tmp))
    return env


def get_template(
    template_name: str = None,
    env=None,
    from_string: str = None,
):
    """

    :param template_name: str:  (Default value = None)
    :param env: Default value = None)
    :param from_string: str:  (Default value = None)
    :param template_name: str:  (Default value = None)
    :param from_string: str:  (Default value = None)

    """
    env = env or get_jinja_env()
    try:
        if from_string:
            template = env.from_string(from_string)
        else:
            template = env.get_template(template_name)
    except (jinja2.exceptions.TemplateNotFound,) as exc:
        LOGGER.critical(f"Template exception: {exc}")
        LOGGER.critical(f"Jinja-includes: {env.pynchon_includes}")
        err = getattr(exc, "templates", exc.message)
        LOGGER.critical(f"Problem template: {err}")
        raise
    template.render = functools.partial(template.render, __template__=template_name)
    # @functools.wraps(template.render)
    # def myrender(*args, **kwargs):
    #     """ """
    #     kwargs.update(
    #         __template__ = kwargs.get('__template__', template_name))
    #     tmp = template.render(*args, **kwargs)
    #     return tmp
    # template.render = myrender
    return template
