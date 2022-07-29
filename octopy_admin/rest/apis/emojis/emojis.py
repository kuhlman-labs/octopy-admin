"""
List emojis available to use on GitHub.
"""


class Emojis:
    """
    List emojis available to use on GitHub.
    """

    def __init__(self, client):
        self._base_url = client._base_url
        self._execute = client._execute

    def get_emojis(self, **payload):
        """
        Get emojis
        https://docs.github.com/rest/reference/emojis#get-emojis
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + f"/emojis"
        response = self._execute("get", url, payload)
        return response
