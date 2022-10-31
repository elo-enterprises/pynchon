""" pynchon.bin.cli
"""
import pynchon
from pynchon import (util,)

from .common import *
from pynchon.bin import (groups, options)
LOGGER = pynchon.get_logger(__name__)
PARENT = groups.gen_cli
@kommand(
    name='toc', parent=PARENT,
    formatters=dict(markdown=pynchon.T_TOC_CLI),
    options=[ options.file_setupcfg, options.format,
        click.option(
            '--output', '-o', default='docs/cli/README.md',
            help=('output file to write.  (optional)')),
        options.stdout, options.header])
def toc(format, file, stdout, output, header):
    """
    Describe entrypoints for this project (parses setup.cfg)
    """
    return util.load_entrypoints(
            util.load_setupcfg(file=file))

@kommand(
    name='all', parent=PARENT,
    formatters=dict(markdown=pynchon.T_DETAIL_CLI),
    options=[ options.file_setupcfg, options.format,
        click.option(
            '--output-dir', default='docs/cli',
            help=('output directory (optional)')),
        options.stdout, options.header])
def _all(format, file, stdout, output_dir, header):
    """
    Generates help for every entrypoint
    """
    return util.load_entrypoints(
            util.load_setupcfg(file=file))


@kommand(
    name='entrypoint', parent=PARENT,
    formatters=dict(markdown=pynchon.T_DETAIL_CLI),
    options=[
        options.format, options.stdout,
        options.header, options.file, options.output,
        options.name, options.module,
        ])
def entrypoint(format, module, name, file, output, stdout, header):
    """
    Autogenenerate docs for python CLIs using click
    """
    result = []
    if name and not module:
        module, name = name.split(':')
    if (module and name):
        mod = importlib.import_module(module)
        entrypoint = getattr(mod, name)
    else:
        msg = "No entrypoint found"
        LOGGER.warning(msg)
        return dict(error=msg)
    LOGGER.debug(f"Recursive help for `{module}:{name}`")
    result = util.click_recursive_help(entrypoint, parent=None)
    package = module.split('.')[0]
    header = f"CLI entry-points for {package} \n\n{header}"
    return dict(commands=result, header=header)
