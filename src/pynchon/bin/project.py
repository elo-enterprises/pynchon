""" pynchon.bin.project
"""
import pynchon
from pynchon import (util,)
from .common import kommand
from pynchon.bin import (groups, options)
LOGGER = pynchon.get_logger(__name__)
PARENT=groups.project
@kommand(
    name='entrypoints', parent=PARENT,
    formatters=dict(markdown=pynchon.T_TOC_CLI),
    options=[ options.file_setupcfg, options.format,
        options.stdout, options.output, options.header])
def project_entrypoints(format, file, stdout, output, header):
    """
    Describe entrypoints for this project (parses setup.cfg)
    """
    return util.load_entrypoints(
            util.load_setupcfg(file=file))


@kommand(
    name='version', parent=PARENT,
    # FIXME: formatters=dict(markdown=pynchon.T_VERSION_METADATA),
    options=[
        # FIXME: options.output_with_default('docs/VERSION.md'),
        options.format_markdown,
        options.stdout, options.header])
def version(format, file, stdout, output, header):
    """
    Describes version details for this package (and pynchon itself).
    """
    return dict(
        pynchon_version='..',
        package_version='..',
        git_hash='..', )

@kommand(
    name='plan', parent=PARENT,
    # FIXME: formatters=dict(markdown=pynchon.T_VERSION_METADATA),
    options=[
        # FIXME: options.output_with_default('docs/VERSION.md'),
        # options.format_markdown,
        # options.stdout, options.header
        ])
def plan():
    """
    List goals for auto-documenting this project
    """
    import os, glob
    config = dict(
        git_root=util.find_git_root(),
        python_project=util.is_python_project(),
    )
    src_root = os.path.join(config['git_root'],'src')
    src_root = src_root if os.path.isdir(src_root) else None
    if src_root:
        config.update(
            main_modules = glob.glob(os.path.join(src_root,'**/__main__.py'), recursive=True))
    config = {
        **config,
        **dict(
            src_root=src_root,
        ),
    }
    LOGGER.debug(f"{config}")
