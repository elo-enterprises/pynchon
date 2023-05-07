""" pynchon.plugins.Core
"""
from pynchon import abcs, api, cli, models
from pynchon.bin import entry
from pynchon.core import Config as CoreConfig
from pynchon.util import files, lme, typing

LOGGER = lme.get_logger(__name__)


class Core(models.Planner):
    """Core Plugin"""

    name = "core"
    priority = -1
    config_class = CoreConfig

    # NB: prevents recursion when `pynchon plan` is used!
    contribute_plan_apply = False

    @typing.classproperty
    def click_group(kls):
        """ """
        kls._finalized_click_groups[kls] = entry.entry
        return kls._finalized_click_groups[kls]

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod

        result = getattr(config_mod, kls.get_config_key())
        return result

    def cfg(self):
        """Show current project config (with templating/interpolation)"""
        return self.project_config

    @cli.click.option('--bash', default=False, is_flag=True, help='bootstrap bash')
    @cli.click.option('--bashrc', default=False, is_flag=True, help='bootstrap bashrc')
    @cli.click.option('--tox', default=False, is_flag=True, help='bootstrap tox')
    def bootstrap(
        self,
        bash: bool = False,
        bashrc: bool = False,
        tox: bool = False,
    ) -> None:
        """
        Bootstrap for shell integration, etc
        """
        pynchon_completions_script = '.tmp.pynchon.completions.sh'
        bashrc_snippet = f'.tmp.pynchon.bashrc'

        if bash:
            import collections

            gr = self.__class__.click_group
            all_known_subcommands = [
                ' '.join(x.split()[1:])
                for x in cli.click.walk_group(gr, path='pynchon').keys()
            ]
            head = [x for x in all_known_subcommands if len(x.split()) == 1]
            rest = [x for x in all_known_subcommands if x not in head]
            tmp = collections.defaultdict(list)
            for phrase in rest:
                bits = phrase.split()
                k = bits.pop(0)
                tmp[k] += bits
            rest = [
                f"""    '{k}'*)
              while read -r; do COMPREPLY+=( "$REPLY" ); done < <( compgen -W "$(_pynchon_completions_filter "{' '.join(subs)}")" -- "$cur" )
              ;;
            """
                for k, subs in tmp.items()
            ]
            rest += [
                f"""    *)
      while read -r; do COMPREPLY+=( "$REPLY" ); done < <( compgen -W "$(_pynchon_completions_filter "{' '.join(head)}")" -- "$cur" )
      ;;"""
            ]
            # LOGGER.warning("This is intended to be run through a pipe, as in:")
            # LOGGER.critical("pynchon bootstrap --bash | bash")
            tmpl = api.render.get_template('pynchon/bootstrap/bash.sh')
            content = tmpl.render(head=head, rest="\n".join(rest), **self.config)
            files.dumps(content=content, file=pynchon_completions_script)
            LOGGER.warning(
                f"To refresh your shell, run: `source {pynchon_completions_script}`"
            )
            return dict()
        if bashrc:
            LOGGER.critical(
                "To use completion hints every time they are "
                "present in a folder, adding this to .bashrc:"
            )
            tmpl = api.render.get_template('pynchon/bootstrap/bashrc.sh')
            content = tmpl.render(pynchon_completions_script=pynchon_completions_script)
            files.dumps(content=content, file=bashrc_snippet, logger=LOGGER.info)
            return files.block_in_file(
                target_file=abcs.Path("~/.bashrc").expanduser(),
                block_file=bashrc_snippet,
            )
        elif tox:
            result = api.render.get_template('pynchon/tox.ini')
            raise NotImplementedError()

    def raw(self) -> None:
        """
        Returns (almost) raw config,
        without interpolation
        """
        from pynchon.config import RAW

        return RAW

    def plan(
        self,
        config=None,
    ) -> models.Plan:
        """Runs plan for all plugins"""

        config = config or self.project_config
        plan = super(self.__class__, self).plan(config)
        plugins = self.active_plugins
        plugins = [p for p in plugins if isinstance(p, models.AbstractPlanner)]
        self.logger.critical(f"Planning on behalf of: {[p.name for p in plugins]}")
        for plugin_obj in plugins:
            if not plugin_obj.contribute_plan_apply:
                continue
            self.logger.critical("=" * 20 + plugin_obj.name)
            subplan = plugin_obj.plan()
            if not subplan:
                self.logger.warning(f'subplan for {plugin_obj} is empty!')
            else:
                for g in subplan:
                    self.logger.info(f'{plugin_obj} contributes {g}')
                    plan.append(g)
        return plan
