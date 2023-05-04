cmd = r"""shellcmd -arg1 val1 --arg2 val2 \
-arg3 val3 \
-arg4 'quoted \
    line-continued \
    string \
' && echo -n1 hello world \
|| bonk one"""

from pyparsing import *


def eat(parsed, level=0):
    for token in parsed:
        if isinstance(token, (str,)):
            print(level * ' ' + token)
        else:
            try:
                a, v = token
                # raise Exception()
            except:
                import IPython

                IPython.embed()
            v = ' '.join(v)
            if token.getName() == 'long_option_name':
                pre = '--'
            else:
                pre = '-'

            print(f'  {pre}{a} "{v}"')


def get_grammar():
    continuation = ('\\' + LineEnd()).suppress()
    name = Word(alphanums)
    name.set_results_name('name')
    # Parse out the multiline quoted string
    def QString(s, loc, tokens):
        text = Word(alphanums + '-') + Optional(continuation)
        g = Combine(ZeroOrMore(text), adjacent=False, joinString=" ")
        return g.parseString(tokens[0])

    arg = name + Optional(continuation)
    qarg = QuotedString("\'", multiline=True)
    qarg.set_results_name('QuotedString')
    qarg.setParseAction(QString)

    vals = Group(ZeroOrMore(arg | qarg))
    option = Literal("-").suppress() + Group(name('short_option_name') + vals)
    loption = Literal("--").suppress() + Group(name('long_option_name') + vals)
    command = name + ZeroOrMore(option | loption)
    grammar = (
        command
        + ZeroOrMore(Literal('&&') + command)
        + ZeroOrMore(Literal('||') + command)
    )
    return grammar


if __name__ == '__main__':
    tmp = get_grammar().parseString(cmd)
    eat(tmp)
