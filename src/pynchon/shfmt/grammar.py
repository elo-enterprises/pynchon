
""" pynchon.shfmt.grammar
"""
r"""@@grammar::bash
@@comments :: /\(\*.*?\*\)/
@@eol_comments :: /#.*?$/
@@whitespace :: /[\t \n \\]/

start = bash_command $;

semi=';'; bash_and = '&&'; bash_bg = '&'; Bash_pipe = /[|]/; bash_or = '||';
backtick = /`(.*)`/; squote = /'(.*)'/; dquote = /"(.*)"/;
qblock = backtick | squote |dquote;

word = /[a-zA-Z0-9_:,=.\{\}\(\)]+/;
PATH_SEP = /\//;
path = {PATH_SEP word}+ | word;
arg  = word | qblock | path;
map_arg = arg COL arg;
busy_arg = map_arg|arg;
COL= /[:]/;
cmd_arg=arg;
args = {arg};
cmd_args={cmd_arg};
_shopt = /-[a-zA-Z0-9-_.]+/;
_lopt = /--[a-zA-Z0-9-_.]+/;
shopt = _shopt [args];
lopt = _lopt [args];
careful_opt = (_lopt|_shopt) [busy_arg];
careful_opts = {careful_opt}+;
opt = shopt|lopt;
opts = {opt};
DASH=/-/;
lparen='('; rparen=')';
Redir=/[>]/;
joiner = bash_and | bash_bg | bash_or | Bash_pipe  | semi | Redir;

simple_command = word cmd_args opts;
command = docker_command | python_command | simple_command ;
redirect_command = command '>' path;
subcommand=word;
subcommands = {subcommand};
anything=/(^[ >|]*)/;
greed=/^[\w]*/;
#docker_tag = &/((^[:])*[:](^[:])*)/ ~ greed;
docker_tag = /[a-zA-Z0-9_]+[\/:][a-zA-Z0-9_]+/;
docker_command = 'docker' subcommand careful_opts docker_tag anything;
python_command = 'python' _shopt subcommands args opts anything;
subproc = lparen command rparen;

compound_command =
  | command '>' (path|word)
  | command joiner command
  | command joiner compound_command
  | subproc joiner compound_command
  | subproc {} {}
  | command {} {}
  ;
#
# pipeline_command =
#   compound_command
#   | compound_command joiner compound_command
#   ;

bash_command = compound_command;
"""

# """
# 1) generates parser-code from the grammar in this file
# 2) prune the generated source-code text:
#      we only want the source for the parsers
# 3) exec the generated source-code to create the
#      parser-classes / inject them into this namespace
# """
import tatsu
src = tatsu.to_python_sourcecode(__doc__)
src = src[: src.rfind("""def main(filename, **kwargs)""")]
# print(src)
# tmp=locals().copy()
exec(src)
