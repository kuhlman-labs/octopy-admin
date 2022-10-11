"""
GHES statistics
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class ServerStatistics:
    """
    GHES statistics
    """

    def __init__(self, client):
        """
        Initializes the ServerStatistics class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_enterprise_server_statistics(self, enterprise_or_org, params=None, payload=None):
        """
        Summary:
        Get GitHub Enterprise Server statistics
        Docs:
        https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/admin-stats#get-github-enterprise-server-statistics
        """
        url = self._base_url + f"/enterprise-installation/{enterprise_or_org}/server-statistics"
        response = self._execute("get", url, params=params, payload=payload)
        return response
