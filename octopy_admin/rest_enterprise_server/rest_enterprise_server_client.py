"""
This module contains the RestEnterpriseServerClient class.
"""

import os

import requests

from . import apis_enterprise_server


class RestEnterpriseServerClientError(Exception):
    """
    Exception raised when a REST request fails.
    """


class RestEnterpriseServerClient:
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-statements
    # pylint: disable=duplicate-code
    # pylint: disable=too-many-arguments
    """
    The following methods are used to form requests to the GitHub Enterprise Server REST API.
    """

    def __init__(self, hostname=None, api_token=None, verify=None):
        """
        Initialize the REST client to make requests to the GitHub Enterprise Server API.

        Attributes:
            api_token (str): GitHub Enterprise Server API token.
            hostname (str): GitHub Enterprise Server Hostname. Example: ghes.example.com
            verify (bool): Verify SSL certificate.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise RestEnterpriseServerClientError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        if hostname is None:
            hostname = os.environ.get("GHE_HOSTNAME")
            if os.environ.get("GHE_HOSTNAME") is None:
                raise RestEnterpriseServerClientError(
                    "GHE_HOSTNAME environment variable is not set"
                )
            rest_api_url = "https://" + hostname + "/api/v3"
        elif hostname:
            rest_api_url = "https://" + hostname + "/api/v3"

        self._base_url = rest_api_url
        self._verify = verify
        self.actions = apis_enterprise_server.actions.Actions(self)
        self.activity = apis_enterprise_server.activity.Activity(self)
        self.apps = apis_enterprise_server.apps.Apps(self)
        self.billing = apis_enterprise_server.billing.Billing(self)
        self.checks = apis_enterprise_server.checks.Checks(self)
        self.code_scanning = apis_enterprise_server.code_scanning.CodeScanning(self)
        self.codes_of_conduct = apis_enterprise_server.codes_of_conduct.CodesOfConduct(self)
        self.codespaces = apis_enterprise_server.codespaces.Codespaces(self)
        self.dependabot = apis_enterprise_server.dependabot.Dependabot(self)
        self.dependency_graph = apis_enterprise_server.dependency_graph.DependencyGraph(self)
        self.emojis = apis_enterprise_server.emojis.Emojis(self)
        self.enterprise_admin = apis_enterprise_server.enterprise_admin.EnterpriseAdmin(self)
        self.gists = apis_enterprise_server.gists.Gists(self)
        self.git = apis_enterprise_server.git.Git(self)
        self.gitignore = apis_enterprise_server.gitignore.Gitignore(self)
        self.interactions = apis_enterprise_server.interactions.Interactions(self)
        self.issues = apis_enterprise_server.issues.Issues(self)
        self.licenses = apis_enterprise_server.licenses.Licenses(self)
        self.markdown = apis_enterprise_server.markdown.Markdown(self)
        self.merge_queue = apis_enterprise_server.merge_queue.MergeQueue(self)
        self.meta = apis_enterprise_server.meta.Meta(self)
        self.migrations = apis_enterprise_server.migrations.Migrations(self)
        self.oauth_authorizations = apis_enterprise_server.oauth_authorizations.OauthAuthorizations(
            self
        )
        self.orgs = apis_enterprise_server.orgs.Orgs(self)
        self.packages = apis_enterprise_server.packages.Packages(self)
        self.projects = apis_enterprise_server.projects.Projects(self)
        self.pulls = apis_enterprise_server.pulls.Pulls(self)
        self.rate_limit = apis_enterprise_server.rate_limit.RateLimit(self)
        self.reactions = apis_enterprise_server.reactions.Reactions(self)
        self.repos = apis_enterprise_server.repos.Repos(self)
        self.search = apis_enterprise_server.search.Search(self)
        self.secret_scanning = apis_enterprise_server.secret_scanning.SecretScanning(self)
        self.server_statistics = apis_enterprise_server.server_statistics.ServerStatistics(self)
        self.teams = apis_enterprise_server.teams.Teams(self)
        self.users = apis_enterprise_server.users.Users(self)
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
            raise RestEnterpriseServerClientError(f"Timeout error: {errtimeout}") from errtimeout
        except requests.exceptions.HTTPError as errhttp:
            raise RestEnterpriseServerClientError(f"HTTP error: {errhttp}") from errhttp
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestEnterpriseServerClientError(
                f"Too many redirects: {errredirect}"
            ) from errredirect
        except requests.exceptions.RequestException as errexcept:
            raise RestEnterpriseServerClientError(f"Unexpected error: {errexcept}") from errexcept
