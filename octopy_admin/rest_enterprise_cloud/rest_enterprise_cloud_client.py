"""
This module contains the RestEnterpriseCloudClient class.
"""

import os

import requests

from . import apis_enterprise_cloud


class RestEnterpriseCloudClientError(Exception):
    """
    Exception raised when a REST request fails.
    """


class RestEnterpriseCloudClient:
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-statements
    # pylint: disable=duplicate-code
    # pylint: disable=too-many-arguments
    """
    The following methods are used to form requests to the GitHub REST API.
    """

    def __init__(self, api_token=None, verify=None):
        """
        Initialize the REST client to make requests to the GitHub API.

        Attributes:
            api_token (str): GitHub API token.
            verify (bool): Verify SSL certificate.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise RestEnterpriseCloudClientError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        rest_api_url = "https://api.github.com"

        self._base_url = rest_api_url
        self._verify = verify
        self.actions = apis_enterprise_cloud.actions.Actions(self)
        self.activity = apis_enterprise_cloud.activity.Activity(self)
        self.apps = apis_enterprise_cloud.apps.Apps(self)
        self.billing = apis_enterprise_cloud.billing.Billing(self)
        self.checks = apis_enterprise_cloud.checks.Checks(self)
        self.code_scanning = apis_enterprise_cloud.code_scanning.CodeScanning(self)
        self.codes_of_conduct = apis_enterprise_cloud.codes_of_conduct.CodesOfConduct(self)
        self.codespaces = apis_enterprise_cloud.codespaces.Codespaces(self)
        self.dependabot = apis_enterprise_cloud.dependabot.Dependabot(self)
        self.dependency_graph = apis_enterprise_cloud.dependency_graph.DependencyGraph(self)
        self.emojis = apis_enterprise_cloud.emojis.Emojis(self)
        self.enterprise_admin = apis_enterprise_cloud.enterprise_admin.EnterpriseAdmin(self)
        self.gists = apis_enterprise_cloud.gists.Gists(self)
        self.git = apis_enterprise_cloud.git.Git(self)
        self.gitignore = apis_enterprise_cloud.gitignore.Gitignore(self)
        self.interactions = apis_enterprise_cloud.interactions.Interactions(self)
        self.issues = apis_enterprise_cloud.issues.Issues(self)
        self.licenses = apis_enterprise_cloud.licenses.Licenses(self)
        self.markdown = apis_enterprise_cloud.markdown.Markdown(self)
        self.merge_queue = apis_enterprise_cloud.merge_queue.MergeQueue(self)
        self.meta = apis_enterprise_cloud.meta.Meta(self)
        self.migrations = apis_enterprise_cloud.migrations.Migrations(self)
        self.oidc = apis_enterprise_cloud.oidc.Oidc(self)
        self.orgs = apis_enterprise_cloud.orgs.Orgs(self)
        self.packages = apis_enterprise_cloud.packages.Packages(self)
        self.projects = apis_enterprise_cloud.projects.Projects(self)
        self.pulls = apis_enterprise_cloud.pulls.Pulls(self)
        self.rate_limit = apis_enterprise_cloud.rate_limit.RateLimit(self)
        self.reactions = apis_enterprise_cloud.reactions.Reactions(self)
        self.repos = apis_enterprise_cloud.repos.Repos(self)
        self.scim = apis_enterprise_cloud.scim.Scim(self)
        self.search = apis_enterprise_cloud.search.Search(self)
        self.secret_scanning = apis_enterprise_cloud.secret_scanning.SecretScanning(self)
        self.server_statistics = apis_enterprise_cloud.server_statistics.ServerStatistics(self)
        self.teams = apis_enterprise_cloud.teams.Teams(self)
        self.users = apis_enterprise_cloud.users.Users(self)
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
            raise RestEnterpriseCloudClientError(f"Timeout error: {errtimeout}") from errtimeout
        except requests.exceptions.HTTPError as errhttp:
            raise RestEnterpriseCloudClientError(f"HTTP error: {errhttp}") from errhttp
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestEnterpriseCloudClientError(
                f"Too many redirects: {errredirect}"
            ) from errredirect
        except requests.exceptions.RequestException as errexcept:
            raise RestEnterpriseCloudClientError(f"Unexpected error: {errexcept}") from errexcept
