""" pynchon.codemod.docstrings.simple """
import libcst as cst
from .base import base
from pynchon.util import lme
from strongtyping.docs_from_typing import docs_from_typing
from pynchon import shimport

LOGGER = lme.get_logger(__name__)


class klass(base):
    DESCRIPTION: str = """\n\tWhere missing, adds docstrings to classes"""


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
        # ctx = dict(mod=,filename=self.context.filename, package=self.context.full_package_name,name=)
        mod = self.context.full_module_name
        dotpath = f"{self.this_class_name+'.' if self.this_class_name else '' }{original_node.name.value}"
        ctx = f"{mod}.{dotpath}"
        # LOGGER.critical(ctx)
        expr, docstring = _get_docstring(original_node)
        if docstring is None:
            LOGGER.critical(f"{ctx}:: no docstring!")
            bits = dotpath.split('.')
            assert mod
            _import = shimport.import_module(mod)
            while bits:
                LOGGER.critical([_import, bits])
                _import = getattr(_import, bits.pop(0))
            default_docstring = docs_from_typing(
                _import, style='rest', remove_linebreak=True
            )
            default_docstring = '\n'.join(default_docstring)
            default_docstring = f'"""{default_docstring}"""'
            LOGGER.critical(f"{ctx}:: suggest:\n\n{default_docstring}")
            # import IPython; IPython.embed()
            # iblock = updated_node.body.children
            # import IPython; IPython.embed()
            # iblock = iblock.with_changes(body=
            #     [cst.parse_statement(f'"""{tmp}"""')] + list(iblock.body))
            # updated_node.children
            # expr.deep_replace()
            # expr=
            tmp = cst.parse_statement(default_docstring)
            cst.ensure_type(expr.body, cst.IndentedBlock)
            # cst.ensure_type(expr.body.body[0], cst.SimpleStatementLine)
            return expr.with_changes(
                body=expr.body.with_changes(body=(tmp,) + expr.body.body)
            )
            # updated_node.deep_replace(
            #     # cst.ensure_type(expr.body.body[0], cst.SimpleStatementLine)
            #     cst.ensure_type(expr.body.body, cst.SimpleStatementLine),
            #
            iblock = expr.body
            # iblock=iblock.deep_replace(iblock.children,
            #     [cst.parse_statement(default_docstring)] \
            #     + list(iblock.children)
            # )
            newbody = [tmp] + list(iblock.body)
            iblock = iblock.with_changes(body=newbody)
            result = updated_node.deep_replace(expr.body, iblock)
            import IPython

            IPython.embed()
            return result
            # return updated_node.deep_replace(
            #     expr, expr.with_changes())
            # import IPython; IPython.embed()
            return updated_node.with_changes(
                body=original_node.body.body.with_changes(
                    body=[
                        [cst.parse_statement(default_docstring)]
                        + list(original_node.body.children)
                    ]
                )
            )
            # return updated_node.with_changes(
            #     body=iblock)

        return original_node
        # from libcst import parse_statement
        # default_docstring = f'"""  """'
        # lctx = f"{original_node.__class__.__name__} @ '{full_module_name}'"
        # raise Exception([ltx, original_node])


from libcst._nodes.statement import *


def _get_docstring(body):
    """:param body: argument
    :type body: body
    Function _get_docstring
    """
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
        # try:
        #     tmp = eval(tmp)
        # except:
        #     LOGGER.debug('cannot eval')
        # if not tmp.strip():
        #     LOGGER.critical(f"{lctx}: docstring present but empty")
        #     better = sstring.with_changes(value=default_docstring)
        # else:
        #     return original_node
        # updated_node = updated_node.deep_replace(sstring, better)
        # return updated_node
