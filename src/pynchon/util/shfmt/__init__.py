""" pynchon.util.shfmt
"""
from pynchon.util import lme

from .grammar import BashCommand

logger = lme.get_logger(__name__).info


def bash_fmt(text, indent='', joiners='| || && > < ;'.split(), logger=logger):
    """ """
    # NB: aggregated until end, since sorting here seems safe
    lopts = []

    def fmt_token(token, indent=''):
        """ """
        result = []
        if isinstance(token, (str,)) and token:
            # if token in joiners:
            #     return f'{token}'

            raise Exception(f'expected token! got {token}')

        tdict = dict(token)
        vals = []
        if 'name' in tdict:
            return token.name

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
                vals += [f"{indent}  {argval}"]

        max_len = max([len(x) for x in vals]) if vals else 0
        joiner = ' ' if max_len < 10 else '\n    '
        vals = joiner.join(vals)

        if 'cmd' in tdict:
            cmd_opts = tdict.get('cmd_opts', [])
            cmd_opts = [fmt_token(t, indent='\n') for t in cmd_opts]
            cmd_opts = ' '.join(cmd_opts)
            cmd_args = tdict.get('cmd_args', [])
            cmd_args = [t for t in cmd_args]
            # if cmd_args:
            #     raise Exception(cmd_args)
            joiner = ' '
            cmd_args = joiner.join(cmd_args)
            redir = f'\n  {" ".join(token.file)}' if token.redir else ''
            return f'{token.joiner and token.joiner[0] or ""} {token.cmd.name} {cmd_opts} {cmd_args}{redir}'.lstrip()
        elif 'short_option_name' in tdict:
            if token.short_option_name.startswith('-'):
                lopt = token.short_option_name[1:]
                lopts.append(f'{indent}  --{token.short_option_name} {vals}')
                return ''
            else:
                logger(f'formatting short: {token}')
                return f'{indent}  -{token.short_option_name} {vals}'

        return vals

    parsed = BashCommand().parseString(text.lstrip())
    msg = list(enumerate(list(parsed)))
    logger(f'parsed:\n\n{msg}')
    result = [fmt_token(token, indent=indent) for token in parsed]
    result = '\n'.join(result).lstrip()
    result += ''.join([x for x in reversed(sorted(lopts, key=len))])
    return result
