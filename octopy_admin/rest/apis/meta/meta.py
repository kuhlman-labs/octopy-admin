"""
Endpoints that give information about the API.
"""


# pylint: disable=too-many-arguments
class Meta:
    """
    Endpoints that give information about the API.
    """

    def __init__(self, client):
        """
        Initialize the Meta class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def github_api_root(self, params=None, payload=None):
        """
        GitHub API Root
        https://docs.github.com/rest/overview/resources-in-the-rest-api#root-endpoint
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_meta_information(self, params=None, payload=None):
        """
        Get GitHub meta information
        https://docs.github.com/rest/reference/meta#get-github-meta-information
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/meta"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_octocat(self, params=None, payload=None):
        """
        Get Octocat
        https://docs.github.com/rest/reference/meta#get-octocat
        Attributes:
        Path Parameters:

        Payload Parameters:
        s
        """
        url = self._base_url + "/octocat"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_all_api_versions(self, params=None, payload=None):
        """
        Get all API versions
        https://docs.github.com/rest/reference/meta#get-all-api-versions
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/versions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_zen_of_github(self, params=None, payload=None):
        """
        Get the Zen of GitHub
        N/A
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/zen"
        response = self._execute("get", url, params=params, payload=payload)
        return response
