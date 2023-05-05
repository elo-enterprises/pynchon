""" pynchon.util.shfmt.__main__
"""
import pprint

from . import grammar

if __name__ == '__main__':
    cmd = r"""shellcmd -arg1 val1 --arg2 val2 \
    -arg3 val3 \
    -arg4 'quoted \
        line-continued \
        string \
    ' && echo -n1 '\
    hello world' \
    || bonk one \
    ; zoooom
    """
    result = grammar.bash_fmt(cmd)
    from rich.console import Console
    from rich.syntax import Syntax
    console= Console()
    syntax=Syntax(result,'bash')
    console.print(syntax, )
