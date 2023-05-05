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
CommandJoiner = Literal('&&')
CommandJoiner|= Literal('||')
CommandJoiner|= Literal(';')
CommandJoiner|= pyparsing.LineStart()
CommandJoiner=Optional(Continuation)+CommandJoiner
# CommandJoiner|=pyparsing.LineStart()
CommandJoiner = CommandJoiner.setResultsName('joiner')

Name = Word(alphanums)

Arg = Name('argval') + Optional(Continuation)
Arg = Arg('argval')
Vals = Group(ZeroOrMore(Arg | QArg('quoted_arg')))

Option = Literal("-").suppress() + Name('short_option_name')
Option = Group(Option + Vals('vals'))
LongOption = Literal("--").suppress() + Name('long_option_name')
LongOption = Group(LongOption + Vals('vals'))
Options = ZeroOrMore(Option | LongOption)

CommandName = Name('name')
Command = Combine(CommandName)('cmd')
Command+= Optional(Options('cmd_opts'))
Command+= Optional(Vals('cmd_args'))

JoinedCommand = ZeroOrMore(Group(CommandJoiner + Command)('cmd'))
#
# BashCommand = Command('cmd').set_results_name('cmd')
# BashCommand+= Optional(JoinedCommand)

BashCommand=JoinedCommand
def fmt_token(token, indent=''):
    """ """
    result = []
    if isinstance(token, (str,)) and token:
        raise Exception(f'expected token! got {token}')

    tdict = dict(token)
    vals=[]
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
            vals+=list(argval)
    vals = ' '.join(vals)

    if 'cmd' in tdict:
        cmd_opts = tdict.get('cmd_opts',[])
        cmd_opts = [fmt_token(t,indent='\n') for t in cmd_opts]
        cmd_opts = ' '.join(cmd_opts)
        cmd_args = tdict.get('cmd_args',[])
        cmd_args = [t for t in cmd_args]
        cmd_args = ' '.join(cmd_args)
        return f'{token.joiner and token.joiner[0] or ""} {token.cmd.name} {cmd_opts} {cmd_args}'.lstrip()
    elif 'long_option_name' in tdict:
        return f'{indent}  --{token.long_option_name} {vals}'
    elif 'short_option_name' in tdict:
        return f'{indent}  -{token.short_option_name} {vals}'
    else:
        logger(f'dont know how to fmt {[token,tdict]}')
        return ''

def bash_fmt(text, indent=''):
    """ """
    text=text.lstrip()
    # print(f'parsing:\n\n{text}\n\n')
    parsed = BashCommand().parseString(text)
    # print(f'parsed:\n\n')
    # import pprint
    # pprint.pprint(list(enumerate(list(parsed))))

    result = [ fmt_token(token, indent=indent) for token in parsed]
    result = '\n'.join(result).lstrip()
    return result
