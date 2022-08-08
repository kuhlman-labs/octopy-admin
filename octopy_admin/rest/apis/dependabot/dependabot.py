"""
Endpoints to manage Dependabot.
"""


# pylint: disable=too-many-arguments
class Dependabot:
    """
    Endpoints to manage Dependabot.
    """

    def __init__(self, client):
        """
        Initialize the Dependabot class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_secrets(self, org, params=None, payload=None):
        """
        List organization secrets
        https://docs.github.com/rest/reference/dependabot#list-organization-secrets
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_public_key(self, org, params=None, payload=None):
        """
        Get an organization public key
        https://docs.github.com/rest/reference/dependabot#get-an-organization-public-key
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Get an organization secret
        https://docs.github.com/rest/reference/dependabot#get-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Create or update an organization secret
        https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Delete an organization secret
        https://docs.github.com/rest/reference/dependabot#delete-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        List selected repositories for an organization secret
        https://docs.github.com/rest/reference/dependabot#list-selected-repositories-for-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:
        page
         per-page
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Set selected repositories for an organization secret
        https://docs.github.com/rest/reference/dependabot#set-selected-repositories-for-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_selected_repository_to_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Add selected repository to an organization secret
        https://docs.github.com/rest/reference/dependabot#add-selected-repository-to-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_selected_repository_from_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Remove selected repository from an organization secret
        https://docs.github.com/rest/reference/dependabot#remove-selected-repository-from-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_secrets(self, owner, repo, params=None, payload=None):
        """
        List repository secrets
        https://docs.github.com/rest/reference/dependabot#list-repository-secrets
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_public_key(self, owner, repo, params=None, payload=None):
        """
        Get a repository public key
        https://docs.github.com/rest/reference/dependabot#get-a-repository-public-key
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Get a repository secret
        https://docs.github.com/rest/reference/dependabot#get-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_repository_secret(
        self, owner, repo, secret_name, params=None, payload=None
    ):
        """
        Create or update a repository secret
        https://docs.github.com/rest/reference/dependabot#create-or-update-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Delete a repository secret
        https://docs.github.com/rest/reference/dependabot#delete-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response
