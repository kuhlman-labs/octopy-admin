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
