""" pynchon.util.shfmt.grammar
"""
from pynchon.util import lme

logger = lme.get_logger(__name__).critical
import pyparsing
from pyparsing import (
    LineEnd,
    Word,
    Combine,
    ZeroOrMore,
    Group,
    Literal,
    Optional,
    alphanums,
    QuotedString,
)

def QString(s, loc, tokens):  # noqa
    """Parse out the multiline quoted string"""
    text = Word(alphanums + '-')
    text |= Word(alphanums + '-\\').suppress()
    text = (text) + Optional(Continuation)
    g = Combine(ZeroOrMore(text), adjacent=False, joinString=" ")
    return g.parseString(tokens[0])
QArg = QuotedString("\'", multiline=True) | QuotedString('\"', multiline=True)
QArg.setParseAction(QString)

Continuation = ('\\' + (LineEnd())).suppress()
CommandJoiner = (Literal('&&') | Literal('||') | Literal(';')).setResultsName('joiner')
Name = Word(alphanums)

Arg = Name('argval') + Optional(Continuation)
Arg = Arg('argval')
Vals = Group(ZeroOrMore(Arg | QArg('quoted_arg')))

Option = Literal("-").suppress() + Name('short_option_name')
Option = Group(Option+ Vals('vals'))
LongOption = Literal("--").suppress() + Name('long_option_name')
LongOption = Group(LongOption+ Vals('vals'))
Options = ZeroOrMore(Option | LongOption)

CommandName = Name('name')
Command = Combine(CommandName)('cmd')
Command+= Options('cmd_opts')

JoinedCommand = ZeroOrMore(Group(CommandJoiner + Command)('cmd'))('tail')
# JoinedCommand = Group(JoinedCommand)

BashCommand = Command('cmd').set_results_name('cmd')
BashCommand+= Optional(JoinedCommand)


def fmt_token(token, level=0):
    """ """
    result = []
    if isinstance(token, (str,)):
        raise Exception(f'expected token! got {token}')
    else:
        tdict = dict(token)
        if 'vals' not in tdict:
            vals = ''
        else:
            vals = []
            vdict = dict(tdict['vals'])
            for v in tdict['vals']:
                if 'quoted_arg' in vdict:
                    vals.append(f"'{v}'")
                else:
                    vals.append(f"{v}")
            vals = ' '.join(vals)
    if 'name' in tdict:
        return token.name
    if 'long_option_name' in tdict:
        return f' --{token.long_option_name} {vals}'
    elif 'short_option_name' in tdict:
        pre = '-'
        return f' -{token.short_option_name} {vals}'
    elif 'cmd' in tdict:
        cmd_opts = tdict.get('cmd_opts',[])
        cmd_opts = [fmt_token(t) for t in cmd_opts]
        cmd_opts = ' '.join(cmd_opts)
        return f'{token.joiner} {token.cmd.name} {cmd_opts}'
    else:
        raise Exception(f'dont know how to fmt {tdict}')


def bash_fmt(parsed, level=0):
    """ """
    result = [ fmt_token(token, level=level) for token in parsed]
    return '\n'.join(result)
