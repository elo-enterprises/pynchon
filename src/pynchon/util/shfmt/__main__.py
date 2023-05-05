""" pynchon.util.shfmt.__main__
"""
from . import grammar


def fmt_token(token,level=0):
    result = []
    if isinstance(token, (str,)):
        return level * ' ' + token
    else:
        a, v = token
        v = ' '.join(v)
        if token.getName() == 'long_option_name':
            pre = '--'
        else:
            pre = '-'
        return f'  {pre}{a} "{v}"'

def fmt(parsed, level=0):
    """
    """
    result = [
        fmt_token(token,level=level) for token in parsed
    ]
    return '\n'.join(result)


if __name__ == '__main__':
    cmd = r"""shellcmd -arg1 val1 --arg2 val2 \
    -arg3 val3 \
    -arg4 'quoted \
        line-continued \
        string \
    ' && echo -n1 hello world \
    || bonk one || echo foo"""
    print(f'parsing:\n\n{cmd}\n\n')
    tmp = grammar.BashCommand().parseString(cmd)
    print(fmt(tmp))
