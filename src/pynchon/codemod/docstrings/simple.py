""" pynchon.codemod.docstrings.simple """
import libcst as cst
from strongtyping.docs_from_typing import docs_from_typing

from pynchon import shimport
from pynchon.util import lme

from .base import base

LOGGER = lme.get_logger(__name__)


class klass(base):
    DESCRIPTION: str = """\n\tWhere missing, adds docstrings to classes"""
    # from libcst import parse_statement
    # default_docstring = f'"""  """'
    # lctx = f"{original_node.__class__.__name__} @ '{full_module_name}'"
    # raise Exception([ltx, original_node])


from libcst._nodes.statement import (BaseSuite, ConcatenatedString, Expr,
                                     Sequence, SimpleStatementLine,
                                     SimpleString, inspect)


def _get_docstring(body):
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

    if evaluated_value is not None and clean:
        return inspect.cleandoc(evaluated_value)
    return expr, evaluated_value


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
        else:
            if not (docstring and docstring.strip()):
                LOGGER.critical(f"{ctx}:: docstring is empty")
            elif docstring == None:
                LOGGER.critical(f"{ctx}:: no docstring!")
            bits = dotpath.split(".")
            assert mod
            _import = shimport.import_module(mod)
            while bits:
                _import = getattr(_import, bits.pop(0))
            LOGGER.critical(f"imported {_import}")
            default_docstring = docs_from_typing(
                _import, style="rest", remove_linebreak=True
            )
            default_docstring = "\n".join(default_docstring)
            default_docstring = f'"""\n{default_docstring.strip()}\n"""'
            LOGGER.critical(f"{ctx}:: suggest:\n\n{default_docstring}")
            # expr=expr.deep_clone()
            tmp = cst.parse_statement(default_docstring)
            tmp = tmp.body[0].value
            cst.ensure_type(original_node.body, cst.IndentedBlock)
            # import IPython; IPython.embed()
            # raise Exception()
            # return updated_node
            # .with_changes(name=cst.Name('bonk'))
            result = updated_node.with_changes(
                body=updated_node.body.with_changes(
                    body=[tmp] + list(original_node.body.body)
                )
            )
            # import IPython; IPython.embed()

            return result

        return original_node


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
            LOGGER.critical(f"{lctx}: empty-file!")
            return updated_node.with_changes(
                body=[cst.parse_statement(default_docstring)]
            )
        try:
            expr = base.children[0]
            sstring = expr.children[0]
        except IndexError:
            # FIXME: module starts with whitespace?
            LOGGER.critical(f"{lctx}: starts with whitespace?")
            return original_node
        sstring = updated_node.children[0].children[0].children.pop(0)
        tmp = sstring.value
        if not tmp.strip():
            return updated_node.with_changes(
                body=[cst.parse_statement(default_docstring)] + list(original_node.body)
            )
        else:
            return original_node
