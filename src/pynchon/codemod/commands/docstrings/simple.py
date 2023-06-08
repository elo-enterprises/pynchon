""" pynchon.codemod.docstrings.simple """
import libcst as cst
from libcst._nodes.statement import (
    BaseSuite,
    ConcatenatedString,
    Expr,
    Sequence,
    SimpleStatementLine,
    SimpleString,
    inspect,
)
from strongtyping.docs_from_typing import docs_from_typing

from pynchon import shimport
from pynchon.util import lme

from .base import base

LOGGER = lme.get_logger(__name__)

from textwrap import dedent


def is_param_doc(txt: str):
    """
    txt: str
    """
    return txt.lstrip().startswith(":param")


def write_docstring(
    mod=None,
    dotpath=None,
    docstring=None,
    # indent=''
):
    """
    mod=None
    dotpath=None
    docstring=None
    """
    """ """
    assert mod, "mod not set.. check .libcst.codemod.yaml src root"
    bits = dotpath.split(".")
    obits = [x for x in bits]
    _import = shimport.import_module(mod)
    while bits:
        try:
            _import = getattr(_import, bits.pop(0))
        except:
            LOGGER.critical(f"cannot import {obits}")
            return None
    LOGGER.critical(f"imported {_import}")
    # try:
    #     default_docstring = docs_from_typing(
    #         _import, style="numpy",
    # remove_linebreak=True
    #     )
    # except (AttributeError,) as exc:
    #     return
    import inspect
    doc_actual = inspect.getdoc(_import)

    default_docstring = str(inspect.signature(_import))
    default_docstring = default_docstring[1:-1].split(', ')
    default_docstring = [
        f':param {x}:'
        for x in default_docstring
        if not any([z.lstrip().startswith(f':param {x}:') for z in doc_actual.split('\n')])
    ]
    # :param arg1: description
    # :type arg1: type description
    # :return: return description
    # :rtype: the return type description
    if doc_actual:
        LOGGER.warning(f"doc string for {obits} already exists; skipping..")
        # return
    src = inspect.getsource(_import).split("\n")
    index = [i for i, x in enumerate(src) if x.endswith(":")][0]
    ctx_indent = src[index + 1][: len(src[index + 1]) - len(dedent(src[index + 1]))]
    default_docstring = reversed(sorted(default_docstring))
    default_docstring = "\n".join(default_docstring)
    default_docstring = f'"""\n{default_docstring.strip()}\n"""'
    default_docstring = [(ctx_indent) + x for x in default_docstring.split("\n")]
    default_docstring = "\n".join(default_docstring)
    # LOGGER.critical(f"{dotpath}:: suggest:\n\n{default_docstring}")
    dstart = index + 1
    dpre = src[dstart].lstrip().rstrip()
    dpre = '"""' if dpre.startswith('"""') else ""
    dpre = "'''" if dpre.startswith("'''") else ""
    for i, x in enumerate(src[dstart + 1 :]):
        x = x.lstrip().strip()
        if x.endswith(dpre):
            dend = i + dstart
            break
    else:
        LOGGER.critical('wat?')
        raise Exception()
        # if x.startswith(dend = index+1
    print(
        [
            dstart,
            dend,
            dpre,
        ]
    )
    src = src[:dstart] + [default_docstring] + src[dend:]
    src = "\n" + "\n".join([x for x in src])
    src = dedent(src)
    # LOGGER.critical(src)
    return src


def _get_docstring(body):
    """
    body
    """
    """ """
    if isinstance(body, Sequence):
        if body:
            expr = body[0]
        else:
            return expr, None
    else:
        expr = body
    while isinstance(expr, (BaseSuite, SimpleStatementLine)):
        if len(expr.body) == 0:
            return expr.body, None
        expr = expr.body[0]
    if not isinstance(expr, Expr):
        return expr, None
    val = expr.value
    if isinstance(val, (SimpleString, ConcatenatedString)):
        evaluated_value = val.evaluated_value
    else:
        return expr, None

    if evaluated_value is None:
        return expr, evaluated_value
    else:
        return inspect.cleandoc(evaluated_value)


class klass(base):
    DESCRIPTION: str = """\n\tWhere missing, adds docstrings to classes"""
    # from libcst import parse_statement
    # default_docstring = f'"""  """'
    # lctx = f"{original_node.__class__.__name__} @ '{full_module_name}'"
    # raise Exception([ltx, original_node])


class module(base):
    DESCRIPTION: str = """\n\tWhere missing, adds docstrings to modules"""

    def leave_Module(
        self,
        original_node: cst.Module,
        updated_node: cst.Module,
    ) -> cst.Module:
        full_module_name = self.context.full_module_name
        default_docstring = f'""" {full_module_name} """'
        lctx = f"{original_node.__class__.__name__} @ '{full_module_name}'"
        try:
            base = updated_node.children[0]
        except IndexError:
            # LOGGER.critical(f"{lctx}: empty-file!")
            return updated_node.with_changes(
                body=[cst.parse_statement(default_docstring)]
            )
        try:
            expr = base.children[0]
            sstring = expr.children[0]
        except IndexError:
            # FIXME: module starts with whitespace?
            # LOGGER.critical(f"{lctx}: starts with whitespace?")
            return original_node
        sstring = updated_node.children[0].children[0].children.pop(0)
        tmp = sstring.value
        if not tmp.strip():
            return updated_node.with_changes(
                body=[cst.parse_statement(default_docstring)] + list(original_node.body)
            )
        else:
            return original_node


class function(base):
    DESCRIPTION: str = """\n\tWhere missing, adds docstrings to functions"""

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.this_class = None

    def leave_ClassDef(
        self,
        original_node: cst.ClassDef,
        updated_node: cst.ClassDef,
    ) -> cst.ClassDef:
        self.this_class_name = None
        return original_node

    def visit_ClassDef(
        self,
        original_node: cst.ClassDef,
        # updated_node: cst.ClassDef,
    ) -> cst.ClassDef:
        self.this_class_name = original_node.name.value
        return original_node

    def leave_FunctionDef(
        self,
        original_node: cst.FunctionDef,
        updated_node: cst.FunctionDef,
    ) -> cst.FunctionDef:
        mod = self.context.full_module_name
        dotpath = f"{self.this_class_name+'.' if self.this_class_name else '' }{original_node.name.value}"
        ctx = f"{mod}.{dotpath}"
        expr, docstring = _get_docstring(original_node)
        if docstring is not None and docstring.strip():
            LOGGER.critical("docstring ok")
            return original_node
        elif not (docstring and docstring.strip()):
            LOGGER.critical(f"{ctx}:: docstring is empty")
            txt = write_docstring(
                mod=mod,
                dotpath=dotpath,
                docstring=docstring
                # indent=self.context.module.default_indent
            )
            if txt is None:
                LOGGER.warning(f'error importing {[mod,dotpath]} ?')
                return original_node
            else:
                updated_node = cst.parse_statement(txt)
                LOGGER.critical(updated_node)
                return updated_node
        elif docstring is None:
            LOGGER.info(f"{ctx}:: no docstring!")
            return original_node
            # if src:
            #     try:
            #         return cst.parse_statement(
            #             src,
            #             # cst.PartialParserConfig(
            #             #     default_indent=self.context.module.default_indent
            #             # ),
            #         )
            #     except (Exception,) as exc:
            #         LOGGER.critical(exc)

        return original_node
