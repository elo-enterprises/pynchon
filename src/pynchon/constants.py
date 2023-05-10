""" pynchon.constants
"""
import os

PYNCHON_ROOT = os.environ.get("PYNCHON_ROOT", None)
PYNCHON_CONFIG = os.environ.get('PYNCHON_CONFIG', None)
LOG_LEVEL = os.environ.get('PYNCHON_LOG_LEVEL', 'WARNING')

CONF_FILE_SEARCH_ORDER = ["pynchon.json5", ".pynchon.json5", "pyproject.toml"]
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

# TEMPLATE_DIR = os.environ.get(
#     "PYNCHON_TEMPLATE_DIR",
#     os.path.join(
#         os.path.dirname(__file__),
#         "templates",
#     ),
# )
#
# # FIXME: reuse parallel jinja env/template stuff in pynchon.util.text.render
# plugin_base = "pynchon/plugins"
# T_DETAIL_CLI = ENV.get_template(f"{plugin_base}/python/cli/detail.md.j2")
# T_TOC_API = ENV.get_template(f"{plugin_base}/python/api/TOC.md.j2")
# T_TOC_CLI = ENV.get_template(f"{plugin_base}/python/cli/TOC.md.j2")
# T_VERSION_METADATA = ENV.get_template(f"{plugin_base}/core/VERSIONS.md.j2")
# T_CLI_MAIN_MODULE = ENV.get_template(f"{plugin_base}/python/cli/main.module.md.j2")
