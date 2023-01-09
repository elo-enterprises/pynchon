""" pynchon.bin.project
"""
import json
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
def project_version(format, file, stdout, output, header):
    """
    Describes version details for this package (and pynchon itself).
    """
    return dict(
        pynchon_version=util.pynchon_version(),
        package_version='..',
        git_hash=util.get_git_hash(), )

# @kommand(
#     name='init', parent=PARENT,
#     # FIXME: formatters=dict(markdown=pynchon.T_VERSION_METADATA),
#     options=[
#         # FIXME: options.output_with_default('docs/VERSION.md'),
#         # options.format_markdown,
#         # options.stdout, options.header
#         ])
# def project_init():
#     """
#     Initialize working-directory as a pynchon project
#     """

@kommand(
    name='plan', parent=PARENT,
    # formatters=dict(
    #     # markdown=pynchon.T_VERSION_METADATA
    #     json=True,
    #     ),
    options=[
        # FIXME: options.output_with_default('docs/VERSION.md'),
        # options.format_markdown,
        options.stdout,
         # options.header
        ])
def project_plan(stdout):
    """
    List goals for auto-documenting this project
    """
    import os, glob
    # setupcfg = util.load_setupcfg()['tool:pynchon']
    # config = dict(
    #     git_root=util.find_git_root(),
    #     python_project=util.is_python_project(),
    #     setupcfg=setupcfg,
    plan = []
    config = dict(
        pynchon=dict(
            version=util.pynchon_version(),
            ),
        project=dict(
            name=os.path.split(os.getcwd())[-1],
            root=util.find_git_root(),
            # project=util.is_python_project(),
            version=util.project_version(),
            hash=util.get_git_hash(),
        )
    )
    src_root = util.find_src_root(config)
    config['source'] = dict(root=src_root)
    if config['source']['root']:
        __main__ = os.path.join(config['source']['root'], '**', '__main__.py')
        __main__ = [os.path.relpath(x) for x in glob.glob(__main__, recursive=True)],
        config['source'].update(__main__=__main__)
        plan += [
            f'mkdir -p {src_root}/docs/api',
        ]
        if __main__:
            plan += [f'mkdir -p {src_root}/docs/cli',]
    # LOGGER.debug(f"{config}")
    config['plan']=plan
    return json.dumps(config,indent=2)
