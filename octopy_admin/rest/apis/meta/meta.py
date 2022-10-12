"""
Endpoints that give information about the API.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Meta:
    """
    Endpoints that give information about the API.
    """

    def __init__(self, client):
        """
        Initializes the Meta class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def github_api_root(self, params=None, payload=None):
        """
        Summary:
        GitHub API Root
        Docs:
        https://docs.github.com/rest/overview/resources-in-the-rest-api#root-endpoint
        """
        url = self._base_url + "/"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_meta_information(self, params=None, payload=None):
        """
        Summary:
        Get GitHub meta information
        Docs:
        https://docs.github.com/rest/reference/meta#get-github-meta-information
        """
        url = self._base_url + "/meta"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_octocat(self, params=None, payload=None):
        """
        Summary:
        Get Octocat
        Docs:
        https://docs.github.com/rest/reference/meta#get-octocat
        """
        url = self._base_url + "/octocat"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_zen_of_github(self, params=None, payload=None):
        """
        Summary:
        Get the Zen of GitHub
        Docs:
        N/A
        """
        url = self._base_url + "/zen"
        response = self._execute("get", url, params=params, payload=payload)
        return response
