"""
This module contains the RestPublicClient class.
"""

import os

import requests

from . import apis_public


class RestPublicClientError(Exception):
    """
    Exception raised when a REST request fails.
    """


class RestPublicClient:
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-statements
    # pylint: disable=duplicate-code
    """
    The following methods are used to form requests to the GitHub REST API.
    """

    def __init__(self, api_token=None):
        """
        Initialize the REST client to make requests to the GitHub API.

        Attributes:
            api_token (str): GitHub API token.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise RestPublicClientError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        rest_api_url = "https://api.github.com"

        self._base_url = rest_api_url
        self.actions = apis_public.actions.Actions(self)
        self.activity = apis_public.activity.Activity(self)
        self.apps = apis_public.apps.Apps(self)
        self.billing = apis_public.billing.Billing(self)
        self.checks = apis_public.checks.Checks(self)
        self.code_scanning = apis_public.code_scanning.CodeScanning(self)
        self.codes_of_conduct = apis_public.codes_of_conduct.CodesOfConduct(self)
        self.codespaces = apis_public.codespaces.Codespaces(self)
        self.dependabot = apis_public.dependabot.Dependabot(self)
        self.dependency_graph = apis_public.dependency_graph.DependencyGraph(self)
        self.emojis = apis_public.emojis.Emojis(self)
        self.enterprise_admin = apis_public.enterprise_admin.EnterpriseAdmin(self)
        self.gists = apis_public.gists.Gists(self)
        self.git = apis_public.git.Git(self)
        self.gitignore = apis_public.gitignore.Gitignore(self)
        self.interactions = apis_public.interactions.Interactions(self)
        self.issues = apis_public.issues.Issues(self)
        self.licenses = apis_public.licenses.Licenses(self)
        self.markdown = apis_public.markdown.Markdown(self)
        self.meta = apis_public.meta.Meta(self)
        self.migrations = apis_public.migrations.Migrations(self)
        self.orgs = apis_public.orgs.Orgs(self)
        self.packages = apis_public.packages.Packages(self)
        self.projects = apis_public.projects.Projects(self)
        self.pulls = apis_public.pulls.Pulls(self)
        self.rate_limit = apis_public.rate_limit.RateLimit(self)
        self.reactions = apis_public.reactions.Reactions(self)
        self.repos = apis_public.repos.Repos(self)
        self.search = apis_public.search.Search(self)
        self.secret_scanning = apis_public.secret_scanning.SecretScanning(self)
        self.server_statistics = apis_public.server_statistics.ServerStatistics(self)
        self.teams = apis_public.teams.Teams(self)
        self.users = apis_public.users.Users(self)
        print("REST API URL:", rest_api_url)

    def paginate_request(self, response):
        """
        Paginate a request.

        Attributes:
            response (obj): API request.
        """
        if response.links.get("next") is None and response:
            yield response.json()
        while response.links.get("next"):
            yield response.json()
            url = response.links.get("next").get("url")
            response = self._execute("GET", url)

    def _execute(self, method, url, payload=None, params=None):
        """
        Execute a request.

        Attributes:
            method (str): HTTP method.
            url (str): URL.
            payload (dict): Payload.
        """
        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=payload,
                headers=self._headers,
                timeout=10,
            )
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as errtimeout:
            raise RestPublicClientError(f"Timeout error: {errtimeout}") from errtimeout
        except requests.exceptions.HTTPError as errhttp:
            raise RestPublicClientError(f"HTTP error: {errhttp}") from errhttp
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestPublicClientError(f"Too many redirects: {errredirect}") from errredirect
        except requests.exceptions.RequestException as errexcept:
            raise RestPublicClientError(f"Unexpected error: {errexcept}") from errexcept
