"""
This module contains the GraphQuery class.
"""
import os
from encodings import utf_8

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError, TransportServerError


class GraphRequest:  # pylint: disable=too-few-public-methods
    """
    This following methods are used to form requests to the GitHub GraphQL API.
    """

    def __init__(self, graph_api_url=None, api_token=None):
        """
        Initialize the GraphQL client.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise GraphRequestError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        if graph_api_url is None:
            graph_api_url = os.environ.get("GRAPH_API_URL", r"https://api.github.com/graphql")
        headers = {"Authorization": f"Bearer {api_token}"}
        transport = AIOHTTPTransport(
            url=graph_api_url,
            headers=headers,
        )
        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def _load_query(self, path):
        """
        Load a query from a file.

        Attributes:
            path (str): Relative path to the query file.
        """
        absolute_path = os.path.dirname(__file__)
        relative_path = path
        full_path = os.path.join(absolute_path, relative_path)
        with open(full_path, encoding=utf_8) as file:
            return gql(file.read())

    def _execute(self, query, params):
        """
        Execute a query.

        Attributes:
            query (str): GraphQL query.
            params (dict): Query parameters.
        """
        try:
            return self._client.execute(query, variable_values=params)
        except TransportQueryError as errquery:
            raise GraphRequestError(errquery.errors[0].get("message")) from errquery
        except TransportServerError as errserver:
            raise GraphRequestError(
                f"Server responded with a {str(errserver.code)} status code"
            ) from errserver


class GraphRequestError(Exception):
    """
    Exception raised when an error occurs in the GraphRequest.
    """


class GraphQueryProvider(GraphRequest):
    """
    This class is used to get the data from the GraphQL API.
    """

    def _get_page_info(self, results):
        """
        This module returns a dictionary of the page info from a GraphQL query.

        Attributes:
            results (dict): The results of a GraphQL query.
        """
        while results.get("pageInfo") is None:
            for _, item in results.items():
                if item.get("pageInfo") is None:
                    results = item
                    return self._get_page_info(results)
                return item.get("pageInfo")

    def _paginate_results(self, query, params):
        """
        This module returns a generator that will yield a dictionary
         of all results from a GraphQL query.

        Attributes:
            query (str): The GraphQL query.
            params (dict): The parameters to pass to the query.
        """
        cursor = None
        while True:
            params["cursor"] = cursor
            results = self._execute(query, params)
            page_info = self._get_page_info(results)
            next_page = page_info.get("hasNextPage")
            cursor = page_info.get("endCursor")
            yield results
            if not next_page:
                return

    def get_enterprise_orgs(self, enterprise):
        """
        This module returns a generator that will yield a dictionary
         of all organizations in an Enterprise.

        Attributes:
            enterprise (str): The name of the Enterprise.

        """
        query = self._load_query("gql_files/get-enterprise-orgs.gql")
        params = {"slug": enterprise, "cursor": None}
        return self._paginate_results(query, params)

    def get_org_repos(self, org):
        """
        This module returns a generator that will yield a dictionary
        of all repositories in an organization.

        Attributes:
            org (str): The name of the Organization.
        """
        query = self._load_query("gql_files/get-org-repos.gql")
        params = {"organization": org, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_collaborators(self, org, repo):
        """
        This module returns a generator that will yield a dictionary
         of all collaborators in a repository.

        Attributes:
            org (str): The name of the Organization.
            repo (str): The name of the Repository.
        """
        query = self._load_query("gql_files/get-repo-collaborators.gql")
        params = {"owner": org, "name": repo, "cursor": None}
        return self._paginate_results(query, params)


class GraphMutationProducer(GraphRequest):
    """
    This class is used to make mutations through the GitHub GraphQL API.
    """

    def add_enterprise_org(self, organization):
        """
        This module adds an Enterprise organization to the GitHub Enterprise.

        Attributes:
            organization (str): The name of the Organization.
        """
        params = {"organization": organization}
        query = self._load_query("gql_files/create-enterprise-org.gql")
        result = self._execute(query, params)
        return print(result)

    def add_repository(self, repository):
        """
        This module adds a repository to the GitHub Enterprise.

        Attributes:
            repository (str): The name of the Repository.
        """
        params = {"repository": repository}
        query = self._load_query("gql_files/create-repository.gql")
        result = self._execute(query, params)
        return print(result)


class GraphQueryResponseTransmuter(GraphQueryProvider):
    """
    This class is used to transform the data from the GraphQL API.
    """

    def get_org_list(self, enterprise):
        """
        This module returns a list of all organizations in an Enterprise.

        Attributes:
            enterprise (str): The name of the Enterprise.
        """
        org_list = []
        try:
            org_results = self.get_enterprise_orgs(enterprise)
            for organizations in org_results:
                for org in organizations.get("enterprise").get("organizations").get("nodes"):
                    org_list.append(org.get("name"))
        except GraphRequestError as err:
            print(err)
        return org_list

    def get_repo_list(self, org):
        """
        This module returns a list of all repositories in an organization.

        Attributes:
            org (str): The name of the Organization.
        """
        repo_list = []
        try:
            repo_results = self.get_org_repos(org)
            for repositories in repo_results:
                for repo in repositories.get("organization").get("repositories").get("edges"):
                    repo_list.append(repo.get("node").get("name"))
        except GraphRequestError as err:
            print(err)
        return repo_list

    def get_collaborators_permission_list(self, org, repo):
        """
        This module returns a list of tuples of all collaborators
        in a repository with their permission level.

        Attributes:
            org (str): The name of the Organization.
            repo (str): The name of the Repository.
        """
        collaborator_list = []
        try:
            collaborator_results = self.get_repo_collaborators(org, repo)
            for collaborators in collaborator_results:
                for collaborator in (
                    collaborators.get("repository").get("collaborators").get("edges")
                ):
                    collaborator_list.append(
                        (
                            collaborator.get("node").get("login"),
                            collaborator.get("permission"),
                        )
                    )
        except GraphRequestError as err:
            print(err)
        return collaborator_list
