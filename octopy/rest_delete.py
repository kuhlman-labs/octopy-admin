"""
This module contains the RestDelete class.
"""

from .rest_request import RestRequest


class RestDelete(RestRequest):
    """
    This Class is used to create DELETE requests.
    """

    def __init__(self, rest_api_url=None, api_token=None):
        """
        Initialize the REST client.

        Attributes:
            method (str): HTTP method.
        """
        super().__init__(rest_api_url, api_token)
        self._method = "Delete"

    def delete_user(self, username):
        """
        Delete a user. It is only available to authenticated site administrators.
        Normal users will receive a 403 response if they try to access it.

        Attributes:
            username (str): The User login to delete.
        """
        url = self._base_url + f"/admin/users/{username}"
        response = self._execute(self._method, url, None)
        return response

    def delete_repo(self, owner, repo_name):
        """
        Deleting a repository requires admin access.
        If OAuth is used, the delete_repo scope is required.

        If an organization owner has configured the organization
        to prevent members from deleting organization-owned repositories,
        you will get a 403 Forbidden response.

        Attributes:
            owner (str): The account owner of the repository. The name is not case sensitive.
            repo_name (str): The name of the repository. The name is not case sensitive.
        """
        url = self._base_url + f"/orgs/{owner}/repos/{repo_name}"
        response = self._execute(self._method, url, None)
        return response
