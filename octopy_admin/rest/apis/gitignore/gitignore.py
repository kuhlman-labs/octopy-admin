"""
View gitignore templates
"""


# pylint: disable=too-many-arguments
class Gitignore:
    """
    View gitignore templates
    """

    def __init__(self, client):
        """
        Initialize the Gitignore class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_all_gitignore_templates(self, params=None, payload=None):
        """
        Get all gitignore templates
        https://docs.github.com/rest/reference/gitignore#get-all-gitignore-templates
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/gitignore/templates"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_gitignore_template(self, name, params=None, payload=None):
        """
        Get a gitignore template
        https://docs.github.com/rest/reference/gitignore#get-a-gitignore-template
        Attributes:
        Path Parameters:
        name
        name
        Payload Parameters:

        """
        url = self._base_url + f"/gitignore/templates/{name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
