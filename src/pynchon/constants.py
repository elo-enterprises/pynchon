""" pynchon.constants
"""
DEFAULT_PLUGINS = [
    # FIXME: docs
    "core",
    "plugins",
    "project",
    "globals",
    "git",
    'python',
    'gen',
    'render',
    "json",
    "jinja",
]

# URL_BUILTINS = "https://docs.python.org/3/library/functions.html"
# TEMPLATE_DIR = os.environ.get(
#     "PYNCHON_TEMPLATE_DIR",
#     os.path.join(
#         os.path.dirname(__file__),
#         "templates",
#     ),
# )
# assert os.path.exists(TEMPLATE_DIR), TEMPLATE_DIR
# import jinja2
# ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
#
# # FIXME: reuse parallel jinja env/template stuff in pynchon.util.text.render
# plugin_base = "pynchon/plugins"
# T_DETAIL_CLI = ENV.get_template(f"{plugin_base}/python/cli/detail.md.j2")
# T_TOC_API = ENV.get_template(f"{plugin_base}/python/api/TOC.md.j2")
# T_TOC_CLI = ENV.get_template(f"{plugin_base}/python/cli/TOC.md.j2")
# T_VERSION_METADATA = ENV.get_template(f"{plugin_base}/core/VERSIONS.md.j2")
# T_CLI_MAIN_MODULE = ENV.get_template(f"{plugin_base}/python/cli/main.module.md.j2")
