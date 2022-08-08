"""
GHES statistics
"""


# pylint: disable=too-many-arguments
class ServerStatistics:
    # pylint: disable=too-few-public-methods
    """
    GHES statistics
    """

    def __init__(self, client):
        """
        Initialize the ServerStatistics class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_enterprise_server_statistics(self, enterprise_or_org, params=None, payload=None):
        """
        Get GitHub Enterprise Server statistics
        https://docs.github.com/rest/reference/enterprise-admin#get-github-enterprise-server-statistics
        Attributes:
        Path Parameters:
        enterprise_or_org
        Payload Parameters:
        date_start
         date_end
        """
        url = self._base_url + f"/enterprise-installation/{enterprise_or_org}/server-statistics"
        response = self._execute("get", url, params=params, payload=payload)
        return response
