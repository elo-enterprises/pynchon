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
    hello world' zonk \
    || bonk one \
    || zoooom
    """
    print(f'parsing:\n\n{cmd}\n\n')
    tmp = grammar.BashCommand().parseString(cmd)
    print(f'parsed:\n\n')
    pprint.pprint(list(tmp))
    print()
    print()
    print(f'flattened:\n\n')
    tmp2 = [
        item
        for sublist in [x for x in tmp if not isinstance(x, (str,))]
        for item in sublist
    ]
    pprint.pprint(list(tmp2))
    print()
    print()
    tmp = grammar.bash_fmt(tmp)
    print(f'formatted:\n\n{tmp}\n\n')
