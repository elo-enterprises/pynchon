""" pynchon.util.text.render

    Helpers for rendering content
"""
import os

import jinja2
from jinja2 import Environment  # Template,; UndefinedError,
from jinja2 import FileSystemLoader, StrictUndefined

from pynchon import abcs
from pynchon.cli import click, options
from pynchon.util import text
from pynchon.util.os import invoke
from pynchon.util.tagging import tags

from pynchon.util import typing, lme  # noqa

LOGGER = lme.get_logger(__name__)

from pynchon.util.text import loadf, loads


def _get_jinja_env(templates):
    """ """

    def _get_jinja_globals():
        """ """

        def invoke_helper(*args, **kwargs) -> typing.StringMaybe:
            """
            A jinja filter/extension
            """
            out = invoke(*args, **kwargs)
            assert out.succeeded
            return out.stdout

        return dict(invoke=invoke_helper, env=os.getenv)

    import pynchon

    ptemp = abcs.Path(pynchon.__file__).parents[0] / 'templates'
    templates += [ptemp]
    templates = [abcs.Path(t) for t in templates]

    for template_dir in templates:
        if not template_dir.exists:
            err = f"template directory @ `{template_dir}` does not exist"
            raise ValueError(err)
    if templates:
        LOGGER.warning(f"Templates: {templates}")
    env = Environment(
        loader=FileSystemLoader([str(t) for t in templates]),
        undefined=StrictUndefined,
    )

    env.globals.update(**_get_jinja_globals())

    known_templates = list(map(abcs.Path, set(env.loader.list_templates())))
    # known_templates = [str(p) for p in known_templates if dot not in p.parents]

    if known_templates:
        from pynchon.util import text as util_text

        msg = "Known templates: "
        msg += "\n{}".format(util_text.to_json(known_templates))
        LOGGER.warning(msg)
    return env


@typing.validate_arguments
def jinja_loadf(
    file: str,
    context: typing.Dict = {},
    templates: typing.List[str] = [],
    strict: bool = True,
    quiet: bool = False,
) -> str:
    """ """
    # from pynchon.util.text.render import jinja
    context = {} if context is None else context
    LOGGER.debug(f"Running with one file: {file} (strict={strict})")
    with open(file, "r") as fhandle:
        content = fhandle.read()
    quiet and LOGGER.debug("render context: \n{}".format(text.to_json(context)))
    tmp = list(context.keys())
    quiet and LOGGER.debug("Rendering with context:\n{}".format(text.to_json(tmp)))
    content = jinja(text=content, context=context, templates=templates)
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
    env = _get_jinja_env(templates)
    template = env.from_string(text)
    context = {
        # FIXME: try to santize this
        **dict(os.environ.items()),
        **context,
    }

    try:
        return template.render(**context)
    except (jinja2.exceptions.UndefinedError,) as exc:
        LOGGER.critical(f"Undefined exception: {exc}")
        LOGGER.critical(f"Jinja context: {list(context.keys())}")
        # import IPython; IPython.embed()
        raise
    except (jinja2.exceptions.TemplateNotFound,) as exc:
        LOGGER.critical(f"Template exception: {exc}")
        LOGGER.critical(f"User-provided templates: {templates}")
        err = getattr(exc, 'templates', exc.message)
        LOGGER.critical(f"Problem template: {err}")
        import IPython

        IPython.embed()
        raise


@options.output
@options.should_print
@options.option_inplace
@options.option_templates
@click.option('--context', help='context literal.  must be JSON')
@click.option('--context-file', help='context file.  must be JSON')
@click.argument("file", nargs=1)
@tags(
    click_aliases=['jinja'],
)
def jinja_file(
    file: str,
    output: typing.StringMaybe = "",
    should_print: typing.Bool = False,
    in_place: typing.Bool = False,
    context: typing.Dict = {},
    context_file: typing.Dict = {},
    templates: typing.List[str] = ["."],
    strict: bool = True,
) -> str:
    """
    Renders jinja2 file (supports includes, custom filters)
    """
    if isinstance(context, (str,)):
        LOGGER.warning("provided `context` is a string, loading it as JSON")
        context = loads.json(context)

    if context_file:
        assert not context
        context = loadf.json(context_file)

    import sys

    content = jinja_loadf(
        file=file,
        context=context,
        templates=[templates],
        strict=strict,
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


# assign utils back to sibling modules for convenience
# FIXME: is this smart?
loadf.jinja = jinja
loads.jinja = jinja
