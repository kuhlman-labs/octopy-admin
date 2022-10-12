"""
View, modify your gists.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Gists:
    """
    View, modify your gists.
    """

    def __init__(self, client):
        """
        Initializes the Gists class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_gists_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List gists for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#list-gists-for-the-authenticated-user
        """
        url = self._base_url + "/gists"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_gist(self, params=None, payload=None):
        """
        Summary:
        Create a gist
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#create-a-gist
        """
        url = self._base_url + "/gists"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_public_gists(self, params=None, payload=None):
        """
        Summary:
        List public gists
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#list-public-gists
        """
        url = self._base_url + "/gists/public"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_starred_gists(self, params=None, payload=None):
        """
        Summary:
        List starred gists
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#list-starred-gists
        """
        url = self._base_url + "/gists/starred"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_gist(self, gist_id, params=None, payload=None):
        """
        Summary:
        Get a gist
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#get-a-gist
        """
        url = self._base_url + f"/gists/{gist_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_gist(self, gist_id, params=None, payload=None):
        """
        Summary:
        Update a gist
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists/#update-a-gist
        """
        url = self._base_url + f"/gists/{gist_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_gist(self, gist_id, params=None, payload=None):
        """
        Summary:
        Delete a gist
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#delete-a-gist
        """
        url = self._base_url + f"/gists/{gist_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_gist_comments(self, gist_id, params=None, payload=None):
        """
        Summary:
        List gist comments
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#list-gist-comments
        """
        url = self._base_url + f"/gists/{gist_id}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_gist_comment(self, gist_id, params=None, payload=None):
        """
        Summary:
        Create a gist comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#create-a-gist-comment
        """
        url = self._base_url + f"/gists/{gist_id}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_gist_comment(self, gist_id, comment_id, params=None, payload=None):
        """
        Summary:
        Get a gist comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#get-a-gist-comment
        """
        url = self._base_url + f"/gists/{gist_id}/comments/{comment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_gist_comment(self, gist_id, comment_id, params=None, payload=None):
        """
        Summary:
        Update a gist comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#update-a-gist-comment
        """
        url = self._base_url + f"/gists/{gist_id}/comments/{comment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_gist_comment(self, gist_id, comment_id, params=None, payload=None):
        """
        Summary:
        Delete a gist comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#delete-a-gist-comment
        """
        url = self._base_url + f"/gists/{gist_id}/comments/{comment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_gist_commits(self, gist_id, params=None, payload=None):
        """
        Summary:
        List gist commits
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#list-gist-commits
        """
        url = self._base_url + f"/gists/{gist_id}/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_gist_forks(self, gist_id, params=None, payload=None):
        """
        Summary:
        List gist forks
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#list-gist-forks
        """
        url = self._base_url + f"/gists/{gist_id}/forks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def fork_a_gist(self, gist_id, params=None, payload=None):
        """
        Summary:
        Fork a gist
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#fork-a-gist
        """
        url = self._base_url + f"/gists/{gist_id}/forks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def check_if_a_gist_is_starred(self, gist_id, params=None, payload=None):
        """
        Summary:
        Check if a gist is starred
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#check-if-a-gist-is-starred
        """
        url = self._base_url + f"/gists/{gist_id}/star"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def star_a_gist(self, gist_id, params=None, payload=None):
        """
        Summary:
        Star a gist
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#star-a-gist
        """
        url = self._base_url + f"/gists/{gist_id}/star"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unstar_a_gist(self, gist_id, params=None, payload=None):
        """
        Summary:
        Unstar a gist
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#unstar-a-gist
        """
        url = self._base_url + f"/gists/{gist_id}/star"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_gist_revision(self, gist_id, sha, params=None, payload=None):
        """
        Summary:
        Get a gist revision
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#get-a-gist-revision
        """
        url = self._base_url + f"/gists/{gist_id}/{sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_gists_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List gists for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/gists#list-gists-for-a-user
        """
        url = self._base_url + f"/users/{username}/gists"
        response = self._execute("get", url, params=params, payload=payload)
        return response
