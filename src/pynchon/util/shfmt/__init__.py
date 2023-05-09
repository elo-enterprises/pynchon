""" pynchon.util.shfmt
"""
from tatsu.contexts import closure

from .grammar import generic_main, asjson, main, bashParser


def append_record(fxn):
    def newf(self, *args, **kargs):
        result = fxn(self, *args, **kargs)
        self.record.append(result)
        return result

    return newf


class Semantics:
    """
    a value, for simple elements such as token, pattern, or constant
    a tuple, for closures, gatherings, and the right-hand-side of rules with more than one element but without named elements
    a dict-derived object (AST) that contains one item for every named element in the grammar rule, with items can be accessed through the standard dict syntax (ast['key']), or as attributes (ast.key).
    """

    def __init__(self):
        self.record = []
        self._joiner = None
        self.indention = '  '

    @property
    def _indent(self):
        return f'  '

    @property
    def _pre(self):
        pre = f'{self._joiner} ' if self._joiner else ''
        self._joiner = None
        return pre

    def backtick(self, ast):
        return f"`{ast}`"

    def squote(self, ast):
        return f"'{ast}'"

    def dquote(self, ast):
        return f'"{ast}"'

    # @append_record
    def lparen(self, ast):
        return f'{self._pre}{ast}'

    # @append_record
    # def rparen(self, ast):
    #     return ast

    @append_record
    def joiner(self, ast):
        self._joiner = ast
        return ''

    def indent(self, text):
        return text  # '\n'.join([self.indention + x for x in text.split('\n')])

    def subproc(self, ast):
        lparen, command, rparen = ast
        command = self.indent(command)
        return f"(\n{command}\n)"

    def qblock(self, ast):
        return f"{ast}"

    # def arg(self, ast):
    #     return ast

    def opts(self, ast):
        def is_lopt(o):
            return o.lstrip().startswith('--')

        first = [o for o in ast if not is_lopt(o)]
        rest = [o for o in ast if is_lopt(o)]
        rest = list(reversed(sorted(rest, key=len)))
        ast = first + rest
        return [f'\n  {o}' for o in ast]

    @append_record
    def command(self, ast):
        # import IPython; IPython.embed()
        name, opts, args = ast
        args = ''.join(args)
        opts = ''.join(opts)
        # args = '\n  '.join(args)
        return f'{self._pre}{name} {args} {opts}'

    def opt(self, ast):
        option, vals = ast
        tmp = ''
        if isinstance(vals, (closure,)):
            for c in vals:
                tmp += f' {c}'
        elif isinstance(vals, (str,)):
            tmp = vals
        else:
            assert type(vals) == 'bonk', type(vals)
        return f"{option}{tmp}"


def fmt(text, filename='?'):
    semantics = Semantics()
    parser = bashParser()
    return parser.parse(
        text,
        parseinfo=True,
        filename=filename,
        semantics=semantics,
    )


bash_fmt = fmt
