"""
Raw Git functionality.
"""


# pylint: disable=too-many-arguments
class Git:
    """
    Raw Git functionality.
    """

    def __init__(self, client):
        """
        Initialize the Git class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def create_a_blob(self, owner, repo, params=None, payload=None):
        """
        Create a blob
        https://docs.github.com/rest/reference/git#create-a-blob
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/blobs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_blob(self, owner, repo, file_sha, params=None, payload=None):
        """
        Get a blob
        https://docs.github.com/rest/reference/git#get-a-blob
        Attributes:
        Path Parameters:
        owner
        repo
        file_sha
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/blobs/{file_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_commit(self, owner, repo, params=None, payload=None):
        """
        Create a commit
        https://docs.github.com/rest/reference/git#create-a-commit
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/commits"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_commit(self, owner, repo, commit_sha, params=None, payload=None):
        """
        Get a commit
        https://docs.github.com/rest/reference/git#get-a-commit
        Attributes:
        Path Parameters:
        owner
        repo
        commit_sha
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/commits/{commit_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_matching_references(self, owner, repo, ref, params=None, payload=None):
        """
        List matching references
        https://docs.github.com/rest/reference/git#list-matching-references
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/matching-refs/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Get a reference
        https://docs.github.com/rest/reference/git#get-a-reference
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/ref/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_reference(self, owner, repo, params=None, payload=None):
        """
        Create a reference
        https://docs.github.com/rest/reference/git#create-a-reference
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/refs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_all_references_in_a_namespace(self, owner, repo, namespace, params=None, payload=None):
        """
        Get all references in a namespace
        https://docs.github.com/rest/reference/git#get-a-reference
        Attributes:
        Path Parameters:
        owner
        repo
        namespace
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/refs/{namespace}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Update a reference
        https://docs.github.com/rest/reference/git#update-a-reference
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/refs/{ref}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Delete a reference
        https://docs.github.com/rest/reference/git#delete-a-reference
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/refs/{ref}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_tag_object(self, owner, repo, params=None, payload=None):
        """
        Create a tag object
        https://docs.github.com/rest/reference/git#create-a-tag-object
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/tags"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_tag(self, owner, repo, tag_sha, params=None, payload=None):
        """
        Get a tag
        https://docs.github.com/rest/reference/git#get-a-tag
        Attributes:
        Path Parameters:
        owner
        repo
        tag_sha
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/tags/{tag_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_tree(self, owner, repo, params=None, payload=None):
        """
        Create a tree
        https://docs.github.com/rest/reference/git#create-a-tree
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/trees"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_tree(self, owner, repo, tree_sha, params=None, payload=None):
        """
        Get a tree
        https://docs.github.com/rest/reference/git#get-a-tree
        Attributes:
        Path Parameters:
        owner
        repo
        tree_sha
        Payload Parameters:
        recursive
        """
        url = self._base_url + f"/repos/{owner}/{repo}/git/trees/{tree_sha}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
