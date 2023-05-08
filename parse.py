r"""@@grammar::bash
@@comments :: /\(\*.*?\*\)/
@@eol_comments :: /#.*?$/
@@whitespace :: /[\t \n \\]/

start = bash_command $;

word = /[\/a-zA-Z0-9_:,=.\{\}\(\)]+/;
backtick = /`(.*)`/;
squote = /'(.*)'/;
dquote = /"(.*)"/;
qblock = backtick | squote |dquote;

arg = word | qblock;
args = {arg};

shopt = /-[a-zA-Z0-9-_]+/;
lopt = /--[a-zA-Z0-9-_]+/;
opt = (shopt|lopt) [args];
opts = {opt};


bash_and = '&&';
bash_bg = '&';
bash_pipe = '|';
bash_or = '||';
semi=';';
lparen='('; rparen=')';
joiner = bash_and | bash_bg | bash_or | bash_pipe  | semi ;

command = word args opts;
subproc = lparen command rparen;
compound_command =
    | command joiner compound_command
    | subproc joiner compound_command
    | subproc
    | command
    ;

pipeline_command =
  compound_command
  | compound_command joiner compound_command
  ;

bash_command = pipeline_command;
"""
import json
import tatsu
from tatsu.contexts import closure
from tatsu.util import asjson

src = tatsu.to_python_sourcecode(__doc__)
src = src[:src.rfind('''def main(filename, **kwargs)''')]
exec(src)

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

    @append_record
    def lparen(self, ast):
        return f'{self._pre}{ast}'

    @append_record
    def rparen(self, ast):
        return ast

    @append_record
    def joiner(self,ast):
        self._joiner = ast
        return ''
    def backtick(self,ast):
        return f"`{ast}`"
    def squote(self,ast):
        return f"'{ast}'"
    def dquote(self,ast):
        return f'"{ast}"'

    # @append_record
    # def backtick(self, ast):
    #     tmp=" ".join(ast)
    #     import IPython; IPython.embed()
    #     return f'`{tmp}`'

    def indent(self,text):
        return '\n'.join([self.indention+x for x in text.split('\n')])

    def subproc(self, ast):
        lparen, command, rparen=ast
        command = self.indent(command)
        return f"(\n{command}\n)"

    def qblock(self, ast):
        # q1,content,q2=ast
        # return f"{q1}{content}{q2}"
        # import IPython; IPython.embed()
        return f"{ast}"

    def arg(self, ast):
        return ast

    @append_record
    def command(self, ast):
        name, opts, args = ast
        opts='\n  '.join(opts)
        args='\n  '.join(args)
        return f'{self._pre}{name} {opts} {args}'

    def opt(self, ast):
        option, vals = ast
        tmp=''
        if isinstance(vals, (closure,)):
            for c in vals:
                tmp+=str(c)
        elif isinstance(vals,(str,)):
            tmp=vals
        else:
            assert type(vals)=='bonk',type(vals)
        return f"{option} {tmp}"

def main(filename, **kwargs):
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = bashParser()
    return parser.parse(
        text, parseinfo=True,
        filename=filename,
        semantics=semantics,
        **kwargs)
semantics=Semantics()
if __name__ == '__main__':
    ast = generic_main(main, bashParser, name='bash')
    data = asjson(ast)
    # print(json.dumps(data, indent=2))
    print('-'*50)
    rec=semantics.record
    for cmd in rec:
        if cmd:
            print(cmd)
