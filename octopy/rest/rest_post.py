"""
This module contains the RestPost class.
"""

from .rest_request import RestRequest


class RestPost(RestRequest):
    """
    This Class is used to create POST requests.
    """

    def __init__(self, rest_api_url=None, api_token=None):
        """
        Initialize the REST client.

        Attributes:
            method (str): HTTP method.
        """
        super().__init__(rest_api_url, api_token)
        self._method = "Post"

    def create_user(self, login, email):
        """
        Create a user. It is only available to authenticated site administrators.
        Normal users will receive a 403 response if they try to access it.

        Attributes:
            login (str): Login name.
            email (str): Email address.
        """
        url = self._base_url + "/admin/users"
        payload = {"login": login, "email": email}
        response = self._execute(self._method, url, payload)
        return response

    def create_org(self, org_name, admin_login):
        """
        Create an organization. It is only available to authenticated site administrators.
        Normal users will receive a 403 response if they try to access it.

        Attributes:
            org_name (str): Organization name.
            admin_login (str): Login name of the administrator.
        """
        url = self._base_url + "/admin/orginizations"
        payload = {"login": org_name, "admin": admin_login}
        response = self._execute(self._method, url, payload)
        return response

    def create_org_repo(self, org_name, repo_name):
        """
        Creates a new repository in the specified organization.
        The authenticated user must be a member of the organization.

        Attributes:
            org_name (str): Organization name.
            repo_name (str): Repository name.
        """
        url = self._base_url + f"/orgs/{org_name}/repos"
        payload = {"name": repo_name}
        response = self._execute(self._method, url, payload)
        return response
