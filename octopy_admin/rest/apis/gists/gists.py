"""
View, modify your gists.
"""


# pylint: disable=too-many-arguments
class Gists:
    """
    View, modify your gists.
    """

    def __init__(self, client):
        """
        Initialize the Gists class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_gists_for_the_authenticated_user(self, params=None, payload=None):
        """
        List gists for the authenticated user
        https://docs.github.com/rest/reference/gists#list-gists-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        since
         per-page
         page
        """
        url = self._base_url + "/gists"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_gist(self, params=None, payload=None):
        """
        Create a gist
        https://docs.github.com/rest/reference/gists#create-a-gist
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/gists"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_public_gists(self, params=None, payload=None):
        """
        List public gists
        https://docs.github.com/rest/reference/gists#list-public-gists
        Attributes:
        Path Parameters:

        Payload Parameters:
        since
         per-page
         page
        """
        url = self._base_url + "/gists/public"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_starred_gists(self, params=None, payload=None):
        """
        List starred gists
        https://docs.github.com/rest/reference/gists#list-starred-gists
        Attributes:
        Path Parameters:

        Payload Parameters:
        since
         per-page
         page
        """
        url = self._base_url + "/gists/starred"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_gist(self, gist_id, params=None, payload=None):
        """
        Get a gist
        https://docs.github.com/rest/reference/gists#get-a-gist
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_gist(self, gist_id, params=None, payload=None):
        """
        Update a gist
        https://docs.github.com/rest/reference/gists/#update-a-gist
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_gist(self, gist_id, params=None, payload=None):
        """
        Delete a gist
        https://docs.github.com/rest/reference/gists#delete-a-gist
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_gist_comments(self, gist_id, params=None, payload=None):
        """
        List gist comments
        https://docs.github.com/rest/reference/gists#list-gist-comments
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/gists/{gist_id}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_gist_comment(self, gist_id, params=None, payload=None):
        """
        Create a gist comment
        https://docs.github.com/rest/reference/gists#create-a-gist-comment
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_gist_comment(self, gist_id, comment_id, params=None, payload=None):
        """
        Get a gist comment
        https://docs.github.com/rest/reference/gists#get-a-gist-comment
        Attributes:
        Path Parameters:
        gist_id
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/comments/{comment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_gist_comment(self, gist_id, comment_id, params=None, payload=None):
        """
        Update a gist comment
        https://docs.github.com/rest/reference/gists#update-a-gist-comment
        Attributes:
        Path Parameters:
        gist_id
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/comments/{comment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_gist_comment(self, gist_id, comment_id, params=None, payload=None):
        """
        Delete a gist comment
        https://docs.github.com/rest/reference/gists#delete-a-gist-comment
        Attributes:
        Path Parameters:
        gist_id
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/comments/{comment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_gist_commits(self, gist_id, params=None, payload=None):
        """
        List gist commits
        https://docs.github.com/rest/reference/gists#list-gist-commits
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/gists/{gist_id}/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_gist_forks(self, gist_id, params=None, payload=None):
        """
        List gist forks
        https://docs.github.com/rest/reference/gists#list-gist-forks
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/gists/{gist_id}/forks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def fork_a_gist(self, gist_id, params=None, payload=None):
        """
        Fork a gist
        https://docs.github.com/rest/reference/gists#fork-a-gist
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/forks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def check_if_a_gist_is_starred(self, gist_id, params=None, payload=None):
        """
        Check if a gist is starred
        https://docs.github.com/rest/reference/gists#check-if-a-gist-is-starred
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/star"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def star_a_gist(self, gist_id, params=None, payload=None):
        """
        Star a gist
        https://docs.github.com/rest/reference/gists#star-a-gist
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/star"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unstar_a_gist(self, gist_id, params=None, payload=None):
        """
        Unstar a gist
        https://docs.github.com/rest/reference/gists#unstar-a-gist
        Attributes:
        Path Parameters:
        gist_id
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/star"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_gist_revision(self, gist_id, sha, params=None, payload=None):
        """
        Get a gist revision
        https://docs.github.com/rest/reference/gists#get-a-gist-revision
        Attributes:
        Path Parameters:
        gist_id
        sha
        Payload Parameters:

        """
        url = self._base_url + f"/gists/{gist_id}/{sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_gists_for_a_user(self, username, params=None, payload=None):
        """
        List gists for a user
        https://docs.github.com/rest/reference/gists#list-gists-for-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        since
         per-page
         page
        """
        url = self._base_url + f"/users/{username}/gists"
        response = self._execute("get", url, params=params, payload=payload)
        return response
