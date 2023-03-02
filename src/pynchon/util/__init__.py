""" pynchon.util
"""
import os
import sys
import ast
import functools
import glob
import subprocess
from collections import OrderedDict
import termcolor
import mccabe
import griffe
import tomli as tomllib  # tomllib only available in py3.11
import pynchon
from pynchon.abcs import Path

LOGGER = pynchon.get_logger(__name__)
from pynchon import annotate

WORKING_DIR = os.getcwd()
GLYPH_COMPLEXITY = "🐉 Complex"


def find_j2s(config):
    project = config["project"].get("subproject", config["project"])
    project_root = project.get("root", config["git"]["root"])
    globs = [
        os.path.join(project_root, "**", "*.j2"),
    ]
    LOGGER.debug(f"finding .j2s under {globs}")
    globs = [glob.glob(x, recursive=True) for x in globs]

    matches = functools.reduce(lambda x, y: x + y, globs)
    j2s = [os.path.relpath(m) for m in matches]
    return j2s


def get_root(path: str = ".") -> str:
    """ """
    path = os.path.abspath(path)
    if ".git" in os.listdir(path):
        return Path(os.path.relpath(path))
    elif not path:
        return None
    else:
        return get_root(os.path.dirname(path))


def is_python_project() -> bool:
    """ """
    from pynchon.api import git
    return os.path.exists(os.path.join(git.get_root(), pynchon.PYNCHON_CONFIG_FILE))


def find_src_root(config: dict) -> str:
    """ """
    pconf = config.get("project", {})
    LOGGER.debug(f"project config: {pconf}")
    src_root = pconf.get("src_root", os.getcwd())
    # src_root = os.path.join(project_root, "src")
    src_root = src_root if os.path.isdir(src_root) else None
    return Path(os.path.relpath(src_root))


def click_recursive_help(cmd, parent=None, out={}, file=sys.stdout):
    """ """
    # source: adapted from https://stackoverflow.com/questions/57810659/automatically-generate-all-help-documentation-for-click-commands
    from click.core import Context as ClickContext

    full_name = cmd.name
    pname = getattr(cmd, "parent", None)
    pname = parent and getattr(parent, "name", "") or ""
    ctx = ClickContext(cmd, info_name=cmd.name, parent=parent)
    help_txt = cmd.get_help(ctx)
    invocation_sample = help_txt.split("\n")[0]
    for x in "Usage: [OPTIONS] COMMAND [COMMAND] [ARGS] ...".split():
        invocation_sample = invocation_sample.replace(x, "")
    out = {
        **out,
        **{
            full_name: dict(
                name=cmd.name, invocation_sample=invocation_sample, help=help_txt
            )
        },
    }
    commands = getattr(cmd, "commands", {})
    for sub in commands.values():
        out = {**out, **click_recursive_help(sub, ctx)}
    return out


def get_module(package: str = "", file: str = ""):
    """ """
    if not bool(package) ^ bool(file):
        err = "Expected --file or --package, but not both"
        raise RuntimeError(err)
    if file:
        file = os.path.abspath(file)
        new_path = os.path.dirname(file)
        assert os.path.exists(file)
        LOGGER.warning(f"modifying sys.path to include {new_path}")
        sys.path.append(new_path)
        package = os.path.splitext(os.path.basename(file))[0]
        working_dir = os.path.dirname(file)
    else:
        working_dir = WORKING_DIR
    loader = griffe.loader.GriffeLoader()
    module = loader.load_module(package)
    annotate.module(package, module, working_dir=working_dir)
    return module


def get_refs(working_dir=None, module=None) -> dict:
    """ """
    refs = dict(
        classes=dict(
            [
                [k, v]
                for k, v in module.classes.items()
                if not module.classes[k].is_alias
            ]
        ),
        modules=dict(
            [
                [k, v]
                for k, v in module.modules.items()
                if not module.modules[k].is_alias
            ]
        ),
        functions=OrderedDict(
            [
                [k, v]
                for k, v in sorted(module.functions.items())
                if not module.functions[k].is_alias
            ]
        ),
    )
    for name, kls in refs["classes"].items():
        annotate.klass(name, kls)
    for name, mod in refs["modules"].items():
        annotate.module(name, mod, working_dir=working_dir)
    for name, fxn in refs["functions"].items():
        annotate.function(name, fxn)
    return refs


