"""
Render GitHub flavored markdown
"""


# pylint: disable=too-many-arguments
class Markdown:
    """
    Render GitHub flavored markdown
    """

    def __init__(self, client):
        """
        Initialize the Markdown class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def render_a_markdown_document(self, params=None, payload=None):
        """
        Render a Markdown document
        https://docs.github.com/rest/reference/markdown#render-a-markdown-document
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/markdown"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def render_a_markdown_document_in_raw_mode(self, params=None, payload=None):
        """
        Render a Markdown document in raw mode
        https://docs.github.com/rest/reference/markdown#render-a-markdown-document-in-raw-mode
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/markdown/raw"
        response = self._execute("post", url, params=params, payload=payload)
        return response
