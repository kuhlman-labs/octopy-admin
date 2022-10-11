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

    def list_global_webhooks(self, params=None, payload=None):
        """
        Summary:
        List global webhooks
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-global-webhooks
        """
        url = self._base_url + "/admin/hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_global_webhook(self, params=None, payload=None):
        """
        Summary:
        Create a global webhook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#create-a-global-webhook
        """
        url = self._base_url + "/admin/hooks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_global_webhook(self, hook_id, params=None, payload=None):
        """
        Summary:
        Get a global webhook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-a-global-webhook
        """
        url = self._base_url + f"/admin/hooks/{hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_global_webhook(self, hook_id, params=None, payload=None):
        """
        Summary:
        Update a global webhook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-a-global-webhook
        """
        url = self._base_url + f"/admin/hooks/{hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_global_webhook(self, hook_id, params=None, payload=None):
        """
        Summary:
        Delete a global webhook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-global-webhook
        """
        url = self._base_url + f"/admin/hooks/{hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def ping_a_global_webhook(self, hook_id, params=None, payload=None):
        """
        Summary:
        Ping a global webhook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#ping-a-global-webhook
        """
        url = self._base_url + f"/admin/hooks/{hook_id}/pings"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_public_keys(self, params=None, payload=None):
        """
        Summary:
        List public keys
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-public-keys
        """
        url = self._base_url + "/admin/keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_public_key(self, key_ids, params=None, payload=None):
        """
        Summary:
        Delete a public key
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-public-key
        """
        url = self._base_url + f"/admin/keys/{key_ids}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def update_ldap_mapping_for_a_team(self, team_id, params=None, payload=None):
        """
        Summary:
        Update LDAP mapping for a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-ldap-mapping-for-a-team
        """
        url = self._base_url + f"/admin/ldap/teams/{team_id}/mapping"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def sync_ldap_mapping_for_a_team(self, team_id, params=None, payload=None):
        """
        Summary:
        Sync LDAP mapping for a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#sync-ldap-mapping-for-a-team
        """
        url = self._base_url + f"/admin/ldap/teams/{team_id}/sync"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_ldap_mapping_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Update LDAP mapping for a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-ldap-mapping-for-a-user
        """
        url = self._base_url + f"/admin/ldap/users/{username}/mapping"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def sync_ldap_mapping_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Sync LDAP mapping for a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#sync-ldap-mapping-for-a-user
        """
        url = self._base_url + f"/admin/ldap/users/{username}/sync"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_an_organization(self, params=None, payload=None):
        """
        Summary:
        Create an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#create-an-organization
        """
        url = self._base_url + "/admin/organizations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_an_organization_name(self, org, params=None, payload=None):
        """
        Summary:
        Update an organization name
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-an-organization-name
        """
        url = self._base_url + f"/admin/organizations/{org}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_pre_receive_environments(self, params=None, payload=None):
        """
        Summary:
        List pre-receive environments
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-pre-receive-environments
        """
        url = self._base_url + "/admin/pre-receive-environments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_pre_receive_environment(self, params=None, payload=None):
        """
        Summary:
        Create a pre-receive environment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#create-a-pre-receive-environment
        """
        url = self._base_url + "/admin/pre-receive-environments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_pre_receive_environment(self, pre_receive_environment_id, params=None, payload=None):
        """
        Summary:
        Get a pre-receive environment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-a-pre-receive-environment
        """
        url = self._base_url + f"/admin/pre-receive-environments/{pre_receive_environment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_pre_receive_environment(
        self, pre_receive_environment_id, params=None, payload=None
    ):
        """
        Summary:
        Update a pre-receive environment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-a-pre-receive-environment
        """
        url = self._base_url + f"/admin/pre-receive-environments/{pre_receive_environment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_pre_receive_environment(
        self, pre_receive_environment_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a pre-receive environment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-pre-receive-environment
        """
        url = self._base_url + f"/admin/pre-receive-environments/{pre_receive_environment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def start_a_pre_receive_environment_download(
        self, pre_receive_environment_id, params=None, payload=None
    ):
        """
        Summary:
        Start a pre-receive environment download
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#start-a-pre-receive-environment-download
        """
        url = (
            self._base_url
            + f"/admin/pre-receive-environments/{pre_receive_environment_id}/downloads"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_the_download_status_for_a_pre_receive_environment(
        self, pre_receive_environment_id, params=None, payload=None
    ):
        """
        Summary:
        Get the download status for a pre-receive environment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-the-download-status-for-a-pre-receive-environment
        """
        url = (
            self._base_url
            + f"/admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_pre_receive_hooks(self, params=None, payload=None):
        """
        Summary:
        List pre-receive hooks
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-pre-receive-hooks
        """
        url = self._base_url + "/admin/pre-receive-hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_pre_receive_hook(self, params=None, payload=None):
        """
        Summary:
        Create a pre-receive hook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#create-a-pre-receive-hook
        """
        url = self._base_url + "/admin/pre-receive-hooks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_pre_receive_hook(self, pre_receive_hook_id, params=None, payload=None):
        """
        Summary:
        Get a pre-receive hook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-a-pre-receive-hook
        """
        url = self._base_url + f"/admin/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_pre_receive_hook(self, pre_receive_hook_id, params=None, payload=None):
        """
        Summary:
        Update a pre-receive hook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-a-pre-receive-hook
        """
        url = self._base_url + f"/admin/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_pre_receive_hook(self, pre_receive_hook_id, params=None, payload=None):
        """
        Summary:
        Delete a pre-receive hook
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-pre-receive-hook
        """
        url = self._base_url + f"/admin/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_personal_access_tokens(self, params=None, payload=None):
        """
        Summary:
        List personal access tokens
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-personal-access-tokens
        """
        url = self._base_url + "/admin/tokens"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_personal_access_token(self, token_id, params=None, payload=None):
        """
        Summary:
        Delete a personal access token
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-personal-access-token
        """
        url = self._base_url + f"/admin/tokens/{token_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_user(self, params=None, payload=None):
        """
        Summary:
        Create a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#create-a-user
        """
        url = self._base_url + "/admin/users"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_the_username_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Update the username for a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-the-username-for-a-user
        """
        url = self._base_url + f"/admin/users/{username}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Delete a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-user
        """
        url = self._base_url + f"/admin/users/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_an_impersonation_oauth_token(self, username, params=None, payload=None):
        """
        Summary:
        Create an impersonation OAuth token
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#create-an-impersonation-oauth-token
        """
        url = self._base_url + f"/admin/users/{username}/authorizations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_an_impersonation_oauth_token(self, username, params=None, payload=None):
        """
        Summary:
        Delete an impersonation OAuth token
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-an-impersonation-oauth-token
        """
        url = self._base_url + f"/admin/users/{username}/authorizations"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_the_global_announcement_banner(self, params=None, payload=None):
        """
        Summary:
        Get the global announcement banner
        Docs:
        N/A
        """
        url = self._base_url + "/enterprise/announcement"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_the_global_announcement_banner(self, params=None, payload=None):
        """
        Summary:
        Set the global announcement banner
        Docs:
        N/A
        """
        url = self._base_url + "/enterprise/announcement"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def remove_the_global_announcement_banner(self, params=None, payload=None):
        """
        Summary:
        Remove the global announcement banner
        Docs:
        N/A
        """
        url = self._base_url + "/enterprise/announcement"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_license_information(self, params=None, payload=None):
        """
        Summary:
        Get license information
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-license-information
        """
        url = self._base_url + "/enterprise/settings/license"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_all_statistics(self, params=None, payload=None):
        """
        Summary:
        Get all statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-statistics
        """
        url = self._base_url + "/enterprise/stats/all"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_comment_statistics(self, params=None, payload=None):
        """
        Summary:
        Get comment statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-comment-statistics
        """
        url = self._base_url + "/enterprise/stats/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_gist_statistics(self, params=None, payload=None):
        """
        Summary:
        Get gist statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-gist-statistics
        """
        url = self._base_url + "/enterprise/stats/gists"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_hooks_statistics(self, params=None, payload=None):
        """
        Summary:
        Get hooks statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-hooks-statistics
        """
        url = self._base_url + "/enterprise/stats/hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_issue_statistics(self, params=None, payload=None):
        """
        Summary:
        Get issue statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-issues-statistics
        """
        url = self._base_url + "/enterprise/stats/issues"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_milestone_statistics(self, params=None, payload=None):
        """
        Summary:
        Get milestone statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-milestone-statistics
        """
        url = self._base_url + "/enterprise/stats/milestones"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_organization_statistics(self, params=None, payload=None):
        """
        Summary:
        Get organization statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-organization-statistics
        """
        url = self._base_url + "/enterprise/stats/orgs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_pages_statistics(self, params=None, payload=None):
        """
        Summary:
        Get pages statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-pages-statistics
        """
        url = self._base_url + "/enterprise/stats/pages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_pull_request_statistics(self, params=None, payload=None):
        """
        Summary:
        Get pull request statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-pull-requests-statistics
        """
        url = self._base_url + "/enterprise/stats/pulls"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_repository_statistics(self, params=None, payload=None):
        """
        Summary:
        Get repository statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-repository-statistics
        """
        url = self._base_url + "/enterprise/stats/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_users_statistics(self, params=None, payload=None):
        """
        Summary:
        Get users statistics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-users-statistics
        """
        url = self._base_url + "/enterprise/stats/users"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_actions_permissions_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Actions permissions for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-github-actions-permissions-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-github-actions-permissions-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-selected-organizations-enabled-for-github-actions-in-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-selected-organizations-enabled-for-github-actions-in-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#enable-a-selected-organization-for-github-actions-in-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#disable-a-selected-organization-for-github-actions-in-an-enterprise
        """
        url = (
            self._base_url + f"/enterprises/{enterprise}/actions/permissions/organizations/{org_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_allowed_actions_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        Get allowed actions for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-allowed-actions-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/permissions/selected-actions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_allowed_actions_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        Set allowed actions for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-allowed-actions-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-self-hosted-runner-groups-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-self-hosted-runner-group-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-self-hosted-runner-group-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#update-a-self-hosted-runner-group-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-a-self-hosted-runner-group-from-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-organization-access-to-a-self-hosted-runner-group-in-a-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-self-hosted-runners-in-a-group-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-self-hosted-runners-in-a-group-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-a-self-hosted-runner-to-a-group-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-a-self-hosted-runner-from-a-group-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-self-hosted-runners-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_runner_applications_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        List runner applications for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-runner-applications-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/downloads"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_registration_token_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        Create a registration token for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-registration-token-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/actions/runners/registration-token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_remove_token_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        Create a remove token for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#create-a-remove-token-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#get-a-self-hosted-runner-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#delete-self-hosted-runner-from-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#list-labels-for-a-self-hosted-runner-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#add-custom-labels-to-a-self-hosted-runner-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#set-custom-labels-for-a-self-hosted-runner-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-all-custom-labels-from-a-self-hosted-runner-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/actions#remove-a-custom-label-from-a-self-hosted-runner-for-an-enterprise
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
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-the-audit-log-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/audit-log"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_pre_receive_hooks_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List pre-receive hooks for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-pre-receive-hooks-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/pre-receive-hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_pre_receive_hook_for_an_organization(
        self, org, pre_receive_hook_id, params=None, payload=None
    ):
        """
        Summary:
        Get a pre-receive hook for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-a-pre-receive-hook-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_pre_receive_hook_enforcement_for_an_organization(
        self, org, pre_receive_hook_id, params=None, payload=None
    ):
        """
        Summary:
        Update pre-receive hook enforcement for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-pre-receive-hook-enforcement-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def remove_pre_receive_hook_enforcement_for_an_organization(
        self, org, pre_receive_hook_id, params=None, payload=None
    ):
        """
        Summary:
        Remove pre-receive hook enforcement for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#remove-pre-receive-hook-enforcement-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_pre_receive_hooks_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List pre-receive hooks for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-pre-receive-hooks-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pre-receive-hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_pre_receive_hook_for_a_repository(
        self, owner, repo, pre_receive_hook_id, params=None, payload=None
    ):
        """
        Summary:
        Get a pre-receive hook for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-a-pre-receive-hook-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_pre_receive_hook_enforcement_for_a_repository(
        self, owner, repo, pre_receive_hook_id, params=None, payload=None
    ):
        """
        Summary:
        Update pre-receive hook enforcement for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-pre-receive-hook-enforcement-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def remove_pre_receive_hook_enforcement_for_a_repository(
        self, owner, repo, pre_receive_hook_id, params=None, payload=None
    ):
        """
        Summary:
        Remove pre-receive hook enforcement for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#remove-pre-receive-hook-enforcement-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_provisioned_scim_groups_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        List provisioned SCIM groups for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-provisioned-scim-groups-for-an-enterprise
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def provision_a_scim_enterprise_group_and_invite_users(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Provision a SCIM enterprise group and invite users
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#provision-a-scim-enterprise-group-and-invite-users
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_scim_provisioning_information_for_an_enterprise_group(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Summary:
        Get SCIM provisioning information for an enterprise group
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-scim-provisioning-information-for-an-enterprise-group
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_scim_information_for_a_provisioned_enterprise_group(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Summary:
        Set SCIM information for a provisioned enterprise group
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#set-scim-information-for-a-provisioned-enterprise-group
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_attribute_for_a_scim_enterprise_group(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Summary:
        Update an attribute for a SCIM enterprise group
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-an-attribute-for-a-scim-enterprise-group
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_scim_group_from_an_enterprise(
        self, enterprise, scim_group_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a SCIM group from an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-scim-group-from-an-enterprise
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_scim_provisioned_identities_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        List SCIM provisioned identities for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#list-scim-provisioned-identities-for-an-enterprise
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def provision_and_invite_a_scim_enterprise_user(self, enterprise, params=None, payload=None):
        """
        Summary:
        Provision and invite a SCIM enterprise user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#provision-and-invite-a-scim-enterprise-user
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_scim_provisioning_information_for_an_enterprise_user(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Summary:
        Get SCIM provisioning information for an enterprise user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-scim-provisioning-information-for-an-enterprise-user
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_scim_information_for_a_provisioned_enterprise_user(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Summary:
        Set SCIM information for a provisioned enterprise user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#set-scim-information-for-a-provisioned-enterprise-user
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_attribute_for_a_scim_enterprise_user(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Summary:
        Update an attribute for a SCIM enterprise user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#update-an-attribute-for-a-scim-enterprise-user
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_scim_user_from_an_enterprise(
        self, enterprise, scim_user_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a SCIM user from an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#delete-a-scim-user-from-an-enterprise
        """
        url = self._base_url + f"/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_the_configuration_status(self, params=None, payload=None):
        """
        Summary:
        Get the configuration status
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-the-configuration-status
        """
        url = self._base_url + "/setup/api/configcheck"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_a_configuration_process(self, params=None, payload=None):
        """
        Summary:
        Start a configuration process
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#start-a-configuration-process
        """
        url = self._base_url + "/setup/api/configure"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_the_maintenance_status(self, params=None, payload=None):
        """
        Summary:
        Get the maintenance status
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-the-maintenance-status
        """
        url = self._base_url + "/setup/api/maintenance"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def enable_or_disable_maintenance_mode(self, params=None, payload=None):
        """
        Summary:
        Enable or disable maintenance mode
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#enable-or-disable-maintenance-mode
        """
        url = self._base_url + "/setup/api/maintenance"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_settings(self, params=None, payload=None):
        """
        Summary:
        Get settings
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-settings
        """
        url = self._base_url + "/setup/api/settings"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_settings(self, params=None, payload=None):
        """
        Summary:
        Set settings
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#set-settings
        """
        url = self._base_url + "/setup/api/settings"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_all_authorized_ssh_keys(self, params=None, payload=None):
        """
        Summary:
        Get all authorized SSH keys
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#get-all-authorized-ssh-keys
        """
        url = self._base_url + "/setup/api/settings/authorized-keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_an_authorized_ssh_key(self, params=None, payload=None):
        """
        Summary:
        Add an authorized SSH key
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#add-an-authorized-ssh-key
        """
        url = self._base_url + "/setup/api/settings/authorized-keys"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def remove_an_authorized_ssh_key(self, params=None, payload=None):
        """
        Summary:
        Remove an authorized SSH key
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#remove-an-authorized-ssh-key
        """
        url = self._base_url + "/setup/api/settings/authorized-keys"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_github_license(self, params=None, payload=None):
        """
        Summary:
        Create a GitHub license
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#create-a-github-enterprise-server-license
        """
        url = self._base_url + "/setup/api/start"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def upgrade_a_license(self, params=None, payload=None):
        """
        Summary:
        Upgrade a license
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#upgrade-a-license
        """
        url = self._base_url + "/setup/api/upgrade"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def promote_a_user_to_be_a_site_administrator(self, username, params=None, payload=None):
        """
        Summary:
        Promote a user to be a site administrator
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#promote-a-user-to-be-a-site-administrator
        """
        url = self._base_url + f"/users/{username}/site_admin"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def demote_a_site_administrator(self, username, params=None, payload=None):
        """
        Summary:
        Demote a site administrator
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#demote-a-site-administrator
        """
        url = self._base_url + f"/users/{username}/site_admin"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def suspend_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Suspend a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#suspend-a-user
        """
        url = self._base_url + f"/users/{username}/suspended"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unsuspend_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Unsuspend a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/enterprise-admin#unsuspend-a-user
        """
        url = self._base_url + f"/users/{username}/suspended"
        response = self._execute("delete", url, params=params, payload=payload)
        return response
