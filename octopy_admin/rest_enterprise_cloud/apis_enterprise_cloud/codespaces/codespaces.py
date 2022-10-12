"""
Endpoints to manage Codespaces using the REST API.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Codespaces:
    """
    Endpoints to manage Codespaces using the REST API.
    """

    def __init__(self, client):
        """
        Initializes the Codespaces class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_codespaces_for_the_organization(self, org, params=None, payload=None):
        """
        Summary:
        List codespaces for the organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-in-organization
        """
        url = self._base_url + f"/orgs/{org}/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def manage_access_control_for_organization_codespaces(self, org, params=None, payload=None):
        """
        Summary:
        Manage access control for organization codespaces
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#set-codespaces-billing
        """
        url = self._base_url + f"/orgs/{org}/codespaces/billing"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_organization_secrets(self, org, params=None, payload=None):
        """
        Summary:
        List organization secrets
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-organization-secrets
        """
        url = self._base_url + f"/orgs/{org}/codespaces/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_public_key(self, org, params=None, payload=None):
        """
        Summary:
        Get an organization public key
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-an-organization-public-key
        """
        url = self._base_url + f"/orgs/{org}/codespaces/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Get an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/codespaces/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Create or update an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#create-or-update-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/codespaces/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Delete an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#delete-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/codespaces/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Summary:
        List selected repositories for an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-selected-repositories-for-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/codespaces/secrets/{secret_name}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Summary:
        Set selected repositories for an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#set-selected-repositories-for-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/codespaces/secrets/{secret_name}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_selected_repository_to_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Add selected repository to an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#add-selected-repository-to-an-organization-secret
        """
        url = (
            self._base_url
            + f"/orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_selected_repository_from_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Remove selected repository from an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#remove-selected-repository-from-an-organization-secret
        """
        url = (
            self._base_url
            + f"/orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_codespaces_for_a_user_in_organization(self, org, username, params=None, payload=None):
        """
        Summary:
        List codespaces for a user in organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-codespaces-for-user-in-org
        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_codespace_from_the_organization(
        self, org, username, codespace_name, params=None, payload=None
    ):
        """
        Summary:
        Delete a codespace from the organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces
        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces/{codespace_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def stop_a_codespace_for_an_organization_user(
        self, org, username, codespace_name, params=None, payload=None
    ):
        """
        Summary:
        Stop a codespace for an organization user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces
        """
        url = self._base_url + f"/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_codespaces_in_a_repository_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        List codespaces in a repository for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-codespaces-in-a-repository-for-the-authenticated-user
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_codespace_in_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a codespace in a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#create-a-codespace-in-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_devcontainer_configurations_in_a_repository_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        List devcontainer configurations in a repository for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-devcontainers-in-a-repository-for-the-authenticated-user
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/devcontainers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_available_machine_types_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List available machine types for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-available-machine-types-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/machines"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_default_attributes_for_a_codespace(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get default attributes for a codespace
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#preview-attributes-for-a-new-codespace
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/new"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_secrets(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository secrets
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-repository-secrets
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_public_key(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a repository public key
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-a-repository-public-key
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Summary:
        Get a repository secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_repository_secret(
        self, owner, repo, secret_name, params=None, payload=None
    ):
        """
        Summary:
        Create or update a repository secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#create-or-update-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Summary:
        Delete a repository secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#delete-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codespaces/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_codespace_from_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        Create a codespace from a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#create-a-codespace-from-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/codespaces"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_codespaces_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List codespaces for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-codespaces-for-the-authenticated-user
        """
        url = self._base_url + "/user/codespaces"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_codespace_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Create a codespace for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#create-a-codespace-for-the-authenticated-user
        """
        url = self._base_url + "/user/codespaces"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_secrets_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List secrets for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-secrets-for-the-authenticated-user
        """
        url = self._base_url + "/user/codespaces/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_public_key_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Get public key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-public-key-for-the-authenticated-user
        """
        url = self._base_url + "/user/codespaces/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_secret_for_the_authenticated_user(self, secret_name, params=None, payload=None):
        """
        Summary:
        Get a secret for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-a-secret-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_secret_for_the_authenticated_user(
        self, secret_name, params=None, payload=None
    ):
        """
        Summary:
        Create or update a secret for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#create-or-update-a-secret-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_secret_for_the_authenticated_user(self, secret_name, params=None, payload=None):
        """
        Summary:
        Delete a secret for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#delete-a-secret-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_selected_repositories_for_a_user_secret(self, secret_name, params=None, payload=None):
        """
        Summary:
        List selected repositories for a user secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-selected-repositories-for-a-user-secret
        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_for_a_user_secret(self, secret_name, params=None, payload=None):
        """
        Summary:
        Set selected repositories for a user secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#set-selected-repositories-for-a-user-secret
        """
        url = self._base_url + f"/user/codespaces/secrets/{secret_name}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_a_selected_repository_to_a_user_secret(
        self, secret_name, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Add a selected repository to a user secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#add-a-selected-repository-to-a-user-secret
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
        Summary:
        Remove a selected repository from a user secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#remove-a-selected-repository-from-a-user-secret
        """
        url = (
            self._base_url + f"/user/codespaces/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_codespace_for_the_authenticated_user(self, codespace_name, params=None, payload=None):
        """
        Summary:
        Get a codespace for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#get-a-codespace-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Summary:
        Update a codespace for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#update-a-codespace-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Summary:
        Delete a codespace for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#delete-a-codespace-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def export_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Summary:
        Export a codespace for the authenticated user
        Docs:
        N/A
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/exports"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_details_about_a_codespace_export(
        self, codespace_name, export_id, params=None, payload=None
    ):
        """
        Summary:
        Get details about a codespace export
        Docs:
        N/A
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/exports/{export_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_machine_types_for_a_codespace(self, codespace_name, params=None, payload=None):
        """
        Summary:
        List machine types for a codespace
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#list-machine-types-for-a-codespace
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/machines"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Summary:
        Start a codespace for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#start-a-codespace-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/start"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def stop_a_codespace_for_the_authenticated_user(
        self, codespace_name, params=None, payload=None
    ):
        """
        Summary:
        Stop a codespace for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/codespaces#stop-a-codespace-for-the-authenticated-user
        """
        url = self._base_url + f"/user/codespaces/{codespace_name}/stop"
        response = self._execute("post", url, params=params, payload=payload)
        return response
