import libcst as cst
from libcst import parse_module
from libcst.codemod import CodemodContext, VisitorBasedCodemodCommand


class AddDocstringsVisitor(cst.CSTVisitor):
    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        print(node)
        # import IPython; IPython.embed()
        # Check if the function has a docstring
        # if not node.body or not isinstance(node.body.children[0], cst.SimpleStatementLine):
        #     # Create an empty docstring
        #     docstring = cst.SimpleString("\"\"\"\"")
        #     docstring_with_indent = docstring #docstring.with_changes(leading_lines=node.defn.leading_lines)
        #     # Insert the docstring before the function definition
        #     new_node = node.with_changes(
        #         docstring_with_indent
        #         # node.defn.with_changes(
        #         #     leading_lines=[docstring_with_indent]
        #         #     # + node.defn.leading_lines
        #         #     )
        #     )
        #     self._visit_and_replace(node, new_node)
        # else:
        # self.generic_visit(node)


class AddDocstringsCommand(VisitorBasedCodemodCommand):
    def __init__(
        self,
        context: CodemodContext,
    ) -> None:
        # Initialize the base class with context, and save our args. Remember, the
        # "dest" for each argument we added above must match a parameter name in
        # this init.
        super().__init__(context)

    def visit_ClassDef(self, node: cst.ClassDef):
        # self.stack.append(node.name.value)
        pass

    def leave_ClassDef(self, node: cst.ClassDef) -> None:
        # self.stack.pop()
        pass

    def visit_FunctionDef(self, node: cst.FunctionDef):
        # self.stack.append(node.name.value)
        # self.annotations[tuple(self.stack)] = (node.params, node.returns)
        # return (
        #     False
        # )  # pyi files don't support inner functions, return False to stop the traversal.
        print(node.name.value)

    def leave_FunctionDef(self, node: cst.FunctionDef) -> None:
        # self.stack.pop()
        print(node.name.value)


if __name__ == "__main__":
    # Parse the input Python file
    python_code = """
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b
"""
    module = parse_module(python_code)

    # Apply the codemod
    updated_module = AddDocstringsCommand(context=module)
    # .visit_and_update_module(module)

    # Print the updated code
    # print(updated_module.code)
