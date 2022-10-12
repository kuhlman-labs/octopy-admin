"""
Insight into codes of conduct for your communities.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class CodesOfConduct:
    """
    Insight into codes of conduct for your communities.
    """

    def __init__(self, client):
        """
        Initializes the CodesOfConduct class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_all_codes_of_conduct(self, params=None, payload=None):
        """
        Summary:
        Get all codes of conduct
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codes-of-conduct#get-all-codes-of-conduct
        """
        url = self._base_url + "/codes_of_conduct"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_code_of_conduct(self, key, params=None, payload=None):
        """
        Summary:
        Get a code of conduct
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codes-of-conduct#get-a-code-of-conduct
        """
        url = self._base_url + f"/codes_of_conduct/{key}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