def visit_module(
    output=[],
    stats={},
    module=None,
    template=pynchon.T_TOC_API,
    visited=[],
    exclude: list = [],
    module_name=None,
    working_dir=WORKING_DIR,
):
    """recursive visitor for this package, submodules, classes, functions, etc"""
    if module_name in exclude:
        LOGGER.debug(f"skipping module: {module_name}")
        return output
    annotate.module(module_name, module, working_dir=working_dir)
    refs = get_refs(working_dir=working_dir, module=module)
    # LOGGER.debug(f"exclude: {exclude}")
    LOGGER.debug(f"rendering module: {module_name}")
    rendered = template.render(
        griffe=griffe,
        stats=stats,
        working_dir=working_dir,
        module_name=module_name,
        module=module,
        **refs,
    )
    output.append(clean_text(rendered))
    for name, sub in refs["modules"].items():
        if sub in visited:
            continue
        visit_module(
            output=output,
            module=sub,
            working_dir=working_dir,
            module_name=f"{module_name}.{name}",
            visited=visited + [module],
            exclude=exclude,
            template=template,
        )
    return output


def clean_text(txt: str) -> str:
    """ """
    return "\n".join([line for line in txt.split("\n") if line.strip()])


class Checker(mccabe.McCabeChecker):
    """ """

    def run(self):
        if self.max_complexity < 0:
            return
        visitor = mccabe.PathGraphingAstVisitor()
        visitor.preorder(self.tree, visitor)
        for graph in visitor.graphs.values():
            tmp = graph.complexity()
            if tmp > self.max_complexity:
                text = self._error_tmpl % (graph.entity, tmp)
                yield tmp, graph.lineno, graph.column, text, type(self)


def complexity(code: str = None, fname: str = None, threshold: int = 7):
    """ """
    threshold = 7
    try:
        tree = compile(code, fname, "exec", ast.PyCF_ONLY_AST)
    except SyntaxError:
        e = sys.exc_info()[1]
        sys.stderr.write("Unable to parse %s: %s\n" % (fname, e))
        return 0
    complex = []
    Checker.max_complexity = threshold
    for complexity, lineno, _offset, text, check in Checker(tree, fname).run():
        complex.append(
            dict(
                file=os.path.relpath(fname),
                lineno=lineno,
                # text=text,
                score=complexity,
            )
        )
    out = []
    for admonition in complex:
        out.append(
            dict(
                glyph=GLYPH_COMPLEXITY,
                hover=f'score {admonition["score"]} / {threshold}',
                link=f'/{admonition["file"]}#L{admonition["lineno"]}',
            )
        )
    return out


from collections import namedtuple


def invoke(
    cmd=None,
    stdin="",
    interactive: bool = False,
    large_output: bool = False,
    log_command: bool = True,
    environment: dict = {},
    log_stdin: bool = True,
    system: bool = False,
):
    """
    dependency-free replacement for the `invoke` module,
    which fixes problems with subprocess.POpen and os.system.
    """
    log_command and LOGGER.info(
        "running command: (system={})\n\t{}".format(
            system, termcolor.colored(cmd, color="green")
        )
    )
    if system:
        assert not stdin and not interactive
        error = os.system(cmd)
        result = namedtuple(
            "InvocationResult",
            ["failed", "failure", "success", "succeeded", "stdout", "stdin"],
        )
        result.failed = result.failure = bool(error)
        result.success = result.succeeded = not bool(error)
        result.stdout = result.stdin = "<os.system>"
        return result
    exec_kwargs = dict(
        shell=True, env={**{k: v for k, v in os.environ.items()}, **environment}
    )
    if stdin:
        msg = "command will receive pipe:\n{}"
        log_stdin and LOGGER.debug(msg.format(((stdin))))
        exec_kwargs.update(
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        exec_cmd = subprocess.Popen(cmd, **exec_kwargs)
        exec_cmd.stdin.write(stdin.encode("utf-8"))
        exec_cmd.stdin.close()
        exec_cmd.wait()
    else:
        if not interactive:
            exec_kwargs.update(
                stdout=subprocess.PIPE,
                # stderr=subprocess.PIPE
            )
        exec_cmd = subprocess.Popen(cmd, **exec_kwargs)
        exec_cmd.wait()
    if exec_cmd.stdout:
        exec_cmd.stdout = (
            "<LargeOutput>" if large_output else exec_cmd.stdout.read().decode("utf-8")
        )
    else:
        exec_cmd.stdout = "<Interactive>"
    if exec_cmd.stderr:
        exec_cmd.stderr = exec_cmd.stderr.read().decode("utf-8")
    exec_cmd.failed = exec_cmd.returncode > 0
    exec_cmd.succeeded = not exec_cmd.failed
    exec_cmd.success = exec_cmd.succeeded
    exec_cmd.failure = exec_cmd.failed
    return exec_cmd
