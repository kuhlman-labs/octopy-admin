"""
Raw Git functionality.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Git:
    """
    Raw Git functionality.
    """

    def __init__(self, client):
        """
        Initializes the Git class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def create_a_blob(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a blob
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#create-a-blob
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/blobs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_blob(self, owner, repo, file_sha, params=None, payload=None):
        """
        Summary:
        Get a blob
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#get-a-blob
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/blobs/{file_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_commit(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a commit
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#create-a-commit
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/commits"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_commit(self, owner, repo, commit_sha, params=None, payload=None):
        """
        Summary:
        Get a commit
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#get-a-commit
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/commits/{commit_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_matching_references(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        List matching references
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#list-matching-references
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/matching-refs/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        Get a reference
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#get-a-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/ref/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_reference(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a reference
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#create-a-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/refs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        Update a reference
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#update-a-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/refs/{ref}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        Delete a reference
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#delete-a-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/refs/{ref}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_tag_object(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a tag object
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#create-a-tag-object
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/tags"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_tag(self, owner, repo, tag_sha, params=None, payload=None):
        """
        Summary:
        Get a tag
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#get-a-tag
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/tags/{tag_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_tree(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a tree
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#create-a-tree
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/trees"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_tree(self, owner, repo, tree_sha, params=None, payload=None):
        """
        Summary:
        Get a tree
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/git#get-a-tree
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/trees/{tree_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
