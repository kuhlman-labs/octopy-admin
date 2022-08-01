"""
This module is used to make queries through the GitHub GraphQL API.
"""


class GraphQuery:
    """
    This class is used to get the data from the GraphQL API.
    """

    def __init__(self, client):
        """
        Initialize the GraphQuery class.
        """
        self._execute = client._execute
        self._load_query = client._load_query

    def _get_page_info(self, results):
        """
        This module returns a dictionary of the page info from a GraphQL query.

        Attributes:
            results (dict): The results of a GraphQL query.
        """
        while results.get("pageInfo") is None:
            for _, item in results.items():
                if isinstance(item, dict):
                    if item.get("pageInfo") is None:
                        results = item
                        return self._get_page_info(results)
                    return item.get("pageInfo")

    def _get_nodes(self, results):
        """
        This module returns a list of nodes from a GraphQL query.

        Attributes:
            results (dict): The results of a GraphQL query.
        """

        while results.get("nodes") or results.get("edges") is None:
            for _, item in results.items():
                if isinstance(item, dict):
                    if item.get("nodes"):
                        return item.get("nodes")
                    if item.get("nodes") == []:
                        return []
                    if item.get("edges"):
                        return item.get("edges")
                    if item.get("edges") == []:
                        return []
                    return self._get_nodes(item)

    def _paginate_results(self, query, params):
        """
        This method returns a generator that will yield a dictionary
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

    def results_to_list(self, results):
        """
        This method returns a list of all results from the nodes or
        edges field in a GraphQL query.

        Attributes:
            results (dict): The results of a GraphQL query.
        """
        result_list = []
        for result in results:
            if self._get_nodes(result):
                result_list.extend(self._get_nodes(result))
        return result_list

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

    def get_repo_branch_protection_rules(self, org, repo):
        """
        This module returns a generator that will yield a dictionary
         of all branch protection rules in a repository.

        Attributes:
            org (str): The name of the Organization.
            repo (str): The name of the Repository.
        """
        query = self._load_query("gql_files/get-repo-branch-protection-rules.gql")
        params = {"owner": org, "name": repo, "cursor": None}
        return self._paginate_results(query, params)
