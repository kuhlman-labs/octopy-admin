"""
List emojis available to use on GitHub.
"""


# pylint: disable=too-many-arguments
class Emojis:
    # pylint: disable=too-few-public-methods
    """
    List emojis available to use on GitHub.
    """

    def __init__(self, client):
        """
        Initialize the Emojis class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_emojis(self, params=None, payload=None):
        """
        Get emojis
        https://docs.github.com/rest/reference/emojis#get-emojis
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/emojis"
        response = self._execute("get", url, params=params, payload=payload)
        return response
