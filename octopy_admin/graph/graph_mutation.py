"""
This module is used to make mutations through the GitHub GraphQL API.
"""


class GraphMutation:
    """
    This class is used to make mutations through the GitHub GraphQL API.
    """

    def __init__(self, client):
        """
        Initialize the GraphMutation class.
        """
        self._execute = client._execute
        self._load_query = client._load_query

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

    def create_branch_protection_rule(self, rule):
        """
        This module adds a branch protection rule to a repository.

        Attributes:
            rule (dict): The branch protection rule.
        """
        params = {"rule": rule}
        query = self._load_query("gql_files/create-branch-protection-rule.gql")
        result = self._execute(query, params)
        return print(result)
