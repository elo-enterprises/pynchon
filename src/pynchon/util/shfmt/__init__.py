""" pynchon.util.shfmt
"""
import tatsu
from tatsu.contexts import closure

from .grammar import bashParser


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

    def lparen(self, ast):
        return f'{self._pre}{ast}'

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

    def opts(self, ast):
        def is_lopt(o):
            return o.lstrip().startswith('--')

        first = [o for o in ast if not is_lopt(o)]
        rest = [o for o in ast if is_lopt(o)]
        rest = list(reversed(sorted(rest, key=len)))
        ast = first + rest
        out = []
        for o in ast:
            tmp = " \\" if o != ast[-1] else ""
            out.append(f'\n  {o}{tmp}')
        return out

    def cmd_arg(self, ast):
        return f' {ast}'

    def cmd_args(self, ast):
        return [f'{a}' for a in ast]

    def command(self, ast):
        # import IPython; IPython.embed()
        name, cmd_args, opts = ast
        cmd_args = ''.join(cmd_args)
        opts = ''.join(opts)
        # opts = opts and opts.strip()[:-1]
        # args = '\n  '.join(args)
        tmp = f'{self._pre}{name}{cmd_args} {opts}'
        # tmp = tmp.strip()[:-1] if tmp.strip().endswith('/') else tmp
        return tmp

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
    try:
        return parser.parse(
            text,
            parseinfo=True,
            filename=filename,
            semantics=semantics,
        )
    except (tatsu.exceptions.FailedParse,):
        return text


bash_fmt = fmt
