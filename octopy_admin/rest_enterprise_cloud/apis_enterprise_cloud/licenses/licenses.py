"""
View various OSS licenses.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, W0622


class Licenses:
    """
    View various OSS licenses.
    """

    def __init__(self, client):
        """
        Initializes the Licenses class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_all_commonly_used_licenses(self, params=None, payload=None):
        """
        Summary:
        Get all commonly used licenses
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/licenses#get-all-commonly-used-licenses
        """
        url = self._base_url + "/licenses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_license(self, license, params=None, payload=None):
        """
        Summary:
        Get a license
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/licenses#get-a-license
        """
        url = self._base_url + f"/licenses/{license}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_license_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get the license for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/licenses/#get-the-license-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/license"
        response = self._execute("get", url, params=params, payload=payload)
        return response
