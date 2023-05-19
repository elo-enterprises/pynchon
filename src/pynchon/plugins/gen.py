""" pynchon.plugins.gen
"""
import functools
from pynchon import models
from pynchon import abcs, cli #noqa
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Generators(models.NameSpace):
    """Collects `gen` commands from other plugins"""

    name = cli_name = "gen"
    priority = 1
    config_class = None

    @classmethod
    def init_cli(kls) -> cli.click.Group:
        """ """
        result = super(kls,kls).init_cli()
        for name,obj in kls.siblings.items():
            if obj.name=='core':
                continue
            elif 'gen' in dir(obj):
                LOGGER.critical(f'acquiring {obj.gen}')
                kls.click_acquire(
                    obj.gen,
                    copy=True,
                    name=obj.name,
                    help=f'Alias for `{kls.click_entry.name} {obj.name} gen`')
        return result
