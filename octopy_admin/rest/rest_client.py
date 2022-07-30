"""
This module containst the RestClient class.
"""

import os

import requests

from . import apis


class RestClientError(Exception):
    """
    Exception raised when a REST request fails.
    """


class RestClient:
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes
    """
    The following methods are used to form requests to the GitHub REST API.
    """

    def __init__(self, rest_api_url=None, api_token=None):
        """
        Initialize the REST client to make requests to the GitHub API.

        Attributes:
            headers (dict): Headers to be used in the requests.
            base_url (str): Base URL of the GitHub API.
            API_TOKEN (str): GitHub API token.
            REST_API_URL (str): GitHub REST API URL.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise RestClientError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        if rest_api_url is None:
            rest_api_url = os.environ.get("REST_API_URL", r"https://api.github.com")
        self._base_url = rest_api_url

        self.actions = apis.actions.Actions(self)
        self.activity = apis.activity.Activity(self)
        self.apps = apis.apps.Apps(self)
        self.billing = apis.billing.Billing(self)
        self.checks = apis.checks.Checks(self)
        self.code_scanning = apis.code_scanning.CodeScanning(self)
        self.codes_of_conduct = apis.codes_of_conduct.CodesOfConduct(self)
        self.codespaces = apis.codespaces.Codespaces(self)
        self.dependabot = apis.dependabot.Dependabot(self)
        self.dependency_graph = apis.dependency_graph.DependencyGraph(self)
        self.emojis = apis.emojis.Emojis(self)
        self.enterprise_admin = apis.enterprise_admin.EnterpriseAdmin(self)
        self.gists = apis.gists.Gists(self)
        self.git = apis.git.Git(self)
        self.gitignore = apis.gitignore.Gitignore(self)
        self.interactions = apis.interactions.Interactions(self)
        self.issues = apis.issues.Issues(self)
        self.licenses = apis.licenses.Licenses(self)
        self.markdown = apis.markdown.Markdown(self)
        self.meta = apis.meta.Meta(self)
        self.migrations = apis.migrations.Migrations(self)
        self.oauth_authorizations = apis.oauth_authorizations.OauthAuthorizations(self)
        self.oidc = apis.oidc.Oidc(self)
        self.orgs = apis.orgs.Orgs(self)
        self.packages = apis.packages.Packages(self)
        self.projects = apis.projects.Projects(self)
        self.pulls = apis.pulls.Pulls(self)
        self.rate_limit = apis.rate_limit.RateLimit(self)
        self.reactions = apis.reactions.Reactions(self)
        self.repos = apis.repos.Repos(self)
        self.scim = apis.scim.Scim(self)
        self.search = apis.search.Search(self)
        self.secret_scanning = apis.secret_scanning.SecretScanning(self)
        self.server_statistics = apis.server_statistics.ServerStatistics(self)
        self.teams = apis.teams.Teams(self)
        self.users = apis.users.Users(self)

    def _execute(self, method, url, payload):
        """
        Execute a request.

        Attributes:
            method (str): HTTP method.
            url (str): URL.
            payload (dict): Payload.
        """
        try:
            response = requests.request(method=method, url=url, json=payload, headers=self._headers)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as errtimeout:
            raise RestClientError(f"Timeout error: {errtimeout}") from errtimeout
        except requests.exceptions.HTTPError as errhttp:
            raise RestClientError(f"HTTP error: {errhttp}") from errhttp
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestClientError(f"Too many redirects: {errredirect}") from errredirect
        except requests.exceptions.RequestException as errexcept:
            raise RestClientError(f"Unexpected error: {errexcept}") from errexcept
