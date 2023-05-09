r"""@@grammar::bash
@@comments :: /\(\*.*?\*\)/
@@eol_comments :: /#.*?$/
@@whitespace :: /[\t \n \\]/

start = bash_command $;

semi=';'; bash_and = '&&'; bash_bg = '&'; bash_pipe = '|'; bash_or = '||';
backtick = /`(.*)`/; squote = /'(.*)'/; dquote = /"(.*)"/;
qblock = backtick | squote |dquote;

word = /[\/a-zA-Z0-9_:,=.\{\}\(\)]+/;

arg = word | qblock;
cmd_arg=arg;
args = {arg};
cmd_args={cmd_arg};
_shopt = /-[a-zA-Z0-9-_.]+/;
_lopt = /--[a-zA-Z0-9-_.]+/;
shopt = _shopt [args];
lopt = _lopt [args];
opt = shopt|lopt;
opts = {opt};

lparen='('; rparen=')';
joiner = bash_and | bash_bg | bash_or | bash_pipe  | semi ;

command = word cmd_args opts;
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
from tatsu.util import asjson
from tatsu.contexts import closure

src = tatsu.to_python_sourcecode(__doc__)
src = src[: src.rfind('''def main(filename, **kwargs)''')]
exec(src)


def main(text=None, filename=None, **kwargs):
    if not text:
        if not filename or filename == '-':
            text = sys.stdin.read()
        else:
            with open(filename) as f:
                text = f.read()
    parser = bashParser()
    return parser.parse(
        text, parseinfo=True, filename=filename, semantics=semantics, **kwargs
    )
