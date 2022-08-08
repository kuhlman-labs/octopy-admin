"""
Check your current rate limit status
"""


# pylint: disable=too-many-arguments
class RateLimit:
    # pylint: disable=too-few-public-methods
    """
    Check your current rate limit status
    """

    def __init__(self, client):
        """
        Initialize the RateLimit class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_rate_limit_status_for_the_authenticated_user(self, params=None, payload=None):
        """
        Get rate limit status for the authenticated user
        https://docs.github.com/rest/reference/rate-limit#get-rate-limit-status-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/rate_limit"
        response = self._execute("get", url, params=params, payload=payload)
        return response
