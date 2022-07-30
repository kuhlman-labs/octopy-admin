"""
Owner or admin management of users interactions.
"""


class Interactions:
    """
    Owner or admin management of users interactions.
    """

    def __init__(self, client):
        """
        Initialize the Interactions class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_interaction_restrictions_for_an_organization(self, org, **payload):
        """
        Get interaction restrictions for an organization
        https://docs.github.com/rest/reference/interactions#get-interaction-restrictions-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/interaction-limits"
        response = self._execute("get", url, payload)
        return response

    def set_interaction_restrictions_for_an_organization(self, org, **payload):
        """
        Set interaction restrictions for an organization
        https://docs.github.com/rest/reference/interactions#set-interaction-restrictions-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/interaction-limits"
        response = self._execute("put", url, payload)
        return response

    def remove_interaction_restrictions_for_an_organization(self, org, **payload):
        """
        Remove interaction restrictions for an organization
        https://docs.github.com/rest/reference/interactions#remove-interaction-restrictions-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/interaction-limits"
        response = self._execute("delete", url, payload)
        return response

    def get_interaction_restrictions_for_a_repository(self, owner, repo, **payload):
        """
        Get interaction restrictions for a repository
        https://docs.github.com/rest/reference/interactions#get-interaction-restrictions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/interaction-limits"
        response = self._execute("get", url, payload)
        return response

    def set_interaction_restrictions_for_a_repository(self, owner, repo, **payload):
        """
        Set interaction restrictions for a repository
        https://docs.github.com/rest/reference/interactions#set-interaction-restrictions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/interaction-limits"
        response = self._execute("put", url, payload)
        return response

    def remove_interaction_restrictions_for_a_repository(self, owner, repo, **payload):
        """
        Remove interaction restrictions for a repository
        https://docs.github.com/rest/reference/interactions#remove-interaction-restrictions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/interaction-limits"
        response = self._execute("delete", url, payload)
        return response

    def get_interaction_restrictions_for_your_public_repositories(self, **payload):
        """
        Get interaction restrictions for your public repositories
        https://docs.github.com/rest/reference/interactions#get-interaction-restrictions-for-your-public-repositories
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/interaction-limits"
        response = self._execute("get", url, payload)
        return response

    def set_interaction_restrictions_for_your_public_repositories(self, **payload):
        """
        Set interaction restrictions for your public repositories
        https://docs.github.com/rest/reference/interactions#set-interaction-restrictions-for-your-public-repositories
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/interaction-limits"
        response = self._execute("put", url, payload)
        return response

    def remove_interaction_restrictions_from_your_public_repositories(self, **payload):
        """
        Remove interaction restrictions from your public repositories
        https://docs.github.com/rest/reference/interactions#remove-interaction-restrictions-from-your-public-repositories
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/interaction-limits"
        response = self._execute("delete", url, payload)
        return response
