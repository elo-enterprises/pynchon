""" pynchon.shfmt
"""
import json

import tatsu

from pynchon import abcs
from pynchon.util import lme, tagging, typing  # noqa
from pynchon.util.text import loads

from .grammar import bashParser

#     def backtick(self, ast):
#         return f"`{ast}`"
#
#     def squote(self, ast):
#         # raise Exception()
#         ast = f"{ast}"
#         if len(ast) > 12:
#             ast = "\n".join([f"{a} \\" for a in ast.split(" ")])
#         return f"'{ast}'"
#
#     def opts(self, ast):
#         def is_lopt(o):
#             return o.lstrip().startswith("--")
#
#         first = [o for o in ast if not is_lopt(o)]
#         rest = [o for o in ast if is_lopt(o)]
#         rest = list(reversed(sorted(rest, key=len)))
#         ast = first + rest
#         out = []
#         for o in ast:
#             tmp = " \\" if o != ast[-1] else ""
#             out.append(f"\n  {o}{tmp}")
#         return out
#
#     def cmd_arg(self, ast):
#         return f" {ast}"
#
#     def path(self, ast):
#         out = []
#         for p in ast:
#             out.append(p if isinstance(p, (str,)) else "".join(p))
#         return "".join(out)
#
#     def cmd_args(self, ast):
#         return [f"{a}" for a in ast]
#
#     def compound_command(self, ast):
#         ast = list(ast)
#         LOGGER.warning(f"compound {ast}")
#         first = ast.pop(0)
#         joiner = ast.pop(0)
#         rest = ast.pop(0)
#         ast = "".join(ast)
#         # if 'printf' in str(ast):
#         #     import IPython; IPython.embed()
#         # joiner=joiner and str(joiner).strip()
#         # joiner=joiner or ''
#         # joiner=joiner.strip()
#         # joiner=joiner and f'\n  {joiner}'
#         ast = "".join(ast) if ast else ""
#         return f"{first}\n{joiner}\n{rest}"
#
#     def command(self, ast):
#         # if 'printf' in str(ast):
#         #     import IPython; IPython.embed()
#         return ast
#
#     def python_command(self, ast):
#         # LOGGER.warning( ast )
#         ast = list(ast)
#         python = ast.pop(0)
#         shopt = ast.pop(0)
#         subs = ast.pop(0)
#         subs = "  " + " ".join(subs)
#         args = ast.pop(0)
#         args = "".join([f"  {a}" for a in args])
#         careful_opts = ast.pop(0)
#         opts = "".join(careful_opts)
#         opts = "  " + opts.lstrip()
#         ast = "".join(ast)
#         tmp = f"{python.upper()} {shopt} \\\n{subs} \\\n{args} \\\n{opts}\n{ast}"
#         return tmp.strip()
#
#     def docker_tag(self, ast):
#         return "".join(ast)
#
#     def docker_command(self, ast):
#         ast = list(ast)
#         docker = ast.pop(0)
#         sub = ast.pop(0)
#         opts = ast.pop(0)
#         epoint = [x for x in opts if x.lstrip().startswith("--entrypoint")]
#         epoint = epoint and epoint[0]
#         epoint = epoint or ""
#         epoint and opts.remove(epoint)
#         workspace = [x for x in opts if "workspace" in x]
#         [opts.remove(x) for x in workspace]
#         workspace = " ".join(workspace).strip()
#         opts = [workspace] + opts
#         opts = "\n".join([f"  {o}" for o in opts])
#         img = ast.pop(0)
#         rest = ast.pop(0)
#         ast and LOGGER.warning(f"got extra: {ast}")
#         return f"{docker.upper()} {sub} {epoint}\n{opts}\n  {img}\n    {rest}"
#
#     def simple_command(self, ast):
#         if isinstance(ast, (str,)):
#             return ast
#         name, cmd_args, opts = ast
#         cmd_args = "".join(cmd_args)
#         opts = "".join(opts)
#         tmp = f"{self._pre}{name}{cmd_args} {opts}"
#         return tmp
#
#     def opt(self, ast):
#         option, vals = ast
#         tmp = ""
#         if isinstance(vals, (closure,)):
#             for c in vals:
#                 tmp += f" {c}"
#         elif isinstance(vals, (str,)):
#             tmp = vals
#         else:
#             assert type(vals) == "bonk", type(vals)
#         return f"{option}{tmp}"

