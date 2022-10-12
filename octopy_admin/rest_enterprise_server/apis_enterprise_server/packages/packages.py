"""
Manage packages for authenticated users and organizations.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class Packages:
    """
    Manage packages for authenticated users and organizations.
    """

    def __init__(self, client):
        """
        Initializes the Packages class.
        """
        self._base_url = client._base_url
        self._execute = client._execute
