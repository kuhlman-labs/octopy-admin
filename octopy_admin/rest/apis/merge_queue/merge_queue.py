"""
Interact with GitHub Merge Queues.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class MergeQueue:
    """
    Interact with GitHub Merge Queues.
    """

    def __init__(self, client):
        """
        Initializes the MergeQueue class.
        """
        self._base_url = client._base_url
        self._execute = client._execute
