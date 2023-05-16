""" pynchon.shfmt
"""
import tatsu
from tatsu.contexts import closure

from .grammar import bashParser


class Semantics:
    """a value, for simple elements such as token, pattern, or constant
    a tuple, for closures, gatherings, and the right-hand-side of rules with more than one element but without named elements
    a dict-derived object (AST) that contains one item for every named element in the grammar rule, with items can be accessed through the standard dict syntax (ast['key']), or as attributes (ast.key).


    """

    def __init__(self):
        self.record = []
        self._joiner = None
        self.indention = "  "

    @property
    def _pre(self):
        pre = f"{self._joiner} " if self._joiner else ""
        self._joiner = None
        return pre

    def backtick(self, ast):
        return f"`{ast}`"

    def squote(self, ast):
        # raise Exception()
        ast = f"{ast}"
        if len(ast) > 12:
            ast = "\n".join([f"{a} \\" for a in ast.split(" ")])
        return f"'{ast}'"

    def dquote(self, ast):
        return f'"{ast}"'

    def redir(self, ast):
        return f"{ast}"

    def lparen(self, ast):
        return f"{self._pre}{ast}"

    def joiner(self, ast):
        self._joiner = ast
        return ""

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
            return o.lstrip().startswith("--")

        first = [o for o in ast if not is_lopt(o)]
        rest = [o for o in ast if is_lopt(o)]
        rest = list(reversed(sorted(rest, key=len)))
        ast = first + rest
        out = []
        for o in ast:
            tmp = " \\" if o != ast[-1] else ""
            out.append(f"\n  {o}{tmp}")
        return out

    def cmd_arg(self, ast):
        return f" {ast}"

    def path(self, ast):
        out = []
        for p in ast:
            out.append(p if isinstance(p, (str,)) else "".join(p))
        return "".join(out)

    def cmd_args(self, ast):
        return [f"{a}" for a in ast]

    def compound_command(self, ast):
        ast = list(ast)
        print(f"compound {ast}")
        first = ast.pop(0)
        joiner = ast.pop(0)
        rest = ast.pop(0)
        ast = "".join(ast)
        # if 'printf' in str(ast):
        #     import IPython; IPython.embed()
        # joiner=joiner and str(joiner).strip()
        # joiner=joiner or ''
        # joiner=joiner.strip()
        # joiner=joiner and f'\n  {joiner}'
        ast = "".join(ast) if ast else ""
        return f"{first}\n{joiner}\n{rest}"

    def anything(self, ast):
        # print(f'anythin {ast}')
        return ast

    def command(self, ast):
        # print(f'command {ast}')
        # if 'printf' in str(ast):
        #     import IPython; IPython.embed()
        return ast

    def python_command(self, ast):
        # print(f'python {ast}')
        # print( ast )
        ast = list(ast)
        python = ast.pop(0)
        shopt = ast.pop(0)
        subs = ast.pop(0)
        subs = "  " + " ".join(subs)
        args = ast.pop(0)
        args = "".join([f"  {a}" for a in args])
        careful_opts = ast.pop(0)
        opts = "".join(careful_opts)
        opts = "  " + opts.lstrip()
        ast = "".join(ast)
        tmp = f"{python.upper()} {shopt} \\\n{subs} \\\n{args} \\\n{opts}\n{ast}"
        return tmp.strip()

    # def redirect_command(self,ast):
    #     import IPython; IPython.embed()#return ' '.join(ast)
    def docker_tag(self, ast):
        return "".join(ast)

    def docker_command(self, ast):
        ast = list(ast)
        docker = ast.pop(0)
        sub = ast.pop(0)
        opts = ast.pop(0)
        epoint = [x for x in opts if x.lstrip().startswith("--entrypoint")]
        epoint = epoint and epoint[0]
        epoint = epoint or ""
        epoint and opts.remove(epoint)
        workspace = [x for x in opts if "workspace" in x]
        [opts.remove(x) for x in workspace]
        workspace = " ".join(workspace).strip()
        opts = [workspace] + opts
        opts = "\n".join([f"  {o}" for o in opts])
        img = ast.pop(0)
        rest = ast.pop(0)
        ast and print(f"got extra: {ast}")
        return f"{docker.upper()} {sub} {epoint}\n{opts}\n  {img}\n    {rest}"

    def simple_command(self, ast):
        # print(f'simple {ast}')
        if isinstance(ast, (str,)):
            return ast
        name, cmd_args, opts = ast
        cmd_args = "".join(cmd_args)
        opts = "".join(opts)
        tmp = f"{self._pre}{name}{cmd_args} {opts}"
        return tmp

    def careful_opt(self, ast):
        try:
            option, vals = ast
        except:
            option, vals = str(ast), []
        tmp = ""
        if isinstance(vals, (closure,)):
            for c in vals:
                tmp += f" {c}"
        elif isinstance(vals, (str,)):
            tmp = vals
        elif isinstance(
            vals,
            (
                tuple,
                list,
            ),
        ):
            tmp = "".join(vals)
        else:
            assert type(vals) == "bonk", type(vals)
        return f"{option} {tmp}"

    def opt(self, ast):
        option, vals = ast
        tmp = ""
        if isinstance(vals, (closure,)):
            for c in vals:
                tmp += f" {c}"
        elif isinstance(vals, (str,)):
            tmp = vals
        else:
            assert type(vals) == "bonk", type(vals)
        return f"{option}{tmp}"


class Semantics:
    def word(self, ast):
        print(f"word: {ast}")
        return ast

    def simple_command(self, ast):
        print(f"simple_command: {ast}")
        tail = ast
        biggest=''
        for i,l in enumerate(tail):
            if len(l)>len(biggest):
                biggest=l
        result = []
        skip_next=False
        for i,l in enumerate(tail):
            if skip_next:
                skip_next=False
                continue
            try:
                n=tail[i+1]
            except:
                n=''
                # print(f'looking at {[i,l,n]}')
            comb=f'{l} {n}'
            if len(comb)<len(biggest):
                result.append(comb)
                skip_next=True
            else:
                result.append(l)
        # import IPython; IPython.embed()
        return '\n  '.join(result)

    def shell_command(self, ast):
        print(f"shell_command: {ast}")
        return ast

    def path(self, ast):
        print(f"path: {ast}")
        # if '/' in ast:
        return ast

    def pipeline_command(self, ast):
        print(f"pipeline_command: {ast}")
        return ast

    def word_list(self, ast):
        print(f"word_list: {ast}")
        return ast

    def opt(self, ast):
        print(f"opt: {ast}")
        return ast if isinstance(ast,(str,)) else ' '.join(ast)

    def opt_val(self, ast):
        print(f"opt_val: {ast}")
        return ast

    def subcommands(self, ast):
        print(f"subcommands: {ast}")
        return ' '.join(ast)

    def drilldown(self,ast):
        print(f"drilldown: {ast}")
        return ast

    def entry(self, ast):
        print(f"entry: {ast}")
        return str(ast)

def fmt(text, filename="?"):
    semantics = Semantics()
    parser = bashParser()
    try:
        parsed = parser.parse(
            text,
            parseinfo=True,
            filename=filename,
            semantics=semantics,
        )
    except (tatsu.exceptions.FailedParse,):
        return text
    else:
        out = []
        for item in parsed:
            if isinstance(item, (list,tuple)):
                item=' '.join([str(x) for x in item])
            out.append(item)
        head=out.pop(0)
        # tail=out.copy()
        tail='\n  '.join(out)
        return f"{head} {tail}"


bash_fmt = fmt
