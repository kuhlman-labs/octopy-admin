"""
Endpoints to manage Codespaces using the REST API.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class Codespaces:
    """
    Endpoints to manage Codespaces using the REST API.
    """

    def __init__(self, client):
        """
        Initializes the Codespaces class.
        """
        self._base_url = client._base_url
        self._execute = client._execute
