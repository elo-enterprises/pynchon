""" pynchon.util.shfmt.__main__
"""
import sys

from pynchon.util import lme

LOGGER = lme.get_logger(__name__)
if __name__ == '__main__':
    from . import *

    cmd = sys.argv[-1]
    result = bash_fmt(cmd, logger=LOGGER.critical)
    from rich.syntax import Syntax

    lme.CONSOLE.print(Syntax(result, 'bash'))
