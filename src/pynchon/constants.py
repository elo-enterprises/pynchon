""" pynchon.constants
"""
import os

import jinja2
DEFAULT_PLUGINS = [
    # WARNING: edit src/pynchon/plugins/__init__ to add import..
    "base", "project",
    "globals",
    "git",
    'python',
    'gen', 'render',
    "json", "jinja",
]
URL_BUILTINS = "https://docs.python.org/3/library/functions.html"
TEMPLATE_DIR = os.environ.get(
    "PYNCHON_TEMPLATE_DIR",
    os.path.join(
        os.path.dirname(__file__),
        "templates",
    ),
)
assert os.path.exists(TEMPLATE_DIR), TEMPLATE_DIR

ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

T_DETAIL_CLI = ENV.get_template("cli/detail.md.j2")
T_TOC_API = ENV.get_template("api/TOC.md.j2")
T_TOC_CLI = ENV.get_template("cli/TOC.md.j2")
T_VERSION_METADATA = ENV.get_template("VERSIONS.md.j2")
T_CLI_MAIN_MODULE = ENV.get_template("cli/main.module.md.j2")
