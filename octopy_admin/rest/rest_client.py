"""
This module contains the RestClient class.
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
    # pylint: disable=too-many-statements
    # pylint: disable=duplicate-code
    # pylint: disable=too-many-arguments
    """
    The following methods are used to form requests to the GitHub REST API.
    """

    def __init__(self, hostname=None, api_token=None, verify=None):
        """
        Initialize the REST client to make requests to the GitHub API.
        Attributes:
            api_token (str): GitHub API token.
            hostname (str): GitHub URL Slug (only needed if using GHES).
            verify (bool): Verify SSL certificate.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise RestClientError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        if hostname is None:
            hostname = os.environ.get("GHE_HOSTNAME")
            if os.environ.get("GHE_HOSTNAME") is None:
                rest_api_url = "https://api.github.com"
            else:
                rest_api_url = "https://" + hostname + "/api/v3"
        elif hostname:
            rest_api_url = "https://" + hostname + "/api/v3"

        self._base_url = rest_api_url
        self._verify = verify
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
        self.merge_queue = apis.merge_queue.MergeQueue(self)
        self.meta = apis.meta.Meta(self)
        self.migrations = apis.migrations.Migrations(self)
        self.orgs = apis.orgs.Orgs(self)
        self.packages = apis.packages.Packages(self)
        self.projects = apis.projects.Projects(self)
        self.pulls = apis.pulls.Pulls(self)
        self.rate_limit = apis.rate_limit.RateLimit(self)
        self.reactions = apis.reactions.Reactions(self)
        self.repos = apis.repos.Repos(self)
        self.search = apis.search.Search(self)
        self.secret_scanning = apis.secret_scanning.SecretScanning(self)
        self.server_statistics = apis.server_statistics.ServerStatistics(self)
        self.teams = apis.teams.Teams(self)
        self.users = apis.users.Users(self)
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
                verify=self._verify,
            )
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
