""" pynchon.models.planner """

import typing

from fleks import tagging
from memoized_property import memoized_property
from fleks.util.tagging import tags

from pynchon import abcs, cli
from pynchon.app import app
from pynchon.util.os import invoke

from . import planning
from .plugins import BasePlugin

from pynchon.util import lme, typing  # noqa


LOGGER = lme.get_logger(__name__)


@tags(cli_label="Planner")
class AbstractPlanner(BasePlugin):
    """A plugin-type that provides plan/apply basics"""

    cli_label = "Planner"

    @tags(publish_to_cli=False)
    def goal(self, **kwargs):
        """ """
        return planning.Goal(
            owner=f"{self.__class__.__module__}.{self.__class__.__name__}", **kwargs
        )

    @property
    def Plan(self):
        return planning.Plan

    def plan(self, config=None) -> planning.Plan:
        """
        Creates a plan for this plugin
        """
        # app.manager.status_bar.update(app='PLAN')
        app.status_bar.update(
            app="Pynchon::PLAN", stage=f"plugin:{self.__class__.name}"
        )
        plan = self.Plan()
        app.status_bar.update(app="Pynchon", stage=f"{len(plan)}")
        return plan

    def apply(self, plan: planning.Plan = None) -> planning.ApplyResults:
        """
        Executes the plan for this plugin
        """
        cls_name = self.__class__.name
        msg = f"Applying for plugin '{cls_name}'"
        app.status_bar.update(
            app="Pynchon::APPLY", stage=f"plugin:{self.__class__.name}"
        )
        plan = plan or self.plan()
        goals = getattr(plan, "goals", plan)
        results = []
        total = len(goals)
        LOGGER.critical(f"{msg} ({total} goals)")
        git = self.siblings["git"]
        for i, action_item in enumerate(goals):
            app.status_bar.update(stage=f"{action_item}")
            cmd = action_item.command
            ordering = f"  {i+1}/{total}"
            prev_changes = git.modified
            invocation = invoke(cmd)
            rsrc_path = abcs.Path(action_item.resource).absolute()
            next_changes = [path.absolute() for path in git.modified]
            changed = all(
                [
                    rsrc_path in next_changes,
                    # rsrc_path not in prev_changes,
                ]
            )
            # raise Exception([changed,action_item.resource, next_changes])
            tmp = planning.Action(
                ok=invocation.succeeded,
                ordering=ordering,
                error="" if invocation.succeeded else invocation.stderr,
                # log=invocation.succeeded and invocation.stderr else None,
                owner=action_item.owner,
                command=action_item.command,
                resource=action_item.resource,
                type=action_item.type,
                changed=changed,
            )
            lme.CONSOLE.print(tmp)
            results.append(tmp)
        results = planning.ApplyResults(results)
        # write status event (used by the app-console)
        app.status_bar.update(
            app="Pynchon::HOOKS",
            stage=f"{cls_name}",
        )
        resources = list({r.resource for r in results})
        LOGGER.critical(f"Finished apply ({len(resources)} resources)")
        hooks = self.apply_hooks
        if hooks:
            self.logger.warning(
                f"{self.__class__} is dispatching {len(hooks)} hooks: {hooks}"
            )
            hook_results = []
            for hook in hooks:
                hook_results.append(self.run_hook(hook, results))
        else:
            self.logger.warning("No applicable hooks were found")
        return results

    def _validate_hooks(self, hooks):
        # FIXME: validation elsewhere
        for x in hooks:
            assert isinstance(x, (str,))
            assert " " not in x
            assert "_" not in x
            assert x.strip()

    @memoized_property
    def apply_hooks(self):
        """ """
        hooks = [x for x in self.hooks if x.split("-")[-1] == "apply"]
        apply_hooks = self["apply_hooks"::[]]
        hooks += [
            x + ("-apply" if not x.endswith("-apply") else "") for x in apply_hooks
        ]
        hooks = list(set(hooks))
        self._validate_hooks(hooks)
        return hooks

    @memoized_property
    def hooks(self):
        """ """
        hooks = self["hooks"::[]]
        self._validate_hooks(hooks)
        return hooks

    def _hook_open_after_apply(self, result: planning.ApplyResults) -> bool:
        """ """
        changes = list({r.resource for r in result})
        changes = [abcs.Path(rsrc) for rsrc in changes]
        changes = [rsrc for rsrc in changes if not rsrc.is_dir()]
        self.logger.warning(f"Opening {len(changes)} changed resources.")
        docs_plugin = self if self.name == "docs" else self.siblings["docs"]
        for ch in changes:
            docs_plugin.open(ch)
        return True

    @typing.validate_arguments
    def run_hook(self, hook_name: str, results: planning.ApplyResults):
        """
        :param hook_name: str:
        :param results: planning.ApplyResults:
        """

        class HookNotFound(Exception):
            pass

        class HookFailed(RuntimeError):
            pass

        norml_hook_name = hook_name.replace("-", "_")
        fxn_name = f"_hook_{norml_hook_name}"
        hook_fxn = getattr(self, fxn_name, None)
        if hook_fxn is None:
            err = [self.__class__, [hook_name, fxn_name]]
            self.logger.critical(err)
            raise HookNotFound(err)
        hook_result = hook_fxn(results)
        self.logger.critical(hook_result)
        return hook_result


class ShyPlanner(AbstractPlanner):
    """ShyPlanner uses plan/apply workflows, but they must be
    executed directly.  ProjectPlugin (or any other parent plugins)
    won't include this as a sub-plan.


    """

    contribute_plan_apply = False


@tags(cli_label="Manager")
class Manager(ShyPlanner):
    cli_label = "Manager"


class ResourceManager(Manager):
    @property
    def changes(self):
        """Set(git_changes).intersection(plugin_resources)"""
        git = self.siblings["git"]
        changes = git.modified
        these_changes = set(changes).intersection(set(self.list(changes=False)))
        return dict(modified=list(these_changes))

    @tagging.tags(click_aliases=["ls"])
    @cli.click.option(
        "--changes",
        "-m",
        "changes",
        is_flag=True,
        default=False,
        help="returns the git-modified subset",
    )
    def list(self, changes: bool = False):
        """Lists resources associated with this plugin"""
        if changes:
            return self.changes["modified"]
        from pynchon import abcs
        from pynchon.util import files

        try:
            include_patterns = self["include_patterns"]
            root = self["root"]
        except (KeyError,) as exc:
            self.logger.critical(
                f"{self.__class__} tried to use self.list(), but does not follow protocol"
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


class Planner(ShyPlanner):
    """Planner uses plan/apply workflows, and contributes it's plans
    to ProjectPlugin (or any other parent plugins).
    """

    contribute_plan_apply = True
