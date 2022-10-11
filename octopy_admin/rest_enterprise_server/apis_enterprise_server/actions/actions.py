"""
Endpoints to manage GitHub Actions using the REST API.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Actions:
    """
    Endpoints to manage GitHub Actions using the REST API.
    """

    def __init__(self, client):
        """
        Initializes the Actions class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_actions_cache_usage_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Actions cache usage for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-cache-usage-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/cache/usage"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_actions_cache_usage_policy_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Actions cache usage policy for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-cache-usage-policy-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/cache/usage-policy"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_cache_usage_policy_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Set GitHub Actions cache usage policy for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-github-actions-cache-usage-policy-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/cache/usage-policy"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_default_workflow_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Get default workflow permissions for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-default-workflow-permissions-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/workflow"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_default_workflow_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Set default workflow permissions for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-default-workflow-permissions-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/workflow"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_github_actions_cache_usage_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Get GitHub Actions cache usage for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-cache-usage-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/cache/usage"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_with_github_actions_cache_usage_for_an_organization(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        List repositories with GitHub Actions cache usage for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-repositories-with-github-actions-cache-usage-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/cache/usage-by-repository"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_actions_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Get GitHub Actions permissions for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-permissions-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Set GitHub Actions permissions for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-github-actions-permissions-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_selected_repositories_enabled_for_github_actions_in_an_organization(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        List selected repositories enabled for GitHub Actions in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-selected-repositories-enabled-for-github-actions-in-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_enabled_for_github_actions_in_an_organization(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        Set selected repositories enabled for GitHub Actions in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-selected-repositories-enabled-for-github-actions-in-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def enable_a_selected_repository_for_github_actions_in_an_organization(
        self, org, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Enable a selected repository for GitHub Actions in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#enable-a-selected-repository-for-github-actions-in-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories/{repository_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_a_selected_repository_for_github_actions_in_an_organization(
        self, org, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Disable a selected repository for GitHub Actions in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#disable-a-selected-repository-for-github-actions-in-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/repositories/{repository_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_allowed_actions_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Get allowed actions for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-allowed-actions-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/selected-actions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_allowed_actions_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Set allowed actions for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-allowed-actions-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/selected-actions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_default_workflow_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Get default workflow permissions for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-default-workflow-permissions
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/workflow"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_default_workflow_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Set default workflow permissions for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-default-workflow-permissions
        """
        url = self._base_url + f"/orgs/{org}/actions/permissions/workflow"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_self_hosted_runner_groups_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List self-hosted runner groups for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-self-hosted-runner-groups-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_self_hosted_runner_group_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Create a self-hosted runner group for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-self-hosted-runner-group-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_group_for_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Get a self-hosted runner group for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-self-hosted-runner-group-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_self_hosted_runner_group_for_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Update a self-hosted runner group for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#update-a-self-hosted-runner-group-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_group_from_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a self-hosted runner group from an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-a-self-hosted-runner-group-from-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_access_to_a_self_hosted_runner_group_in_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        List repository access to a self-hosted runner group in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-repository-access-to-a-self-hosted-runner-group-in-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_repository_access_for_a_self_hosted_runner_group_in_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Set repository access for a self-hosted runner group in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-repository-access-to-a-self-hosted-runner-group-in-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_repository_access_to_a_self_hosted_runner_group_in_an_organization(
        self, org, runner_group_id, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Add repository access to a self-hosted runner group in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-repository-acess-to-a-self-hosted-runner-group-in-an-organization
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
        Summary:
        Remove repository access to a self-hosted runner group in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-repository-access-to-a-self-hosted-runner-group-in-an-organization
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
        Summary:
        List self-hosted runners in a group for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-self-hosted-runners-in-a-group-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_self_hosted_runners_in_a_group_for_an_organization(
        self, org, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Set self-hosted runners in a group for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-self-hosted-runners-in-a-group-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/runners"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_a_self_hosted_runner_to_a_group_for_an_organization(
        self, org, runner_group_id, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Add a self-hosted runner to a group for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-a-self-hosted-runner-to-a-group-for-an-organization
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
        Summary:
        Remove a self-hosted runner from a group for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-a-self-hosted-runner-from-a-group-for-an-organization
        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List self-hosted runners for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-self-hosted-runners-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_runner_applications_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List runner applications for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-runner-applications-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/downloads"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_registration_token_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Create a registration token for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-registration-token-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/registration-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_remove_token_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Create a remove token for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-remove-token-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/remove-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Get a self-hosted runner for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-self-hosted-runner-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_from_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a self-hosted runner from an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-a-self-hosted-runner-from-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_labels_for_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Summary:
        List labels for a self-hosted runner for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-labels-for-a-self-hosted-runner-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_custom_labels_to_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Add custom labels to a self-hosted runner for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-custom-labels-to-a-self-hosted-runner-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_custom_labels_for_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Set custom labels for a self-hosted runner for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-custom-labels-for-a-self-hosted-runner-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_all_custom_labels_from_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Remove all custom labels from a self-hosted runner for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-all-custom-labels-from-a-self-hosted-runner-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def remove_a_custom_label_from_a_self_hosted_runner_for_an_organization(
        self, org, runner_id, name, params=None, payload=None
    ):
        """
        Summary:
        Remove a custom label from a self-hosted runner for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-a-custom-label-from-a-self-hosted-runner-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/actions/runners/{runner_id}/labels/{name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_organization_secrets(self, org, params=None, payload=None):
        """
        Summary:
        List organization secrets
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-organization-secrets
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_public_key(self, org, params=None, payload=None):
        """
        Summary:
        Get an organization public key
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-an-organization-public-key
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Get an organization secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Create or update an organization secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-or-update-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Delete an organization secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Summary:
        List selected repositories for an organization secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-selected-repositories-for-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Summary:
        Set selected repositories for an organization secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-selected-repositories-for-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/actions/secrets/{secret_name}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_selected_repository_to_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Add selected repository to an organization secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-selected-repository-to-an-organization-secret
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
        Summary:
        Remove selected repository from an organization secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-selected-repository-from-an-organization-secret
        """
        url = (
            self._base_url
            + f"/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_artifacts_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List artifacts for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-artifacts-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/artifacts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_artifact(self, owner, repo, artifact_id, params=None, payload=None):
        """
        Summary:
        Get an artifact
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-an-artifact
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_artifact(self, owner, repo, artifact_id, params=None, payload=None):
        """
        Summary:
        Delete an artifact
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-an-artifact
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def download_an_artifact(
        self, owner, repo, artifact_id, archive_format, params=None, payload=None
    ):
        """
        Summary:
        Download an artifact
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#download-an-artifact
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
        Summary:
        Get GitHub Actions cache usage for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-cache-usage-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/cache/usage"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_actions_cache_usage_policy_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Actions cache usage policy for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-cache-usage-policy-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/cache/usage-policy"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_cache_usage_policy_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Set GitHub Actions cache usage policy for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-github-actions-cache-usage-policy-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/cache/usage-policy"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_a_job_for_a_workflow_run(self, owner, repo, job_id, params=None, payload=None):
        """
        Summary:
        Get a job for a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-job-for-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/jobs/{job_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_job_logs_for_a_workflow_run(self, owner, repo, job_id, params=None, payload=None):
        """
        Summary:
        Download job logs for a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#download-job-logs-for-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/jobs/{job_id}/logs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def re_run_a_job_from_a_workflow_run(self, owner, repo, job_id, params=None, payload=None):
        """
        Summary:
        Re-run a job from a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#re-run-job-for-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_github_actions_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Actions permissions for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-permissions-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Set GitHub Actions permissions for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-github-actions-permissions-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_the_level_of_access_for_workflows_outside_of_the_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Get the level of access for workflows outside of the repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-workflow-access-level-to-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/access"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_the_level_of_access_for_workflows_outside_of_the_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Set the level of access for workflows outside of the repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-workflow-access-to-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/access"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_allowed_actions_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get allowed actions for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-allowed-actions-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/selected-actions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_allowed_actions_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Set allowed actions for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-allowed-actions-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/selected-actions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_default_workflow_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Get default workflow permissions for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-default-workflow-permissions-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/workflow"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_default_workflow_permissions_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Set default workflow permissions for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-default-workflow-permissions-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/permissions/workflow"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List self-hosted runners for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-self-hosted-runners-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_runner_applications_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List runner applications for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-runner-applications-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/downloads"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_registration_token_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a registration token for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-registration-token-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/registration-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_remove_token_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a remove token for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-remove-token-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/remove-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Get a self-hosted runner for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-self-hosted-runner-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_from_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a self-hosted runner from a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-a-self-hosted-runner-from-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_labels_for_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Summary:
        List labels for a self-hosted runner for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-labels-for-a-self-hosted-runner-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_custom_labels_to_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Add custom labels to a self-hosted runner for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-custom-labels-to-a-self-hosted-runner-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_custom_labels_for_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Set custom labels for a self-hosted runner for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-custom-labels-for-a-self-hosted-runner-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_all_custom_labels_from_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Remove all custom labels from a self-hosted runner for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-all-custom-labels-from-a-self-hosted-runner-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def remove_a_custom_label_from_a_self_hosted_runner_for_a_repository(
        self, owner, repo, runner_id, name, params=None, payload=None
    ):
        """
        Summary:
        Remove a custom label from a self-hosted runner for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-a-custom-label-from-a-self-hosted-runner-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runners/{runner_id}/labels/{name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_workflow_runs_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List workflow runs for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-workflow-runs-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        Get a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        Delete a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_the_review_history_for_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Summary:
        Get the review history for a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-the-review-history-for-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/approvals"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_workflow_run_artifacts(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        List workflow run artifacts
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-workflow-run-artifacts
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_workflow_run_attempt(
        self, owner, repo, run_id, attempt_number, params=None, payload=None
    ):
        """
        Summary:
        Get a workflow run attempt
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-workflow-run-attempt
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
        Summary:
        List jobs for a workflow run attempt
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-jobs-for-a-workflow-run-attempt
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
        Summary:
        Download workflow run attempt logs
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#download-workflow-run-attempt-logs
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def cancel_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        Cancel a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#cancel-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_jobs_for_a_workflow_run(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        List jobs for a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-jobs-for-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_workflow_run_logs(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        Download workflow run logs
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#download-workflow-run-logs
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_workflow_run_logs(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        Delete workflow run logs
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-workflow-run-logs
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_pending_deployments_for_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Summary:
        Get pending deployments for a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-pending-deployments-for-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def review_pending_deployments_for_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Summary:
        Review pending deployments for a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#review-pending-deployments-for-a-workflow-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def re_run_a_workflow(self, owner, repo, run_id, params=None, payload=None):
        """
        Summary:
        Re-run a workflow
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#re-run-a-workflow
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def re_run_failed_jobs_from_a_workflow_run(
        self, owner, repo, run_id, params=None, payload=None
    ):
        """
        Summary:
        Re-run failed jobs from a workflow run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#re-run-workflow-failed-jobs
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_secrets(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository secrets
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-repository-secrets
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_public_key(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a repository public key
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-repository-public-key
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Summary:
        Get a repository secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_repository_secret(
        self, owner, repo, secret_name, params=None, payload=None
    ):
        """
        Summary:
        Create or update a repository secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-or-update-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Summary:
        Delete a repository secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_workflows(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository workflows
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-repository-workflows
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_workflow(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Summary:
        Get a workflow
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-workflow
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def disable_a_workflow(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Summary:
        Disable a workflow
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#disable-a-workflow
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def create_a_workflow_dispatch_event(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Summary:
        Create a workflow dispatch event
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-workflow-dispatch-event
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def enable_a_workflow(self, owner, repo, workflow_id, params=None, payload=None):
        """
        Summary:
        Enable a workflow
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#enable-a-workflow
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_workflow_runs_for_a_workflow(
        self, owner, repo, workflow_id, params=None, payload=None
    ):
        """
        Summary:
        List workflow runs for a workflow
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-workflow-runs
        """
        url = self._base_url + f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_environment_secrets(self, repository_id, environment_name, params=None, payload=None):
        """
        Summary:
        List environment secrets
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-environment-secrets
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
        Summary:
        Get an environment public key
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-an-environment-public-key
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
        Summary:
        Get an environment secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-an-environment-secret
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
        Summary:
        Create or update an environment secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-or-update-an-environment-secret
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
        Summary:
        Delete an environment secret
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-an-environment-secret
        """
        url = (
            self._base_url
            + f"/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response
