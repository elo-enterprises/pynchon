""" pynchon.util.shfmt
"""
from rich.syntax import Syntax
from rich.console import Console

from pynchon.util import lme

from .grammar import BashCommand

logger = lme.get_logger(__name__).info


def bash_fmt(text, indent=''):
    """ """
    lopts = []

    def fmt_token(token, indent=''):
        """ """
        result = []
        if isinstance(token, (str,)) and token:
            raise Exception(f'expected token! got {token}')

        tdict = dict(token)
        vals = []
        if 'vals' in tdict:
            vdict = dict(tdict['vals'])
            for v in tdict['vals']:
                if 'quoted_arg' in vdict:
                    vals.append(f"'{v}'")
                else:
                    vals.append(f"{v}")
        if 'argval' in tdict:
            argval = token.argval[0]
            if argval:
                vals += list(argval)
        vals = ' '.join(vals)

        if 'cmd' in tdict:
            cmd_opts = tdict.get('cmd_opts', [])
            cmd_opts = [fmt_token(t, indent='\n') for t in cmd_opts]
            cmd_opts = ' '.join(cmd_opts)
            cmd_args = tdict.get('cmd_args', [])
            cmd_args = [t for t in cmd_args]
            cmd_args = ' '.join(cmd_args)
            return f'{token.joiner and token.joiner[0] or ""} {token.cmd.name} {cmd_opts} {cmd_args}'.lstrip()
        elif 'short_option_name' in tdict:
            if token.short_option_name.startswith('-'):
                lopt = token.short_option_name[1:]
                lopts.append(f'{indent}  --{token.short_option_name} {vals}')
                return ''
            else:
                logger(f'formatting short: {token}')
                return f'{indent}  -{token.short_option_name} {vals}'
        else:
            logger(f'dont know how to fmt {[token,tdict]}')
            return ''

    parsed = BashCommand().parseString(text.lstrip())
    msg = list(enumerate(list(parsed)))
    logger('parsed:\n\n{msg}')
    result = [fmt_token(token, indent=indent) for token in parsed]
    result = '\n'.join(result).lstrip()
    result += ''.join([x for x in reversed(sorted(lopts, key=len))])
    return result


def bash_fmt_display(*args, **kwargs):
    """ """
    console = kwargs.pop('console', None) or Console(stderr=True)
    result = bash_fmt(*args, **kwargs)
    syntax = Syntax(result, 'bash', line_numbers=True)
    return console.print(syntax)
