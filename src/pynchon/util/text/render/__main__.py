""" pynchon.util.text.render CLI
"""
from pynchon import click
from pynchon.cli import options


@click.group('render')
def entry() -> None:
    """
    pynchon.util.text.render CLI
    """

@options.option_output
@options.option_print
@click.option('--context', help='context file.  must be JSON')
@click.argument("file", nargs=1)
def j2cli(
    output: str, should_print: bool, file: str, context: str, format: str = 'json'
) -> None:
    """
    Renders the named file, using the given context-file.
    This is a wrapper on `j2`, so j2cli must be installed.
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

if __name__=='__main__':
    entry()
