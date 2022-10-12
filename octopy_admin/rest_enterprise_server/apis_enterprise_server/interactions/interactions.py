"""
Owner or admin management of users interactions.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class Interactions:
    """
    Owner or admin management of users interactions.
    """

    def __init__(self, client):
        """
        Initializes the Interactions class.
        """
        self._base_url = client._base_url
        self._execute = client._execute
