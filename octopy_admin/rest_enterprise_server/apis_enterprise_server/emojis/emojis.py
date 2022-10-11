"""
List emojis available to use on GitHub.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class Emojis:
    """
    List emojis available to use on GitHub.
    """

    def __init__(self, client):
        """
        Initializes the Emojis class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_emojis(self, params=None, payload=None):
        """
        Summary:
        Get emojis
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/emojis#get-emojis
        """
        url = self._base_url + "/emojis"
        response = self._execute("get", url, params=params, payload=payload)
        return response
