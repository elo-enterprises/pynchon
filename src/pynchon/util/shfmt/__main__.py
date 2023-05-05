""" pynchon.util.shfmt.__main__
"""
import pprint

from . import grammar

if __name__ == '__main__':

    import sys;
    cmd=sys.stdin.read()
    result = grammar.bash_fmt(cmd)
    from rich.console import Console
    from rich.syntax import Syntax
    console= Console()
    syntax=Syntax(result,'bash')
    console.print(syntax, )
