"""
Insight into codes of conduct for your communities.
"""


class CodesOfConduct:
    """
    Insight into codes of conduct for your communities.
    """

    def __init__(self, client):
        """
        Initialize the CodesOfConduct class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_all_codes_of_conduct(self, payload=None):
        """
        Get all codes of conduct
        https://docs.github.com/rest/reference/codes-of-conduct#get-all-codes-of-conduct
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/codes_of_conduct"
        response = self._execute("get", url, payload)
        return response

    def get_a_code_of_conduct(self, key, payload=None):
        """
        Get a code of conduct
        https://docs.github.com/rest/reference/codes-of-conduct#get-a-code-of-conduct
        Attributes:
        Path Parameters:
        key
        Payload Parameters:

        """
        url = self._base_url + f"/codes_of_conduct/{key}"
        response = self._execute("get", url, payload)
        return response
