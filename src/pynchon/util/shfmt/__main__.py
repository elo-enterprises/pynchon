""" pynchon.util.shfmt.__main__
"""
from rich.syntax import Syntax

from pynchon import cli
from pynchon.util import lme

from . import fmt

LOGGER = lme.get_logger(__name__)


@cli.click.argument(
    'filename',
)
@cli.click.command
def entry(filename: str = '/dev/stdin'):
    """

    :param filename: str:  (Default value = '/dev/stdin')
    :param filename: str:  (Default value = '/dev/stdin')

    """
    LOGGER.debug(f'reading from file: {filename}')
    if filename == '-':
        filename = '/dev/stdin'
    with open(filename, 'r') as fhandle:
        text = fhandle.read()
    lme.CONSOLE.print(
        Syntax(
            fmt(text, filename=filename),
            'bash',
            word_wrap=True,
        )
    )


if __name__ == '__main__':
    entry()
