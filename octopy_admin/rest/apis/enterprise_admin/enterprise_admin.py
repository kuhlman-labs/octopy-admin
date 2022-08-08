"""
Administer a GitHub enterprise.
"""


# pylint: disable=too-many-arguments
class EnterpriseAdmin:
    # pylint: disable=too-many-public-methods
    """
    Administer a GitHub enterprise.
    """

    def __init__(self, client):
        """
        Initialize the EnterpriseAdmin class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_actions_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Get GitHub Actions permissions for an enterprise
        https://docs.github.com/rest/reference/actions#get-github-actions-permissions-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_github_actions_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Set GitHub Actions permissions for an enterprise
        https://docs.github.com/rest/reference/actions#set-github-actions-permissions-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_selected_organizations_enabled_for_github_actions_in_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        List selected organizations enabled for GitHub Actions in an enterprise
        https://docs.github.com/rest/reference/actions#list-selected-organizations-enabled-for-github-actions-in-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/organizations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_organizations_enabled_for_github_actions_in_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Set selected organizations enabled for GitHub Actions in an enterprise
        https://docs.github.com/rest/reference/actions#set-selected-organizations-enabled-for-github-actions-in-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/organizations"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def enable_a_selected_organization_for_github_actions_in_an_enterprise(
        self, enterprise, org_id, params=None, payload=None
    ):
        """
        Enable a selected organization for GitHub Actions in an enterprise
        https://docs.github.com/rest/reference/actions#enable-a-selected-organization-for-github-actions-in-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        org_id
        Payload Parameters:

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
        Disable a selected organization for GitHub Actions in an enterprise
        https://docs.github.com/rest/reference/actions#disable-a-selected-organization-for-github-actions-in-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        org_id
        Payload Parameters:

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
        Get allowed actions and reusable workflows for an enterprise
        https://docs.github.com/rest/reference/actions#get-allowed-actions-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/selected-actions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_allowed_actions_and_reusable_workflows_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Set allowed actions and reusable workflows for an enterprise
        https://docs.github.com/rest/reference/actions#set-allowed-actions-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/selected-actions"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_self_hosted_runner_groups_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        List self-hosted runner groups for an enterprise
        https://docs.github.com/rest/reference/actions#list-self-hosted-runner-groups-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        per-page
         page
         visible-to-organization
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_self_hosted_runner_group_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Create a self-hosted runner group for an enterprise
        https://docs.github.com/rest/reference/actions#create-self-hosted-runner-group-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_group_for_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Get a self-hosted runner group for an enterprise
        https://docs.github.com/rest/reference/actions#get-a-self-hosted-runner-group-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_self_hosted_runner_group_for_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Update a self-hosted runner group for an enterprise
        https://docs.github.com/rest/reference/actions#update-a-self-hosted-runner-group-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_group_from_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        Delete a self-hosted runner group from an enterprise
        https://docs.github.com/rest/reference/actions#delete-a-self-hosted-runner-group-from-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_organization_access_to_a_self_hosted_runner_group_in_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        List organization access to a self-hosted runner group in an enterprise
        https://docs.github.com/rest/reference/actions#list-organization-access-to-a-self-hosted-runner-group-in-a-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        Payload Parameters:
        per-page
         page
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
        Set organization access for a self-hosted runner group in an enterprise
        https://docs.github.com/rest/reference/actions#set-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        Payload Parameters:

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
        Add organization access to a self-hosted runner group in an enterprise
        https://docs.github.com/rest/reference/actions#add-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        org_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_organization_access_to_a_self_hosted_runner_group_in_an_enterprise(
        self, enterprise, runner_group_id, org_id, params=None, payload=None
    ):
        """
        Remove organization access to a self-hosted runner group in an enterprise
        https://docs.github.com/rest/reference/actions#remove-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        org_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_in_a_group_for_an_enterprise(
        self, enterprise, runner_group_id, params=None, payload=None
    ):
        """
        List self-hosted runners in a group for an enterprise
        https://docs.github.com/rest/reference/actions#list-self-hosted-runners-in-a-group-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        Payload Parameters:
        per-page
         page
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
        Set self-hosted runners in a group for an enterprise
        https://docs.github.com/rest/reference/actions#set-self-hosted-runners-in-a-group-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        Payload Parameters:

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
        Add a self-hosted runner to a group for an enterprise
        https://docs.github.com/rest/reference/actions#add-a-self-hosted-runner-to-a-group-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        runner_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_self_hosted_runner_from_a_group_for_an_enterprise(
        self, enterprise, runner_group_id, runner_id, params=None, payload=None
    ):
        """
        Remove a self-hosted runner from a group for an enterprise
        https://docs.github.com/rest/reference/actions#remove-a-self-hosted-runner-from-a-group-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_group_id
        runner_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_self_hosted_runners_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        List self-hosted runners for an enterprise
        https://docs.github.com/rest/reference/actions#list-self-hosted-runners-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_runner_applications_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        List runner applications for an enterprise
        https://docs.github.com/rest/reference/actions#list-runner-applications-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/downloads"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_registration_token_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Create a registration token for an enterprise
        https://docs.github.com/rest/reference/actions#create-a-registration-token-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/registration-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_remove_token_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Create a remove token for an enterprise
        https://docs.github.com/rest/reference/actions#create-a-remove-token-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/remove-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Get a self-hosted runner for an enterprise
        https://docs.github.com/rest/reference/actions#get-a-self-hosted-runner-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_self_hosted_runner_from_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Delete a self-hosted runner from an enterprise
        https://docs.github.com/rest/reference/actions#delete-self-hosted-runner-from-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_labels_for_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        List labels for a self-hosted runner for an enterprise
        https://docs.github.com/rest/reference/actions#list-labels-for-a-self-hosted-runner-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_custom_labels_to_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Add custom labels to a self-hosted runner for an enterprise
        https://docs.github.com/rest/reference/actions#add-custom-labels-to-a-self-hosted-runner-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_custom_labels_for_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Set custom labels for a self-hosted runner for an enterprise
        https://docs.github.com/rest/reference/actions#set-custom-labels-for-a-self-hosted-runner-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_all_custom_labels_from_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, params=None, payload=None
    ):
        """
        Remove all custom labels from a self-hosted runner for an enterprise
        https://docs.github.com/rest/reference/actions#remove-all-custom-labels-from-a-self-hosted-runner-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_id
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def remove_a_custom_label_from_a_self_hosted_runner_for_an_enterprise(
        self, enterprise, runner_id, name, params=None, payload=None
    ):
        """
        Remove a custom label from a self-hosted runner for an enterprise
        https://docs.github.com/rest/reference/actions#remove-a-custom-label-from-a-self-hosted-runner-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        runner_id
        name
        Payload Parameters:
        runner-label-name
        """
        url = (
            self._base_url + f"/enterprises/{enterprise}/actions/runners/{runner_id}/labels/{name}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_the_audit_log_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Get the audit log for an enterprise
        https://docs.github.com/rest/reference/enterprise-admin#get-the-audit-log-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        audit-log-phrase
         audit-log-include
         audit-log-after
         audit-log-before
         audit-log-order
         page
         per-page
        """
        url = self._base_url + f"/enterprises/{enterprise}/audit-log"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def retrieve_enterprise_license_sync_consumed_licenses(
        self, enterprise, params=None, payload=None
    ):
        """
        Retrieve Enterprise License Sync Consumed Licenses
        https://docs.github.com/rest/reference/enterprise-admin#retrieve-enterprise-license-sync-consumed-licenses
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/enterprises/{enterprise}/consumed-licenses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def provides_license_sync_job_status_for_connected_instances(
        self, enterprise, params=None, payload=None
    ):
        """
        Provides License Sync Job status for connected instances
        https://docs.github.com/rest/reference/enterprise-admin#provides-license-sync-job-status-for-connected-instances
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/license-sync-status"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_provisioned_scim_groups_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        List provisioned SCIM groups for an enterprise
        https://docs.github.com/rest/reference/enterprise-admin#list-provisioned-scim-groups-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        start-index
         count
         filter
         excludedAttributes
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def provision_a_scim_enterprise_group_and_invite_users(
        self, enterprise, params=None, payload=None
    ):
        """
        Provision a SCIM enterprise group and invite users
        https://docs.github.com/rest/reference/enterprise-admin#provision-a-scim-enterprise-group-and-invite-users
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_scim_provisioning_information_for_an_enterprise_group(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Get SCIM provisioning information for an enterprise group
        https://docs.github.com/rest/reference/enterprise-admin#get-scim-provisioning-information-for-an-enterprise-group
        Attributes:
        Path Parameters:
        enterprise
        scim_group_id
        Payload Parameters:
        excludedAttributes
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_scim_information_for_a_provisioned_enterprise_group(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Set SCIM information for a provisioned enterprise group
        https://docs.github.com/rest/reference/enterprise-admin#set-scim-information-for-a-provisioned-enterprise-group
        Attributes:
        Path Parameters:
        enterprise
        scim_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_attribute_for_a_scim_enterprise_group(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Update an attribute for a SCIM enterprise group
        https://docs.github.com/rest/reference/enterprise-admin#update-an-attribute-for-a-scim-enterprise-group
        Attributes:
        Path Parameters:
        enterprise
        scim_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_scim_group_from_an_enterprise(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Delete a SCIM group from an enterprise
        https://docs.github.com/rest/reference/enterprise-admin#delete-a-scim-group-from-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        scim_group_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_scim_provisioned_identities_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        List SCIM provisioned identities for an enterprise
        https://docs.github.com/rest/reference/enterprise-admin#list-scim-provisioned-identities-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        start-index
         count
         filter
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def provision_and_invite_a_scim_enterprise_user(self, enterprise, params=None, payload=None):
        """
        Provision and invite a SCIM enterprise user
        https://docs.github.com/rest/reference/enterprise-admin#provision-and-invite-a-scim-enterprise-user
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_scim_provisioning_information_for_an_enterprise_user(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Get SCIM provisioning information for an enterprise user
        https://docs.github.com/rest/reference/enterprise-admin#get-scim-provisioning-information-for-an-enterprise-user
        Attributes:
        Path Parameters:
        enterprise
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_scim_information_for_a_provisioned_enterprise_user(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Set SCIM information for a provisioned enterprise user
        https://docs.github.com/rest/reference/enterprise-admin#set-scim-information-for-a-provisioned-enterprise-user
        Attributes:
        Path Parameters:
        enterprise
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_attribute_for_a_scim_enterprise_user(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Update an attribute for a SCIM enterprise user
        https://docs.github.com/rest/reference/enterprise-admin#update-an-attribute-for-a-scim-enterprise-user
        Attributes:
        Path Parameters:
        enterprise
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_scim_user_from_an_enterprise(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Delete a SCIM user from an enterprise
        https://docs.github.com/rest/reference/enterprise-admin#delete-a-scim-user-from-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response
