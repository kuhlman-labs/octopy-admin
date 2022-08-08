"""
View various OSS licenses.
"""


# pylint: disable=too-many-arguments
class Licenses:
    """
    View various OSS licenses.
    """

    def __init__(self, client):
        """
        Initialize the Licenses class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_all_commonly_used_licenses(self, params=None, payload=None):
        """
        Get all commonly used licenses
        https://docs.github.com/rest/reference/licenses#get-all-commonly-used-licenses
        Attributes:
        Path Parameters:

        Payload Parameters:
        featured
         per-page
         page
        """
        url = self._base_url + "/licenses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_license(self, license, params=None, payload=None):
        # pylint: disable=redefined-builtin
        """
        Get a license
        https://docs.github.com/rest/reference/licenses#get-a-license
        Attributes:
        Path Parameters:
        license
        Payload Parameters:

        """
        url = self._base_url + f"/licenses/{license}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_license_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Get the license for a repository
        https://docs.github.com/rest/reference/licenses/#get-the-license-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/license"
        response = self._execute("get", url, params=params, payload=payload)
        return response