LOGGER = lme.get_logger(__name__)


class Semantics:
    def strict_word(self, ast):
        LOGGER.warning(f"strict_word: {ast}")
        return ast

    def dquote(self, ast):
        LOGGER.warning(f"dquote: {ast}")
        if len(ast) > 10:
            ast = ast.lstrip()
            return f'"\\n{ast}\\n"'
        return ast

    def squote(self, ast):
        LOGGER.warning(f"squote: {ast}")
        ast = ast.strip().lstrip()
        is_json = ast.startswith("{") and ast.strip().endswith("}")
        if is_json:
            try:
                tmp = loads.json5(ast)
            except:
                is_json = False
            else:
                LOGGER.critical(f"found json: {tmp}")
                ast = json.dumps(tmp, indent=2)
            out = [x + " \\" for x in ast.split("\n")]
            out = "\n".join(out)
            return f"'{out}'"
        return ast

    # def group_command(self, ast):
    #     LOGGER.warning(f"group_command: {ast}")
    #     return ast

    def word(self, ast):
        LOGGER.warning(f"word: {ast}")
        return ast

    def simple_command(self, ast):
        LOGGER.warning(f"simple_command: {ast}")
        tail = ast
        biggest = ""
        for i, l in enumerate(tail):
            if len(l) > len(biggest):
                biggest = l
        result = []
        skip_next = False
        for i, l in enumerate(tail):
            if skip_next:
                skip_next = False
                continue
            try:
                n = tail[i + 1]
            except:
                n = ""
                # LOGGER.warning(f'looking at {[i,l,n]}')
            comb = f"{l} {n}"
            if len(comb) < len(biggest):
                result.append(comb)
                skip_next = True
            else:
                result.append(l)
        # import IPython; IPython.embed()
        newp = []
        while result:
            item = result.pop(0)
            if isinstance(item, (tuple,)):
                item = " ".join(item)
            newp.append(item)
        result = newp
        return "\n  ".join(result)

    def shell_command(self, ast):
        LOGGER.warning(f"shell_command: {ast}")
        return ast

    def path(self, ast):
        LOGGER.warning(f"path: {ast}")
        try:
            tmp = abcs.Path(ast).relative_to(abcs.Path(".").absolute())
        except ValueError:
            return ast
        else:
            return f"'{tmp}'"

    def pipeline_command(self, ast):
        LOGGER.warning(f"pipeline_command: {ast}")
        return ast

    def simple_list(self, ast):
        LOGGER.warning(f"simple_list: {ast}")
        return ast

    def word_list(self, ast):
        LOGGER.warning(f"word_list: {ast}")
        return ast

    def opt(self, ast):
        LOGGER.warning(f"opt: {ast}")
        return ast if isinstance(ast, (str,)) else " ".join(ast)

    def opt_val(self, ast):
        LOGGER.warning(f"opt_val: {ast}")
        return ast

    def subcommands(self, ast):
        LOGGER.warning(f"subcommands: {ast}")
        return " ".join(ast)

    def drilldown(self, ast):
        LOGGER.warning(f"drilldown: {ast}")
        return ast

    def entry(self, ast):
        LOGGER.warning(f"entry: {ast}")
        return str(ast)


def fmt(text, filename="?"):
    """
    :param text: argument
    :param filename: argument  (Default value = ?)
    :type text: text
    :type filename: filename='?'
    """
    semantics = Semantics()
    parser = bashParser()
    try:
        parsed = parser.parse(
            text,
            parseinfo=True,
            filename=filename,
            semantics=semantics,
        )
    except (tatsu.exceptions.FailedParse,) as exc:
        LOGGER.critical(exc)
        return text
    else:
        out = []
        for item in parsed:
            if isinstance(item, (list, tuple)):
                item = " ".join([str(x) for x in item])
            out.append(item)
        head = out.pop(0)
        # tail=out.copy()
        tail = "\n  ".join(out)
        return f"{head} {tail}"


bash_fmt = fmt
