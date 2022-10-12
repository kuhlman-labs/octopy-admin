"""
Administer a GitHub enterprise.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class EnterpriseAdmin:
    """
    Administer a GitHub enterprise.
    """

    def __init__(self, client):
        """
        Initializes the EnterpriseAdmin class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_actions_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Actions permissions for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#get-github-actions-permissions-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Set GitHub Actions permissions for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#set-github-actions-permissions-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_selected_organizations_enabled_for_github_actions_in_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        List selected organizations enabled for GitHub Actions in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#list-selected-organizations-enabled-for-github-actions-in-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/organizations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_organizations_enabled_for_github_actions_in_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Set selected organizations enabled for GitHub Actions in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#set-selected-organizations-enabled-for-github-actions-in-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/organizations"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def enable_a_selected_organization_for_github_actions_in_an_enterprise(
        self, enterprise, org_id, params=None, payload=None
    ):
        """
        Summary:
        Enable a selected organization for GitHub Actions in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#enable-a-selected-organization-for-github-actions-in-an-enterprise
        """
        url = (
            self._base_url + f"/enterprises/{enterprise}/actions/permissions/organizations/{org_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_a_selected_organization_for_github_actions_in_an_enterprise(
        self, enterprise, org_id, params=None, payload=None
    ):
        """
        Summary:
        Disable a selected organization for GitHub Actions in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#disable-a-selected-organization-for-github-actions-in-an-enterprise
        """
        url = (
            self._base_url + f"/enterprises/{enterprise}/actions/permissions/organizations/{org_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_allowed_actions_and_reusable_workflows_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Get allowed actions and reusable workflows for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#get-allowed-actions-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/selected-actions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_allowed_actions_and_reusable_workflows_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Set allowed actions and reusable workflows for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#set-allowed-actions-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/selected-actions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_self_hosted_runner_groups_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        List self-hosted runner groups for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#list-self-hosted-runner-groups-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_self_hosted_runner_group_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Create a self-hosted runner group for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#create-self-hosted-runner-group-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_group_for_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Get a self-hosted runner group for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#get-a-self-hosted-runner-group-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_self_hosted_runner_group_for_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Update a self-hosted runner group for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#update-a-self-hosted-runner-group-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_group_from_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a self-hosted runner group from an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#delete-a-self-hosted-runner-group-from-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_organization_access_to_a_self_hosted_runner_group_in_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        List organization access to a self-hosted runner group in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#list-organization-access-to-a-self-hosted-runner-group-in-a-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_organization_access_for_a_self_hosted_runner_group_in_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Set organization access for a self-hosted runner group in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#set-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_organization_access_to_a_self_hosted_runner_group_in_an_enterprise(
        self, enterprise, runner_group_id, org_id, params=None, payload=None
    ):
        """
        Summary:
        Add organization access to a self-hosted runner group in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#add-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_organization_access_to_a_self_hosted_runner_group_in_an_enterprise(
        self, enterprise, runner_group_id, org_id, params=None, payload=None
    ):
        """
        Summary:
        Remove organization access to a self-hosted runner group in an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#remove-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_in_a_group_for_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        List self-hosted runners in a group for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#list-self-hosted-runners-in-a-group-for-an-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_self_hosted_runners_in_a_group_for_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Summary:
        Set self-hosted runners in a group for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#set-self-hosted-runners-in-a-group-for-an-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_a_self_hosted_runner_to_a_group_for_an_enterprise(
        self, enterprise, runner_group_id, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Add a self-hosted runner to a group for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#add-a-self-hosted-runner-to-a-group-for-an-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_self_hosted_runner_from_a_group_for_an_enterprise(
        self, enterprise, runner_group_id, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Remove a self-hosted runner from a group for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#remove-a-self-hosted-runner-from-a-group-for-an-enterprise
        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        List self-hosted runners for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#list-self-hosted-runners-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_runner_applications_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        List runner applications for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#list-runner-applications-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/downloads"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_registration_token_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        Create a registration token for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#create-a-registration-token-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/registration-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_remove_token_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        Create a remove token for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#create-a-remove-token-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/remove-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Get a self-hosted runner for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#get-a-self-hosted-runner-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_from_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a self-hosted runner from an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#delete-self-hosted-runner-from-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_labels_for_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Summary:
        List labels for a self-hosted runner for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#list-labels-for-a-self-hosted-runner-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_custom_labels_to_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Add custom labels to a self-hosted runner for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#add-custom-labels-to-a-self-hosted-runner-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_custom_labels_for_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Set custom labels for a self-hosted runner for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#set-custom-labels-for-a-self-hosted-runner-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_all_custom_labels_from_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Summary:
        Remove all custom labels from a self-hosted runner for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#remove-all-custom-labels-from-a-self-hosted-runner-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def remove_a_custom_label_from_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, name, params=None, payload=None
    ):
        """
        Summary:
        Remove a custom label from a self-hosted runner for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/actions#remove-a-custom-label-from-a-self-hosted-runner-for-an-enterprise
        """
        url = (
            self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels/{name}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_the_audit_log_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        Get the audit log for an enterprise
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/enterprise-admin#get-the-audit-log-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/audit-log"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_enterprise_consumed_licenses(self, enterprise, params=None, payload=None):
        """
        Summary:
        List enterprise consumed licenses
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/enterprise-admin#list-enterprise-consumed-licenses
        """
        url = self._base_url + f"/enterprises/{enterprise}/consumed-licenses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_license_sync_status(self, enterprise, params=None, payload=None):
        """
        Summary:
        Get a license sync status
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/enterprise-admin#get-a-license-sync-status
        """
        url = self._base_url + f"/enterprises/{enterprise}/license-sync-status"
        response = self._execute("get", url, params=params, payload=payload)
        return response
