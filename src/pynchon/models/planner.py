"""
"""
import typing

from pynchon import events, cli

# from pynchon.bin import entry
# from pynchon.fleks.plugin import Plugin as AbstractPlugin
# from pynchon.plugins.util import get_plugin_obj
from pynchon.util.tagging import tags

# from .planning import *
from . import planning
from .plugin_types import BasePlugin

from pynchon.util import typing, lme  # noqa


@tags(cli_label='Planner')
class AbstractPlanner(BasePlugin):
    """
    AbstractPlanner is a plugin-type that provides plan/apply basics
    """

    cli_label = 'Planner'

    @property
    def changes(self):
        """
        Set(git_changes).intersection(plugin_resources)
        """
        git = self.siblings['git']
        changes = git.modified
        these_changes = set(changes).intersection(set(self.list(changes=False)))
        return dict(modified=list(these_changes))

    @cli.click.option(
        '--changes',
        '-m',
        'changes',
        is_flag=True,
        default=False,
        help='returns the git-modified subset',
    )
    def list(self, changes: bool = False):
        """Lists resources associated with this plugin"""
        if changes:
            return self.changes['modified']
        from pynchon import abcs
        from pynchon.util import files

        try:
            include_patterns = self['include_patterns']
            root = self['root']
        except (KeyError,) as exc:
            self.logger.critical(
                f'self.__class__ tried to use self.list(), but does not follow protocol'
            )
            self.logger.critical(
                "self['include_patterns'] and self['root'] must both be defined!"
            )
            raise
        root = abcs.Path(root)
        # proot = self.project_config['pynchon']['root']
        tmp = [p for p in include_patterns if abcs.Path(p).is_absolute()]
        tmp += [root / p for p in include_patterns if not abcs.Path(p).is_absolute()]
        # tmp += [proot / p for p in include_patterns if not abcs.Path(p).is_absolute()]
        return files.find_globs(tmp)

    @tags(publish_to_cli=False)
    def goal(self, **kwargs):
        """ """
        return planning.Goal(
            owner=f"{self.__class__.__module__}.{self.__class__.__name__}", **kwargs
        )

    def plan(self, config=None) -> planning.Plan:
        """Creates a plan for this plugin"""
        config = config or self.cfg()
        events.lifecycle.send(
            # writes status event (used by the app-console)
            stage=f"Planning for `{self.__class__.name}`"
        )
        plan = planning.Plan()
        return plan

    def apply(self, config=None) -> planning.ApplyResults:
        """Executes the plan for this plugin"""
        from pynchon.util.os import invoke

        events.lifecycle.send(
            # write status event (used by the app-console)
            stage=f"applying for `{self.__class__.name}`"
        )
        plan = self.plan(config=config)
        results = []
        for action_item in plan:
            events.lifecycle.send(self, applying=action_item)
            application = invoke(action_item.command)
            tmp = planning.Action(
                result=application.succeeded,
                command=action_item.command,
                resource=action_item.resource,
                type=action_item.type,
            )
            results.append(tmp)
        results = planning.ApplyResults(results)
        return results


class ShyPlanner(AbstractPlanner):
    """
    ShyPlanner uses plan/apply workflows, but they must be
    executed directly.  ProjectPlugin (or any other parent plugins)
    won't include this as a sub-plan.
    """

    contribute_plan_apply = False


@tags(cli_label='Manager')
class Manager(ShyPlanner):
    cli_label = 'Manager'


class Planner(ShyPlanner):
    """
    Planner uses plan/apply workflows, and contributes it's plans
    to ProjectPlugin (or any other parent plugins).
    """

    contribute_plan_apply = True
