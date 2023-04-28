""" pynchon.util.text.render CLI
"""
from pynchon import click
from pynchon.cli import options
from pynchon.util import text, typing, lme

LOGGER = lme.get_logger(__name__)
from pynchon.util.os import invoke

from . import jinja


@click.group('render')
def entry() -> typing.NoneType:
    pass


entry.__doc__ = __doc__ or ""


@options.option_output
@options.option_print
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
        result = text.load_json5(content=result)
        result = text.to_json(result)
    msg = result
    print(msg, file=open(output, 'w'))
    if should_print and output != '/dev/stdout':
        print(msg)


entry.command()(j2cli)
entry.command('j2')(j2cli)
entry.command()(jinja)
entry.command('j')(jinja)

if __name__ == '__main__':
    entry()
