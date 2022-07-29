"""
GHES statistics
"""


class ServerStatistics:
    """
    GHES statistics
    """

    def __init__(self, client):
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_enterprise_server_statistics(self, enterprise_or_org, **payload):
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
        response = self._execute("get", url, payload)
        return response
