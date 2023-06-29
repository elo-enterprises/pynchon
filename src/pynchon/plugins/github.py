""" pynchon.plugins.github
"""
import webbrowser

from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)

option_api_token = cli.click.option(
    "--api-token", "-t", "token", default="", help="defaults to $GITHUB_API_TOKEN"
)


@tagging.tags(click_aliases=["gh"])
class GitHub(models.ToolPlugin):
    """Tools for working with GitHub"""

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] =  "github"
        defaults = dict(enterprise=False)

        @property
        def org_name(self):
            from pynchon.config import git

            return git.github_org

    name = "github"
    cli_name = "github"
    cli_aliases = []

    @cli.click.option("--org", "-o")
    def open(self, org=None):
        """Opens org/repo github in a webbrowser

        :param org: Default value = None)

        """
        org_name = self["org_name"]
        url = f"https://github.com/{org_name}"
        if not org:
            repo_name = self[:"git.repo_name":]
            url = f"{url}/{repo_name}"
        return webbrowser.open(url)

    @cli.options.org_name
    @option_api_token
    def clone_org(self, org_name: str = None, token: str = None):  # noqa
        """Clones an entire github-org

        :param org_name: str:  (Default value = None)
        :param token: str:  (Default value = None)
        :param org_name: str:  (Default value = None)
        :param token: str:  (Default value = None)

        """
        raise NotImplementedError()

    @cli.click.argument("repo")
    @option_api_token
    def clone(self, repo: str, token: str = None):  # noqa
        """Clones a single repo from this project's org

        :param repo: str:
        :param token: str:  (Default value = None)
        :param repo: str:
        :param token: str:  (Default value = None)

        """
        raise NotImplementedError()

    # @cli.click.argument('repo')
    @tagging.tags(click_aliases=["pr"])
    @option_api_token
    def pull_request(self, repo: str, token: str = None):  # noqa
        """Creates a pull-request from this branch

        :param repo: str:
        :param token: str:  (Default value = None)
        :param repo: str:
        :param token: str:  (Default value = None)

        """
        raise NotImplementedError()

    @tagging.tags(click_aliases=["codeowners"])
    # @option_api_token
    def code_owners(self, repo: str, token: str = None):  # noqa
        """Describes code-owners for changes or for working-dir

        :param repo: str:
        :param token: str:  (Default value = None)
        :param repo: str:
        :param token: str:  (Default value = None)

        """
        raise NotImplementedError()
