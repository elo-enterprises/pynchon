
### Python Plugins

For auto-discovery of things like "name of this package" or "entry-points for this package" `pynchon` assumes by default that it is working inside the source-tree for a modern python project.

If your project is using older packaging standards, or you're working on a group of files that's not a proper python project, you can usually work around this by passing information in directly instead of relying on auto-discovery.  Use the `pkg_name` top-level config key.


Pynchon relies heavily on [griffe](https://pypi.org/project/griffe/) for parsing and for [AST-walking](https://docs.python.org/3/library/ast.html).

For cyclomatic complexity, we rely on [mccabe](https://github.com/PyCQA/mccabe).
