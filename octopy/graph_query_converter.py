"""
This module is used to convert a GraphQL query to more native Python types.
"""

from .graph_query import GraphQuery
from .graph_request import GraphRequestError


class GraphQueryConverter(GraphQuery):
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

    def get_repo_branch_protection_rule_list(self, org, repo):
        """
        This module returns a list of all branch protection rules
        in a repository.

        Attributes:
            org (str): The name of the Organization.
            repo (str): The name of the Repository.
        """
        branch_protection_rule_list = []
        try:
            branch_protection_rule_results = self.get_repo_branch_protection_rules(org, repo)

            for branch_protection_rules in branch_protection_rule_results:
                for branch_protection_rule in (
                    branch_protection_rules.get("repository")
                    .get("branchProtectionRules")
                    .get("nodes")
                ):
                    rules = []
                    for key, item in branch_protection_rule.items():
                        if item:
                            rules.append(f"{key}: {item}")
                    branch_protection_rule_list.append(rules)
        except GraphRequestError as err:
            print(err)
        return branch_protection_rule_list
