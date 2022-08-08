"""
Endpoints to manage GitHub Actions using the REST API.
"""
# pylint: disable=too-many-lines


# pylint: disable=too-many-arguments
class Actions:
    # pylint: disable=too-many-public-methods
    """
    Endpoints to manage GitHub Actions using the REST API.
    """

    def __init__(self, client):
        """
        Initialize the Actions class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_actions_cache_usage_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Get GitHub Actions cache usage for an enterprise
        https://docs.github.com/rest/reference/actions#get-github-actions-cache-usage-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/cache/usage"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_the_github_actions_oidc_custom_issuer_policy_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Set the GitHub Actions OIDC custom issuer policy for an enterprise
        https://docs.github.com/rest/reference/actions/oidc#set-actions-oidc-custom-issuer-policy-for-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/oidc/customization/issuer"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_default_workflow_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Get default workflow permissions for an enterprise
        https://docs.github.com/rest/reference/actions#get-default-workflow-permissions-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/workflow"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_default_workflow_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Set default workflow permissions for an enterprise
        https://docs.github.com/rest/reference/actions#set-default-workflow-permissions-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/workflow"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_github_actions_cache_usage_for_an_organization(self, org, params=None, payload=None):
        """
        Get GitHub Actions cache usage for an organization
        https://docs.github.com/rest/reference/actions#get-github-actions-cache-usage-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/cache/usage"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_with_github_actions_cache_usage_for_an_organization(
        self, org, params=None, payload=None
    ):
        """
        List repositories with GitHub Actions cache usage for an organization
        https://docs.github.com/rest/reference/actions#list-repositories-with-github-actions-cache-usage-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/actions/cache/usage-by-repository"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_actions_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Get GitHub Actions permissions for an organization
        https://docs.github.com/rest/reference/actions#get-github-actions-permissions-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Set GitHub Actions permissions for an organization
        https://docs.github.com/rest/reference/actions#set-github-actions-permissions-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_selected_repositories_enabled_for_github_actions_in_an_organization(
        self, org, params=None, payload=None
    ):
        """
        List selected repositories enabled for GitHub Actions in an organization
        https://docs.github.com/rest/reference/actions#list-selected-repositories-enabled-for-github-actions-in-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_enabled_for_github_actions_in_an_organization(
        self, org, params=None, payload=None
    ):
        """
        Set selected repositories enabled for GitHub Actions in an organization
        https://docs.github.com/rest/reference/actions#set-selected-repositories-enabled-for-github-actions-in-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def enable_a_selected_repository_for_github_actions_in_an_organization(
        self, org, repository_id, params=None, payload=None
    ):
        """
        Enable a selected repository for GitHub Actions in an organization
        https://docs.github.com/rest/reference/actions#enable-a-selected-repository-for-github-actions-in-an-organization
        Attributes:
        Path Parameters:
        org
        repository_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories/{repository_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_a_selected_repository_for_github_actions_in_an_organization(
        self, org, repository_id, params=None, payload=None
    ):
        """
        Disable a selected repository for GitHub Actions in an organization
        https://docs.github.com/rest/reference/actions#disable-a-selected-repository-for-github-actions-in-an-organization
        Attributes:
        Path Parameters:
        org
        repository_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories/{repository_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_allowed_actions_and_reusable_workflows_for_an_organization(
        self, org, params=None, payload=None
    ):
        """
        Get allowed actions and reusable workflows for an organization
        https://docs.github.com/rest/reference/actions#get-allowed-actions-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/selected-actions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_allowed_actions_and_reusable_workflows_for_an_organization(
        self, org, params=None, payload=None
    ):
        """
        Set allowed actions and reusable workflows for an organization
        https://docs.github.com/rest/reference/actions#set-allowed-actions-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/selected-actions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_default_workflow_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Get default workflow permissions for an organization
        https://docs.github.com/rest/reference/actions#get-default-workflow-permissions
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/workflow"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_default_workflow_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Set default workflow permissions for an organization
        https://docs.github.com/rest/reference/actions#set-default-workflow-permissions
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/workflow"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_self_hosted_runner_groups_for_an_organization(self, org, params=None, payload=None):
        """
        List self-hosted runner groups for an organization
        https://docs.github.com/rest/reference/actions#list-self-hosted-runner-groups-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
         visible-to-repository
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_self_hosted_runner_group_for_an_organization(self, org, params=None, payload=None):
        """
        Create a self-hosted runner group for an organization
        https://docs.github.com/rest/reference/actions#create-a-self-hosted-runner-group-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_group_for_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Get a self-hosted runner group for an organization
        https://docs.github.com/rest/reference/actions#get-a-self-hosted-runner-group-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_self_hosted_runner_group_for_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Update a self-hosted runner group for an organization
        https://docs.github.com/rest/reference/actions#update-a-self-hosted-runner-group-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_group_from_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Delete a self-hosted runner group from an organization
        https://docs.github.com/rest/reference/actions#delete-a-self-hosted-runner-group-from-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_access_to_a_self_hosted_runner_group_in_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        List repository access to a self-hosted runner group in an organization
        https://docs.github.com/rest/reference/actions#list-repository-access-to-a-self-hosted-runner-group-in-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        Payload Parameters:
        page
         per-page
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_repository_access_for_a_self_hosted_runner_group_in_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Set repository access for a self-hosted runner group in an organization
        https://docs.github.com/rest/reference/actions#set-repository-access-to-a-self-hosted-runner-group-in-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_repository_access_to_a_self_hosted_runner_group_in_an_organization(
        self, org, runner_group_id, repository_id, params=None, payload=None
    ):
        """
        Add repository access to a self-hosted runner group in an organization
        https://docs.github.com/rest/reference/actions#add-repository-acess-to-a-self-hosted-runner-group-in-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_repository_access_to_a_self_hosted_runner_group_in_an_organization(
        self, org, runner_group_id, repository_id, params=None, payload=None
    ):
        """
        Remove repository access to a self-hosted runner group in an organization
        https://docs.github.com/rest/reference/actions#remove-repository-access-to-a-self-hosted-runner-group-in-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_in_a_group_for_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        List self-hosted runners in a group for an organization
        https://docs.github.com/rest/reference/actions#list-self-hosted-runners-in-a-group-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_self_hosted_runners_in_a_group_for_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Set self-hosted runners in a group for an organization
        https://docs.github.com/rest/reference/actions#set-self-hosted-runners-in-a-group-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/runners"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_a_self_hosted_runner_to_a_group_for_an_organization(
        self, org, runner_group_id, runner_id, params=None, payload=None
    ):
        """
        Add a self-hosted runner to a group for an organization
        https://docs.github.com/rest/reference/actions#add-a-self-hosted-runner-to-a-group-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        runner_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_self_hosted_runner_from_a_group_for_an_organization(
        self, org, runner_group_id, runner_id, params=None, payload=None
    ):
        """
        Remove a self-hosted runner from a group for an organization
        https://docs.github.com/rest/reference/actions#remove-a-self-hosted-runner-from-a-group-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_group_id
        runner_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_for_an_organization(self, org, params=None, payload=None):
        """
        List self-hosted runners for an organization
        https://docs.github.com/rest/reference/actions#list-self-hosted-runners-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/actions/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_runner_applications_for_an_organization(self, org, params=None, payload=None):
        """
        List runner applications for an organization
        https://docs.github.com/rest/reference/actions#list-runner-applications-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/downloads"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_registration_token_for_an_organization(self, org, params=None, payload=None):
        """
        Create a registration token for an organization
        https://docs.github.com/rest/reference/actions#create-a-registration-token-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/registration-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_remove_token_for_an_organization(self, org, params=None, payload=None):
        """
        Create a remove token for an organization
        https://docs.github.com/rest/reference/actions#create-a-remove-token-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/remove-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Get a self-hosted runner for an organization
        https://docs.github.com/rest/reference/actions#get-a-self-hosted-runner-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_from_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Delete a self-hosted runner from an organization
        https://docs.github.com/rest/reference/actions#delete-a-self-hosted-runner-from-an-organization
        Attributes:
        Path Parameters:
        org
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_labels_for_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        List labels for a self-hosted runner for an organization
        https://docs.github.com/rest/reference/actions#list-labels-for-a-self-hosted-runner-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_custom_labels_to_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Add custom labels to a self-hosted runner for an organization
        https://docs.github.com/rest/reference/actions#add-custom-labels-to-a-self-hosted-runner-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_custom_labels_for_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Set custom labels for a self-hosted runner for an organization
        https://docs.github.com/rest/reference/actions#set-custom-labels-for-a-self-hosted-runner-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_all_custom_labels_from_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Remove all custom labels from a self-hosted runner for an organization
        https://docs.github.com/rest/reference/actions#remove-all-custom-labels-from-a-self-hosted-runner-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def remove_a_custom_label_from_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, name, params=None, payload=None
    ):
        """
        Remove a custom label from a self-hosted runner for an organization
        https://docs.github.com/rest/reference/actions#remove-a-custom-label-from-a-self-hosted-runner-for-an-organization
        Attributes:
        Path Parameters:
        org
        runner_id
        name
        Payload Parameters:
        runner-label-name
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels/{name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_organization_secrets(self, org, params=None, payload=None):
        """
        List organization secrets
        https://docs.github.com/rest/reference/actions#list-organization-secrets
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_public_key(self, org, params=None, payload=None):
        """
        Get an organization public key
        https://docs.github.com/rest/reference/actions#get-an-organization-public-key
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Get an organization secret
        https://docs.github.com/rest/reference/actions#get-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Create or update an organization secret
        https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Delete an organization secret
        https://docs.github.com/rest/reference/actions#delete-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        List selected repositories for an organization secret
        https://docs.github.com/rest/reference/actions#list-selected-repositories-for-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:
        page
         per-page
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Set selected repositories for an organization secret
        https://docs.github.com/rest/reference/actions#set-selected-repositories-for-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_selected_repository_to_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Add selected repository to an organization secret
        https://docs.github.com/rest/reference/actions#add-selected-repository-to-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_selected_repository_from_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Remove selected repository from an organization secret
        https://docs.github.com/rest/reference/actions#remove-selected-repository-from-an-organization-secret
        Attributes:
        Path Parameters:
        org
        secret_name
        repository_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_artifacts_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List artifacts for a repository
        https://docs.github.com/rest/reference/actions#list-artifacts-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/artifacts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_artifact(self, owner, repo, artifact_id, params=None, payload=None):
        """
        Get an artifact
        https://docs.github.com/rest/reference/actions#get-an-artifact
        Attributes:
        Path Parameters:
        owner
        repo
        artifact_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_artifact(self, owner, repo, artifact_id, params=None, payload=None):
        """
        Delete an artifact
        https://docs.github.com/rest/reference/actions#delete-an-artifact
        Attributes:
        Path Parameters:
        owner
        repo
        artifact_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def download_an_artifact(
        self, owner, repo, artifact_id, archive_format, params=None, payload=None
    ):
        """
        Download an artifact
        https://docs.github.com/rest/reference/actions#download-an-artifact
        Attributes:
        Path Parameters:
        owner
        repo
        artifact_id
        archive_format
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_actions_cache_usage_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Get GitHub Actions cache usage for a repository
        https://docs.github.com/rest/reference/actions#get-github-actions-cache-usage-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/cache/usage"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_github_actions_caches_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List GitHub Actions caches for a repository
        https://docs.github.com/rest/actions/cache#list-github-actions-caches-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
         git-ref
         actions-cache-key
         actions-cache-list-sort
         direction
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/caches"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_github_actions_caches_for_a_repository__using_a_cache_key(
        self, owner, repo, params=None, payload=None
    ):
        """
        Delete GitHub Actions caches for a repository (using a cache key)
        https://docs.github.com/rest/actions/cache#delete-github-actions-caches-for-a-repository-using-a-cache-key
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        actions-cache-key-required
         git-ref
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/caches"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def delete_a_github_actions_cache_for_a_repository__using_a_cache_id(
        self, owner, repo, cache_id, params=None, payload=None
    ):
        """
        Delete a GitHub Actions cache for a repository (using a cache ID)
        https://docs.github.com/rest/actions/cache#delete-a-github-actions-cache-for-a-repository-using-a-cache-id
        Attributes:
        Path Parameters:
        owner
        repo
        cache_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/caches/{cache_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_job_for_a_workflow_run(self, owner, repo, job_id, params=None, payload=None):
        """
        Get a job for a workflow run
        https://docs.github.com/rest/reference/actions#get-a-job-for-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        job_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/jobs/{job_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_job_logs_for_a_workflow_run(self, owner, repo, job_id, params=None, payload=None):
        """
        Download job logs for a workflow run
        https://docs.github.com/rest/reference/actions#download-job-logs-for-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        job_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/jobs/{job_id}/logs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def re_run_a_job_from_a_workflow_run(self, owner, repo, job_id, params=None, payload=None):
        """
        Re-run a job from a workflow run
        https://docs.github.com/rest/reference/actions#re-run-job-for-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        job_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_the_opt_out_flag_of_an_oidc_subject_claim_customization_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Get the opt-out flag of an OIDC subject claim customization for a repository
        https://docs.github.com/rest/actions/oidc#get-the-opt-out-flag-of-an-oidc-subject-claim-customization-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/oidc/customization/sub"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_the_opt_out_flag_of_an_oidc_subject_claim_customization_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Set the opt-out flag of an OIDC subject claim customization for a repository
        https://docs.github.com/rest/actions/oidc#set-the-opt-out-flag-of-an-oidc-subject-claim-customization-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/oidc/customization/sub"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_github_actions_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Get GitHub Actions permissions for a repository
        https://docs.github.com/rest/reference/actions#get-github-actions-permissions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Set GitHub Actions permissions for a repository
        https://docs.github.com/rest/reference/actions#set-github-actions-permissions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_the_level_of_access_for_workflows_outside_of_the_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Get the level of access for workflows outside of the repository
        https://docs.github.com/rest/reference/actions#get-workflow-access-level-to-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/access"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_the_level_of_access_for_workflows_outside_of_the_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Set the level of access for workflows outside of the repository
        https://docs.github.com/rest/reference/actions#set-workflow-access-to-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/access"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_allowed_actions_and_reusable_workflows_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Get allowed actions and reusable workflows for a repository
        https://docs.github.com/rest/reference/actions#get-allowed-actions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/selected-actions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_allowed_actions_and_reusable_workflows_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Set allowed actions and reusable workflows for a repository
        https://docs.github.com/rest/reference/actions#set-allowed-actions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/selected-actions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_default_workflow_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Get default workflow permissions for a repository
        https://docs.github.com/rest/reference/actions#get-default-workflow-permissions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/workflow"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_default_workflow_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Set default workflow permissions for a repository
        https://docs.github.com/rest/reference/actions#set-default-workflow-permissions-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/workflow"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List self-hosted runners for a repository
        https://docs.github.com/rest/reference/actions#list-self-hosted-runners-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_runner_applications_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List runner applications for a repository
        https://docs.github.com/rest/reference/actions#list-runner-applications-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/downloads"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_registration_token_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Create a registration token for a repository
        https://docs.github.com/rest/reference/actions#create-a-registration-token-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/registration-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_remove_token_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Create a remove token for a repository
        https://docs.github.com/rest/reference/actions#create-a-remove-token-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/remove-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Get a self-hosted runner for a repository
        https://docs.github.com/rest/reference/actions#get-a-self-hosted-runner-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_from_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Delete a self-hosted runner from a repository
        https://docs.github.com/rest/reference/actions#delete-a-self-hosted-runner-from-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_labels_for_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        List labels for a self-hosted runner for a repository
        https://docs.github.com/rest/reference/actions#list-labels-for-a-self-hosted-runner-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_custom_labels_to_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Add custom labels to a self-hosted runner for a repository
        https://docs.github.com/rest/reference/actions#add-custom-labels-to-a-self-hosted-runner-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_custom_labels_for_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Set custom labels for a self-hosted runner for a repository
        https://docs.github.com/rest/reference/actions#set-custom-labels-for-a-self-hosted-runner-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_all_custom_labels_from_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Remove all custom labels from a self-hosted runner for a repository
        https://docs.github.com/rest/reference/actions#remove-all-custom-labels-from-a-self-hosted-runner-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def remove_a_custom_label_from_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, name, params=None, payload=None
    ):
        """
        Remove a custom label from a self-hosted runner for a repository
        https://docs.github.com/rest/reference/actions#remove-a-custom-label-from-a-self-hosted-runner-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        runner_id
        name
        Payload Parameters:
        runner-label-name
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels/{name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_workflow_runs_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List workflow runs for a repository
        https://docs.github.com/rest/reference/actions#list-workflow-runs-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        actor
         workflow-run-branch
         event
         workflow-run-status
         per-page
         page
         created
         exclude-pull-requests
         workflow-run-check-suite-id
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        Get a workflow run
        https://docs.github.com/rest/reference/actions#get-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:
        exclude-pull-requests
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        Delete a workflow run
        https://docs.github.com/rest/reference/actions#delete-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_the_review_history_for_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Get the review history for a workflow run
        https://docs.github.com/rest/reference/actions#get-the-review-history-for-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/approvals"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def approve_a_workflow_run_for_a_fork_pull_request(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Approve a workflow run for a fork pull request
        https://docs.github.com/rest/reference/actions#approve-a-workflow-run-for-a-fork-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/approve"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_workflow_run_artifacts(self, owner, repo, run_id, params=None, payload=None):
        """
        List workflow run artifacts
        https://docs.github.com/rest/reference/actions#list-workflow-run-artifacts
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_workflow_run_attempt(
        self, owner, repo, run_id, attempt_number, params=None, payload=None
    ):
        """
        Get a workflow run attempt
        https://docs.github.com/rest/reference/actions#get-a-workflow-run-attempt
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        attempt_number
        Payload Parameters:
        exclude-pull-requests
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_jobs_for_a_workflow_run_attempt(
        self, owner, repo, run_id, attempt_number, params=None, payload=None
    ):
        """
        List jobs for a workflow run attempt
        https://docs.github.com/rest/reference/actions#list-jobs-for-a-workflow-run-attempt
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        attempt_number
        Payload Parameters:
        per-page
         page
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_workflow_run_attempt_logs(
        self, owner, repo, run_id, attempt_number, params=None, payload=None
    ):
        """
        Download workflow run attempt logs
        https://docs.github.com/rest/reference/actions#download-workflow-run-attempt-logs
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        attempt_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def cancel_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        Cancel a workflow run
        https://docs.github.com/rest/reference/actions#cancel-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_jobs_for_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        List jobs for a workflow run
        https://docs.github.com/rest/reference/actions#list-jobs-for-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:
        filter
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_workflow_run_logs(self, owner, repo, run_id, params=None, payload=None):
        """
        Download workflow run logs
        https://docs.github.com/rest/reference/actions#download-workflow-run-logs
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_workflow_run_logs(self, owner, repo, run_id, params=None, payload=None):
        """
        Delete workflow run logs
        https://docs.github.com/rest/reference/actions#delete-workflow-run-logs
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_pending_deployments_for_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Get pending deployments for a workflow run
        https://docs.github.com/rest/reference/actions#get-pending-deployments-for-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def review_pending_deployments_for_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Review pending deployments for a workflow run
        https://docs.github.com/rest/reference/actions#review-pending-deployments-for-a-workflow-run
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def re_run_a_workflow(self, owner, repo, run_id, params=None, payload=None):
        """
        Re-run a workflow
        https://docs.github.com/rest/reference/actions#re-run-a-workflow
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def re_run_failed_jobs_from_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Re-run failed jobs from a workflow run
        https://docs.github.com/rest/reference/actions#re-run-workflow-failed-jobs
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def retry_a_workflow(self, owner, repo, run_id, params=None, payload=None):
        """
        Retry a workflow
        https://docs.github.com/rest/reference/actions#retry-a-workflow
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/retry"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_workflow_run_usage(self, owner, repo, run_id, params=None, payload=None):
        """
        Get workflow run usage
        https://docs.github.com/rest/reference/actions#get-workflow-run-usage
        Attributes:
        Path Parameters:
        owner
        repo
        run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/timing"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_secrets(self, owner, repo, params=None, payload=None):
        """
        List repository secrets
        https://docs.github.com/rest/reference/actions#list-repository-secrets
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_public_key(self, owner, repo, params=None, payload=None):
        """
        Get a repository public key
        https://docs.github.com/rest/reference/actions#get-a-repository-public-key
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Get a repository secret
        https://docs.github.com/rest/reference/actions#get-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_repository_secret(
        self, owner, repo, secret_name, params=None, payload=None
    ):
        """
        Create or update a repository secret
        https://docs.github.com/rest/reference/actions#create-or-update-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Delete a repository secret
        https://docs.github.com/rest/reference/actions#delete-a-repository-secret
        Attributes:
        Path Parameters:
        owner
        repo
        secret_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_workflows(self, owner, repo, params=None, payload=None):
        """
        List repository workflows
        https://docs.github.com/rest/reference/actions#list-repository-workflows
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_workflow(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Get a workflow
        https://docs.github.com/rest/reference/actions#get-a-workflow
        Attributes:
        Path Parameters:
        owner
        repo
        workflow_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def disable_a_workflow(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Disable a workflow
        https://docs.github.com/rest/reference/actions#disable-a-workflow
        Attributes:
        Path Parameters:
        owner
        repo
        workflow_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def create_a_workflow_dispatch_event(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Create a workflow dispatch event
        https://docs.github.com/rest/reference/actions#create-a-workflow-dispatch-event
        Attributes:
        Path Parameters:
        owner
        repo
        workflow_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def enable_a_workflow(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Enable a workflow
        https://docs.github.com/rest/reference/actions#enable-a-workflow
        Attributes:
        Path Parameters:
        owner
        repo
        workflow_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_workflow_runs(self, owner, repo, workflow_id, params=None, payload=None):
        """
        List workflow runs
        https://docs.github.com/rest/reference/actions#list-workflow-runs
        Attributes:
        Path Parameters:
        owner
        repo
        workflow_id
        Payload Parameters:
        actor
         workflow-run-branch
         event
         workflow-run-status
         per-page
         page
         created
         exclude-pull-requests
         workflow-run-check-suite-id
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_workflow_usage(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Get workflow usage
        https://docs.github.com/rest/reference/actions#get-workflow-usage
        Attributes:
        Path Parameters:
        owner
        repo
        workflow_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def run_an_actions_workflow_dynamically(self, repository_id, params=None, payload=None):
        """
        Run an actions workflow dynamically
        https://docs.github.com/rest/reference/actions#run-an-actions-workflow-dynamically
        Attributes:
        Path Parameters:
        repository_id
        Payload Parameters:

        """
        url = self._base_url + f"/repositories/{repository_id}/actions/dynamic"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_environment_secrets(self, repository_id, environment_name, params=None, payload=None):
        """
        List environment secrets
        https://docs.github.com/rest/reference/actions#list-environment-secrets
        Attributes:
        Path Parameters:
        repository_id
        environment_name
        Payload Parameters:
        per-page
         page
        """
        url = (
            self._base_url
            + f"/repositories/{repository_id}/environments/{environment_name}/secrets"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_environment_public_key(
        self, repository_id, environment_name, params=None, payload=None
    ):
        """
        Get an environment public key
        https://docs.github.com/rest/reference/actions#get-an-environment-public-key
        Attributes:
        Path Parameters:
        repository_id
        environment_name
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repositories/{repository_id}/environments/{environment_name}/secrets/public-key"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_environment_secret(
        self, repository_id, environment_name, secret_name, params=None, payload=None
    ):
        """
        Get an environment secret
        https://docs.github.com/rest/reference/actions#get-an-environment-secret
        Attributes:
        Path Parameters:
        repository_id
        environment_name
        secret_name
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_environment_secret(
        self, repository_id, environment_name, secret_name, params=None, payload=None
    ):
        """
        Create or update an environment secret
        https://docs.github.com/rest/reference/actions#create-or-update-an-environment-secret
        Attributes:
        Path Parameters:
        repository_id
        environment_name
        secret_name
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_environment_secret(
        self, repository_id, environment_name, secret_name, params=None, payload=None
    ):
        """
        Delete an environment secret
        https://docs.github.com/rest/reference/actions#delete-an-environment-secret
        Attributes:
        Path Parameters:
        repository_id
        environment_name
        secret_name
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response
