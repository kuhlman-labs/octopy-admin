"""
View gitignore templates
"""


class Gitignore:
    """
    View gitignore templates
    """

    def __init__(self, client):
        self._base_url = client._base_url
        self._execute = client._execute

    def get_all_gitignore_templates(self, **payload):
        """
        Get all gitignore templates
        https://docs.github.com/rest/reference/gitignore#get-all-gitignore-templates
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + f"/gitignore/templates"
        response = self._execute("get", url, payload)
        return response

    def get_a_gitignore_template(self, name, **payload):
        """
        Get a gitignore template
        https://docs.github.com/rest/reference/gitignore#get-a-gitignore-template
        Attributes:
        Path Parameters:
        name
        Payload Parameters:

        """
        url = self._base_url + f"/gitignore/templates/{name}"
        response = self._execute("get", url, payload)
        return response
