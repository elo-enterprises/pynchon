"""
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
CommandJoiner |= Literal('||')
CommandJoiner |= Literal(';')
CommandJoiner |= pyparsing.LineStart()
CommandJoiner = Optional(Continuation) + CommandJoiner
# CommandJoiner|=pyparsing.LineStart()
CommandJoiner = CommandJoiner.setResultsName('joiner')

Name = Word(alphanums + "./")  # +pyparsing.White()

Arg = Word(alphanums + "./-_")('argval') + Optional(Continuation)
Arg = Arg('argval')
Vals = Group(ZeroOrMore(Arg | QArg('quoted_arg')))

# Option = Literal("-").suppress() + Word(alphanums+".-")
# Option =
LOption = Group(
    Literal("--").suppress()
    + Word(alphanums + ".-")('long_option_name')
    + Optional(Vals('vals'))
)
Option = Group(
    Literal("-").suppress()
    + Word(alphanums + ".-")('short_option_name')
    + Optional(Vals('vals'))
)
Options = ZeroOrMore(Option)
LOptions = ZeroOrMore(LOption)
# LongOption = Literal("--").suppress() + Name('long_option_name')
# LongOption = Group(LongOption + Optional(Vals('vals')))
# LongOptions = ZeroOrMore(LongOption)

CommandName = Name('name')
Command = Combine(CommandName)('cmd')
Command += Optional(LOptions('cmd_lopts') + Options('cmd_opts'))
# Command+= Optional(LongOptions('cmd_lopts'))
Command += Optional(Vals('cmd_args'))
RedirCommand = Literal('>').setResultsName('redir') + Word(alphanums + "./-_")('file')
Command += Optional(RedirCommand)('file')
# Command = Command |
PipedCommand = ZeroOrMore(Group(Literal('|').setResultsName('joiner') + Command))
JoinedCommand = ZeroOrMore(Group(CommandJoiner + Command)('cmd'))

#
# BashCommand = Command('cmd').set_results_name('cmd')
# BashCommand+= Optional(JoinedCommand)

BashCommand = Command + (PipedCommand | RedirCommand | JoinedCommand)
