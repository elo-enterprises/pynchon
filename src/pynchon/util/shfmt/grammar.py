""" pynchon.util.shfmt.grammar
"""
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

continuation = ('\\' + LineEnd()).suppress()
Name = Word(alphanums)
# Name.set_results_name('Name')
Arg = Name + Optional(continuation)

def QString(s, loc, tokens):  # noqa
    """Parse out the multiline quoted string"""
    text = Word(alphanums + '-') + Optional(continuation)
    g = Combine(ZeroOrMore(text), adjacent=False, joinString=" ")
    return g.parseString(tokens[0])

QArg = QuotedString("\'", multiline=True)
QArg.setParseAction(QString)

Vals = Group(ZeroOrMore(Arg | QArg))
Option = Literal("-").suppress() + Group(Name('short_option_name') + Vals)
LongOption = Literal("--").suppress() + Group(Name('long_option_name') + Vals)
Command = Name + ZeroOrMore(Option | LongOption)
BashCommand = (
    Command
    + ZeroOrMore(Literal('&&') + Command)
    + ZeroOrMore(Literal('||') + Command)
    # + ZeroOrMore(Literal(';') + Command)
)
