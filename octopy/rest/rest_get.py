"""
This module contains the RESTQuery class.
"""

from .rest_request import RestRequest


class RestGet(RestRequest):
    """
    This Class is used to create GET requests.
    """

    def __init__(self):
        """
        Initialize the REST client.

        Attributes:
            method (str): HTTP method.
        """
        super().__init__()
        self._method = "Get"

    def get_user(self, user):
        """
        Get a user.

        Attributes:
            user (str): User name.
        """
        url = self._base_url + f"/users/{user}"
        response = self._execute(self._method, url, None)
        return response

    def get_org(self, org):
        """
        Get an organization.

        Attributes:
            org (str): Organization name.
        """
        url = self._base_url + f"/orgs/{org}"
        response = self._execute(self._method, url, None)
        return response

    def get_repo(self, owner, repo):
        """
        Get a repository.

        Attributes:
            owner (str): Repository owner.
            repo (str): Repository name.
        """
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute(self._method, url, None)
        return response

    def get_repo_list(self, owner):
        """
        Get a list of repositories.

        Attributes:
            owner (str): Repository owner.
        """
        url = self._base_url + f"/orgs/{owner}/repos"
        response = self._execute(self._method, url, None)
        return response

    def get_collaborators(self, owner, repo):
        """
        Get a list of collaborators for a repository.

        Attributes:
            owner (str): Repository owner.
            repo (str): Repository name.
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators"
        response = self._execute(self._method, url, None)
        return response

    def get_collaborator_permission(self, owner, repo, user):
        """
        Get a collaborator's permission.

        Attributes:
            owner (str): Repository owner.
            repo (str): Repository name.
            user (str): Collaborator name.
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{user}/permission"
        response = self._execute(self._method, url, None)
        return response

    def get_repo_webhook_list(self, owner, repo):
        """
        Get a list of webhooks for a repository.

        Attributes:
            owner (str): Repository owner.
            repo (str): Repository name.
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks"
        response = self._execute(self._method, url, None)
        return response

    def get_org_webhook_list(self, org):
        """
        Get a list of webhooks for an organization.

        Attributes:
            org (str): Organization name.
        """
        url = self._base_url + f"/orgs/{org}/hooks"
        response = self._execute(self._method, url, None)
        return response

    def get_repo_webhook(self, owner, repo, hook_id):
        """
        Get a webhook for a repository.

        Attributes:

            owner (str): Repository owner.
            repo (str): Repository name.
            hook_id (str): Webhook ID.
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute(self._method, url, None)
        return response

    def get_org_webhook(self, org, hook_id):
        """
        Get a webhook for an organization.

        Attributes:
            org (str): Organization name.
            hook_id (str): Webhook ID.
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute(self._method, url, None)
        return response
