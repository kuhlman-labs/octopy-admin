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

    def get_repo_collaborators_with_permission(self, owner, name):
        """
        This module returns a generator that will yield a dictionary
         of all collaborators in a repository.

        Attributes:
            owner (str): The name of the Organization.
            name (str): The name of the Repository.
        """
        query = self._load_query("gql_files/get-repo-collaborators-with-permission.gql")
        params = {"owner": owner, "name": name, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_branch_protection_rules(self, owner, name):
        """
        This module returns a generator that will yield a dictionary
         of all branch protection rules in a repository.

        Attributes:
            owner (str): The name of the Organization.
            name (str): The name of the Repository.
        """
        query = self._load_query("gql_files/get-repo-branch-protection-rules.gql")
        params = {"owner": owner, "name": name, "cursor": None}
        return self._paginate_results(query, params)

    def get_the_authenticated_user(self):
        """
        This module returns a dictionary with the login
        of the currently authenticated user.
        """
        query = self._load_query("gql_files/get-the-authenticated-user.gql")
        return self._execute(query)

    def get_org_members_with_role(self, org):
        """
        This module returns a generator that will yield a dictionary
         of all members in an organization.

        Attributes:
            org (str): The name of the Organization.
        """
        query = self._load_query("gql_files/get-org-members-with-role.gql")
        params = {"organization": org, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_prs(self, owner, name):
        """
        This module returns a generator that will yield a dictionary
         of all pull requests in a repository.

        Attributes:
            owner (str): The name of the Organization.
            name (str): The name of the Repository.
        """
        query = self._load_query("gql_files/get-repo-prs.gql")
        params = {"owner": owner, "name": name, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_pr_review_requested_events(self, owner, name):
        """
        This module returns a generator that will yield a dictionary
         of all pull request review requested events in a repository.

        Attributes:
            owner (str): The name of the Organization.
            name (str): The name of the Repository.
        """
        query = self._load_query("gql_files/get-repo-pr-review-requested-events.gql")
        params = {"owner": owner, "name": name, "cursor": None}
        return self._paginate_results(query, params)

    def get_enterprise_admins(self, enterprise):
        """
        This module returns a generator that will yield a dictionary
         of all admins in an Enterprise.

        Attributes:
            enterprise (str): The name of the Enterprise.
        """
        query = self._load_query("gql_files/get-enterprise-admins.gql")
        params = {"slug": enterprise, "cursor": None}
        return self._paginate_results(query, params)

    def get_users_public_repos(self, user):
        """
        This method returns a generator that will yield a dictionary
        of all public repos for a given user.
        """
        query = self._load_query("gql_files/get-users-public-repos.gql")
        params = {"user": user, "cursor": None}
        return self._paginate_results(query, params)

    def get_enterprise_members(self, slug):
        """
        This method returns a generator that will yield a dictionary
        of all members for a given enterprise.
        """
        query = self._load_query("gql_files/get-enterprise-members.gql")
        params = {"slug": slug, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_languages(self, owner, name):
        """
        This method returns a generator that will yield a dictionary
        of all languages for a given repository.
        """
        query = self._load_query("gql_files/get-repo-languages.gql")
        params = {"owner": owner, "name": name, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_id(self, owner, name):
        """
        This method returns a dictionary of the ID for a given repository.
        """
        query = self._load_query("gql_files/get-repo-id.gql")
        params = {"owner": owner, "name": name}
        return self._execute(query, params)

    def get_enterprise_id(self, slug):
        """
        This method returns a dictionary of the ID for a given enterprise.
        """
        query = self._load_query("gql_files/get-enterprise-id.gql")
        params = {"slug": slug}
        return self._execute(query, params)
