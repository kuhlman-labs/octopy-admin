"""
Endpoints to manage Codespaces using the REST API.
"""


# pylint: disable=too-many-arguments
class Codespaces:
    # pylint: disable=too-many-public-methods
    """
    Endpoints to manage Codespaces using the REST API.
    """

    def __init__(self, client):
        """
        Initialize the Codespaces class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_secrets(self, org, params=None, payload=None):
        """
        List organization secrets
        https://docs.github.com/rest/reference/codespaces#list-organization-secrets
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/organizations/{org}/codespaces/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_codespaces_for_the_organization(self, org, params=None, payload=None):
        """
        List codespaces for the organization
        https://docs.github.com/rest/reference/codespaces#list-in-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_codespaces_for_a_user_in_organization(self, org, username, params=None, payload=None):
        """
        List codespaces for a user in organization
        https://docs.github.com/rest/reference/codespaces#get-codespaces-for-user-in-org
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_codespace_from_the_organization(
        self, org, username, codespace_name, params=None, payload=None
    ):
        """
        Delete a codespace from the organization
        https://docs.github.com/rest/reference/codespaces
        Attributes:
        Path Parameters:
        org
        username
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces/{codespace_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def export_a_codespace_for_an_organization_user(
        self, org, username, codespace_name, params=None, payload=None
    ):
        """
        Export a codespace for an organization user
        https://docs.github.com/rest/reference/codespaces
        Attributes:
        Path Parameters:
        org
        username
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces/{codespace_name}/exports"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def start_a_codespace_for_an_organization_user(
        self, org, username, codespace_name, params=None, payload=None
    ):
        """
        Start a codespace for an organization user
        https://docs.github.com/rest/reference/codespaces
        Attributes:
        Path Parameters:
        org
        username
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces/{codespace_name}/start"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def stop_a_codespace_for_an_organization_user(
        self, org, username, codespace_name, params=None, payload=None
    ):
        """
        Stop a codespace for an organization user
        https://docs.github.com/rest/reference/codespaces
        Attributes:
        Path Parameters:
        org
        username
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_codespaces_in_a_repository_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        List codespaces in a repository for the authenticated user
        https://docs.github.com/rest/reference/codespaces#list-codespaces-in-a-repository-for-the-authenticated-user
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_codespace_in_a_repository(self, owner, repo, params=None, payload=None):
        """
        Create a codespace in a repository
        https://docs.github.com/rest/reference/codespaces#create-a-codespace-in-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_devcontainer_configurations_in_a_repository_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        List devcontainer configurations in a repository for the authenticated user
        https://docs.github.com/rest/reference/codespaces#list-devcontainers-in-a-repository-for-the-authenticated-user
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/devcontainers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_available_machine_types_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List available machine types for a repository
        https://docs.github.com/rest/reference/codespaces#list-available-machine-types-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        location
         client_ip
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/machines"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_default_attributes_for_a_codespace(self, owner, repo, params=None, payload=None):
        """
        Get default attributes for a codespace
        https://docs.github.com/rest/reference/codespaces#preview-attributes-for-a-new-codespace
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        ref
         client_ip
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/new"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_secrets(self, owner, repo, params=None, payload=None):
        """
        List repository secrets
        https://docs.github.com/rest/reference/codespaces#list-repository-secrets
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_public_key(self, owner, repo, params=None, payload=None):
        """
        Get a repository public key
        https://docs.github.com/rest/reference/codespaces#get-a-repository-public-key
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Get a repository secret
        https://docs.github.com/rest/reference/codespaces#get-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_repository_secret(
        self, owner, repo, secret_name, params=None, payload=None
    ):
        """
        Create or update a repository secret
        https://docs.github.com/rest/reference/codespaces#create-or-update-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Delete a repository secret
        https://docs.github.com/rest/reference/codespaces#delete-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_codespace_from_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Create a codespace from a pull request
        https://docs.github.com/rest/reference/codespaces#create-a-codespace-from-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/codespaces"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_codespaces_for_the_authenticated_user(self, params=None, payload=None):
        """
        List codespaces for the authenticated user
        https://docs.github.com/rest/reference/codespaces#list-codespaces-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
         repository-id-in-query
        """
        url = self._base_url + "/user/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_codespace_for_the_authenticated_user(self, params=None, payload=None):
        """
        Create a codespace for the authenticated user
        https://docs.github.com/rest/reference/codespaces#create-a-codespace-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/codespaces"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_secrets_for_the_authenticated_user(self, params=None, payload=None):
        """
        List secrets for the authenticated user
        https://docs.github.com/rest/reference/codespaces#list-secrets-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/codespaces/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_public_key_for_the_authenticated_user(self, params=None, payload=None):
        """
        Get public key for the authenticated user
        https://docs.github.com/rest/reference/codespaces#get-public-key-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/codespaces/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_secret_for_the_authenticated_user(self, secret_name, params=None, payload=None):
        """
        Get a secret for the authenticated user
        https://docs.github.com/rest/reference/codespaces#get-a-secret-for-the-authenticated-user
        Attributes:
        Path Parameters:
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_secret_for_the_authenticated_user(
        self, secret_name, params=None, payload=None
    ):
        """
        Create or update a secret for the authenticated user
        https://docs.github.com/rest/reference/codespaces#create-or-update-a-secret-for-the-authenticated-user
        Attributes:
        Path Parameters:
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_secret_for_the_authenticated_user(self, secret_name, params=None, payload=None):
        """
        Delete a secret for the authenticated user
        https://docs.github.com/rest/reference/codespaces#delete-a-secret-for-the-authenticated-user
        Attributes:
        Path Parameters:
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_selected_repositories_for_a_user_secret(self, secret_name, params=None, payload=None):
        """
        List selected repositories for a user secret
        https://docs.github.com/rest/reference/codespaces#list-selected-repositories-for-a-user-secret
        Attributes:
        Path Parameters:
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_for_a_user_secret(self, secret_name, params=None, payload=None):
        """
        Set selected repositories for a user secret
        https://docs.github.com/rest/reference/codespaces#set-selected-repositories-for-a-user-secret
        Attributes:
        Path Parameters:
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_a_selected_repository_to_a_user_secret(
        self, secret_name, repository_id, params=None, payload=None
    ):
        """
        Add a selected repository to a user secret
        https://docs.github.com/rest/reference/codespaces#add-a-selected-repository-to-a-user-secret
        Attributes:
        Path Parameters:
        secret_name
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url + f"/user/codespaces/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_selected_repository_from_a_user_secret(
        self, secret_name, repository_id, params=None, payload=None
    ):
        """
        Remove a selected repository from a user secret
        https://docs.github.com/rest/reference/codespaces#remove-a-selected-repository-from-a-user-secret
        Attributes:
        Path Parameters:
        secret_name
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url + f"/user/codespaces/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_codespace_for_the_authenticated_user(self, codespace_name, params=None, payload=None):
        """
        Get a codespace for the authenticated user
        https://docs.github.com/rest/reference/codespaces#get-a-codespace-for-the-authenticated-user
        Attributes:
        Path Parameters:
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Update a codespace for the authenticated user
        https://docs.github.com/rest/reference/codespaces#update-a-codespace-for-the-authenticated-user
        Attributes:
        Path Parameters:
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Delete a codespace for the authenticated user
        https://docs.github.com/rest/reference/codespaces#delete-a-codespace-for-the-authenticated-user
        Attributes:
        Path Parameters:
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def export_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Export a codespace for the authenticated user
        N/A
        Attributes:
        Path Parameters:
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/exports"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_details_about_a_codespace_export(
        self, codespace_name, export_id, params=None, payload=None
    ):
        """
        Get details about a codespace export
        N/A
        Attributes:
        Path Parameters:
        codespace_name
        export_id
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/exports/{export_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_machine_types_for_a_codespace(self, codespace_name, params=None, payload=None):
        """
        List machine types for a codespace
        https://docs.github.com/rest/reference/codespaces#list-machine-types-for-a-codespace
        Attributes:
        Path Parameters:
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/machines"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Start a codespace for the authenticated user
        https://docs.github.com/rest/reference/codespaces#start-a-codespace-for-the-authenticated-user
        Attributes:
        Path Parameters:
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/start"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def stop_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Stop a codespace for the authenticated user
        https://docs.github.com/rest/reference/codespaces#stop-a-codespace-for-the-authenticated-user
        Attributes:
        Path Parameters:
        codespace_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/stop"
        response = self._execute("post", url, params=params, payload=payload)
        return response
