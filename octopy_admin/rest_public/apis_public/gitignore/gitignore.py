"""
View gitignore templates
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Gitignore:
    """
    View gitignore templates
    """

    def __init__(self, client):
        """
        Initializes the Gitignore class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_all_gitignore_templates(self, params=None, payload=None):
        """
        Summary:
        Get all gitignore templates
        Docs:
        https://docs.github.com/rest/reference/gitignore#get-all-gitignore-templates
        """
        url = self._base_url + "/gitignore/templates"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_gitignore_template(self, name, params=None, payload=None):
        """
        Summary:
        Get a gitignore template
        Docs:
        https://docs.github.com/rest/reference/gitignore#get-a-gitignore-template
        """
        url = self._base_url + f"/gitignore/templates/{name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
