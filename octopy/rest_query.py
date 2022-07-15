"""
This module contains the RESTQuery class.
"""

import os

import requests


class RestRequestError(Exception):
    """
    Exception raised when a REST request fails.
    """


class RestRequest:  # pylint: disable=too-few-public-methods
    """
    The following methods are used to form requests to the GitHub REST API.
    """

    def __init__(self, rest_api_url=None, api_token=None):
        """
        Initialize the REST client to make requests to the GitHub API.

        Attributes:
            headers (dict): Headers to be used in the requests.
            base_url (str): Base URL of the GitHub API.
            API_TOKEN (str): GitHub API token.
            REST_API_URL (str): GitHub REST API URL.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise RestRequestError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        if rest_api_url is None:
            rest_api_url = os.environ.get("REST_API_URL", r"https://api.github.com")
        self._base_url = rest_api_url

    def _execute(self, method, url, payload):
        """
        Execute a request.

        Attributes:
            method (str): HTTP method.
            url (str): URL.
            payload (dict): Payload.
        """
        try:
            response = requests.request(method=method, url=url, json=payload, headers=self._headers)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as errtimeout:
            raise RestRequestError from errtimeout
        except requests.exceptions.HTTPError as errhttp:
            raise RestRequestError from errhttp
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestRequestError from errredirect
        except requests.exceptions.RequestException as errexcept:
            raise RestRequestError from errexcept


class RestPostProducer(RestRequest):
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


class RestPatchProducer(RestRequest):
    """
    Initialize the REST client.
    """

    def __init__(self):
        super().__init__()
        self._method = "Patch"

    def update_repo_webhook_config(self, owner, repo, hook_id, config):
        """
        Update a repository webhook URL.

        Attributes:
            owner (str): Repository owner.
            repo (str): Repository name.
            hook_id (str): Webhook ID.
            new_url (str): New webhook URL.
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/config"
        payload = config
        response = self._execute(self._method, url, payload)
        return response

    def update_org_webhook_config(self, owner, hook_id, config):
        """
        Update an organization webhook URL.

        Attributes:
            owner (str): Organization name.
            hook_id (str): Webhook ID.
            new_url (str): New webhook URL.
        """
        url = self._base_url + f"/orgs/{owner}/hooks/{hook_id}/config"
        payload = config
        response = self._execute(self._method, url, payload)
        return response


class RestGetProvider(RestRequest):
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
