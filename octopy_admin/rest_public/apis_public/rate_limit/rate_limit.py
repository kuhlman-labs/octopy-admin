"""
Check your current rate limit status
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class RateLimit:
    """
    Check your current rate limit status
    """

    def __init__(self, client):
        """
        Initializes the RateLimit class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_rate_limit_status_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Get rate limit status for the authenticated user
        Docs:
        https://docs.github.com/rest/reference/rate-limit#get-rate-limit-status-for-the-authenticated-user
        """
        url = self._base_url + "/rate_limit"
        response = self._execute("get", url, params=params, payload=payload)
        return response
