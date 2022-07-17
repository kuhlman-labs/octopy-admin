"""
This module contains the RestPatch class.
"""

from .rest_request import RestRequest


class RestPatch(RestRequest):
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
