""" pynchon.codemod.commands.docstrings
"""
import argparse
import textwrap

import libcst as cst
from libcst.codemod import CodemodContext, VisitorBasedCodemodCommand

from pynchon.util import lme
LOGGER = lme.get_logger(__name__)

class javadoc(VisitorBasedCodemodCommand):
    DESCRIPTION: str = textwrap.dedent(
        """
        Add docstrings to functions
        """
    )

    def __init__(
        self,
        context: CodemodContext,
        # formatter: str = "black",
        # parameter_count: Optional[int] = None,
        # argument_count: Optional[int] = None,
    ) -> None:
        super().__init__(context)
        # self.parameter_count: int = parameter_count or presets["parameter_count"]
        # self.argument_count: int = argument_count or presets["argument_count"]

    @staticmethod
    def add_args(arg_parser: argparse.ArgumentParser) -> None:
        """ """
        # arg_parser.add_argument(
        #     "--formatter",
        #     dest="formatter",
        #     metavar="FORMATTER",
        #     help="Formatter to target (e.g. yapf or black)",
        #     type=str,
        #     default="black",
        # )
        # arg_parser.add_argument(
        #     "--paramter-count",
        #     dest="parameter_count",
        #     metavar="PARAMETER_COUNT",
        #     help="Minimal number of parameters for us to add trailing comma",
        #     type=int,
        #     default=None,
        # )
        # arg_parser.add_argument(
        #     "--argument-count",
        #     dest="argument_count",
        #     metavar="ARGUMENT_COUNT",
        #     help="Minimal number of arguments for us to add trailing comma",
        #     type=int,
        #     default=None,
        # )

    # def leave_Parameters(
    #     self,
    #     original_node: cst.Parameters,
    #     updated_node: cst.Parameters,
    # ) -> cst.Parameters:
        # skip = (
        #     #
        #     self.parameter_count is None
        #     or len(updated_node.params) < self.parameter_count
        #     or (
        #         len(updated_node.params) == 1
        #         and updated_node.params[0].name.value in {"self", "cls"}
        #     )
        # )
        # if skip:
        #     return updated_node
        # else:
        #     last_param = updated_node.params[-1]
        #     return updated_node.with_changes(
        #         params=(
        #             *updated_node.params[:-1],
        #             last_param.with_changes(comma=cst.Comma()),
        #         ),
        #     )

    # def leave_SimpleString(
    #     self, onode, unode
    # ):
    #     import IPython; IPython.embed()
    def leave_Module(
        self,
        original_node: cst.Module,
        updated_node: cst.Module,
    ) -> cst.Module:
        try:
            base = updated_node.children[0]
        except IndexError:
            tmp=self.context.full_module_name
            LOGGER.critical(f"{original_node.__class__.__name__} @ {tmp} is empty-file!")
            from libcst import matchers as m, parse_statement
            return updated_node.with_changes(body=[parse_statement(f'"""{tmp}"""')])
        expr = base.children[0]
        sstring = expr.children[0]
        sstring = updated_node.children[0].children[0].children.pop(0)
        tmp = sstring.value
        # LOGGER.critical(f"found module docstring:\n\n{tmp}'")
        if not eval(tmp).strip():
            better = sstring.with_changes(value='"""bonk"""')
            import IPython; IPython.embed()
        else:
            better = sstring
            # import IPython
            # IPython.embed()
        # updated_node.children[0].children[0].children[0].insert(0, sstring)
        updated_node = updated_node.deep_replace(sstring, better)
        # original_node.children[0].children[0].children[0]=original_node.children[0].children[0].children[0].with_changes(value='"""bonk"""')
        # print(updated_node.children[0].children[0].children[0])
        return updated_node
        # import IPython; IPython.embed()
        # if len(updated_node.args) < self.argument_count:
        #     return updated_node
        # else:
        #     last_arg = updated_node.args[-1]
        #     return updated_node.with_changes(
        #         args=(
        #             *updated_node.args[:-1],
        #             last_arg.with_changes(comma=cst.Comma()),
        #         ),
        #     )
