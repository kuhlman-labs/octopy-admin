"""
Interact with GitHub Orgs.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Orgs:
    """
    Interact with GitHub Orgs.
    """

    def __init__(self, client):
        """
        Initializes the Orgs class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organizations(self, params=None, payload=None):
        """
        Summary:
        List organizations
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-organizations
        """
        url = self._base_url + "/organizations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_custom_repository_roles_in_an_organization(
        self, organization_id, params=None, payload=None
    ):
        """
        Summary:
        List custom repository roles in an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-custom-repository-roles-in-an-organization
        """
        url = self._base_url + f"/organizations/{organization_id}/custom_roles"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Get an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#get-an-organization
        """
        url = self._base_url + f"/orgs/{org}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Update an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs/#update-an-organization
        """
        url = self._base_url + f"/orgs/{org}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_the_audit_log_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        Get the audit log for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#get-audit-log
        """
        url = self._base_url + f"/orgs/{org}/audit-log"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_users_blocked_by_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List users blocked by an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-users-blocked-by-an-organization
        """
        url = self._base_url + f"/orgs/{org}/blocks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_user_is_blocked_by_an_organization(
        self, org, username, params=None, payload=None
    ):
        """
        Summary:
        Check if a user is blocked by an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#check-if-a-user-is-blocked-by-an-organization
        """
        url = self._base_url + f"/orgs/{org}/blocks/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def block_a_user_from_an_organization(self, org, username, params=None, payload=None):
        """
        Summary:
        Block a user from an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#block-a-user-from-an-organization
        """
        url = self._base_url + f"/orgs/{org}/blocks/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unblock_a_user_from_an_organization(self, org, username, params=None, payload=None):
        """
        Summary:
        Unblock a user from an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#unblock-a-user-from-an-organization
        """
        url = self._base_url + f"/orgs/{org}/blocks/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_saml_sso_authorizations_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List SAML SSO authorizations for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-saml-sso-authorizations-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/credential-authorizations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def remove_a_saml_sso_authorization_for_an_organization(
        self, org, credential_id, params=None, payload=None
    ):
        """
        Summary:
        Remove a SAML SSO authorization for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#remove-a-saml-sso-authorization-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/credential-authorizations/{credential_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_custom_role(self, org, params=None, payload=None):
        """
        Summary:
        Create a custom role
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#create-a-custom-role
        """
        url = self._base_url + f"/orgs/{org}/custom_roles"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_a_custom_role(self, org, role_id, params=None, payload=None):
        """
        Summary:
        Update a custom role
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#update-a-custom-role
        """
        url = self._base_url + f"/orgs/{org}/custom_roles/{role_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_custom_role(self, org, role_id, params=None, payload=None):
        """
        Summary:
        Delete a custom role
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#delete-a-custom-role
        """
        url = self._base_url + f"/orgs/{org}/custom_roles/{role_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_failed_organization_invitations(self, org, params=None, payload=None):
        """
        Summary:
        List failed organization invitations
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-failed-organization-invitations
        """
        url = self._base_url + f"/orgs/{org}/failed_invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_fine_grained_permissions_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List fine-grained permissions for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-fine-grained-permissions-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/fine_grained_permissions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organization_webhooks(self, org, params=None, payload=None):
        """
        Summary:
        List organization webhooks
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-organization-webhooks
        """
        url = self._base_url + f"/orgs/{org}/hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_webhook(self, org, params=None, payload=None):
        """
        Summary:
        Create an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#create-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Summary:
        Get an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#get-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Summary:
        Update an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#update-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Summary:
        Delete an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#delete-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_webhook_configuration_for_an_organization(
        self, org, hook_id, params=None, payload=None
    ):
        """
        Summary:
        Get a webhook configuration for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#get-a-webhook-configuration-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/config"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_webhook_configuration_for_an_organization(
        self, org, hook_id, params=None, payload=None
    ):
        """
        Summary:
        Update a webhook configuration for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#update-a-webhook-configuration-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/config"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_deliveries_for_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Summary:
        List deliveries for an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-deliveries-for-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/deliveries"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_webhook_delivery_for_an_organization_webhook(
        self, org, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Summary:
        Get a webhook delivery for an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#get-a-webhook-delivery-for-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def redeliver_a_delivery_for_an_organization_webhook(
        self, org, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Summary:
        Redeliver a delivery for an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#redeliver-a-delivery-for-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def ping_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Summary:
        Ping an organization webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#ping-an-organization-webhook
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/pings"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_app_installations_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List app installations for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-app-installations-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/installations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_pending_organization_invitations(self, org, params=None, payload=None):
        """
        Summary:
        List pending organization invitations
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-pending-organization-invitations
        """
        url = self._base_url + f"/orgs/{org}/invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_invitation(self, org, params=None, payload=None):
        """
        Summary:
        Create an organization invitation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#create-an-organization-invitation
        """
        url = self._base_url + f"/orgs/{org}/invitations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def cancel_an_organization_invitation(self, org, invitation_id, params=None, payload=None):
        """
        Summary:
        Cancel an organization invitation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#cancel-an-organization-invitation
        """
        url = self._base_url + f"/orgs/{org}/invitations/{invitation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_organization_invitation_teams(self, org, invitation_id, params=None, payload=None):
        """
        Summary:
        List organization invitation teams
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-organization-invitation-teams
        """
        url = self._base_url + f"/orgs/{org}/invitations/{invitation_id}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organization_members(self, org, params=None, payload=None):
        """
        Summary:
        List organization members
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-organization-members
        """
        url = self._base_url + f"/orgs/{org}/members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Summary:
        Check organization membership for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#check-organization-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/members/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def remove_an_organization_member(self, org, username, params=None, payload=None):
        """
        Summary:
        Remove an organization member
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#remove-an-organization-member
        """
        url = self._base_url + f"/orgs/{org}/members/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Summary:
        Get organization membership for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#get-organization-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/memberships/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Summary:
        Set organization membership for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#set-organization-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/memberships/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Summary:
        Remove organization membership for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#remove-organization-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/memberships/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_outside_collaborators_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List outside collaborators for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-outside-collaborators-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/outside_collaborators"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def convert_an_organization_member_to_outside_collaborator(
        self, org, username, params=None, payload=None
    ):
        """
        Summary:
        Convert an organization member to outside collaborator
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#convert-an-organization-member-to-outside-collaborator
        """
        url = self._base_url + f"/orgs/{org}/outside_collaborators/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_outside_collaborator_from_an_organization(
        self, org, username, params=None, payload=None
    ):
        """
        Summary:
        Remove outside collaborator from an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#remove-outside-collaborator-from-an-organization
        """
        url = self._base_url + f"/orgs/{org}/outside_collaborators/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_public_organization_members(self, org, params=None, payload=None):
        """
        Summary:
        List public organization members
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-public-organization-members
        """
        url = self._base_url + f"/orgs/{org}/public_members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_public_organization_membership_for_a_user(
        self, org, username, params=None, payload=None
    ):
        """
        Summary:
        Check public organization membership for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#check-public-organization-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/public_members/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_public_organization_membership_for_the_authenticated_user(
        self, org, username, params=None, payload=None
    ):
        """
        Summary:
        Set public organization membership for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#set-public-organization-membership-for-the-authenticated-user
        """
        url = self._base_url + f"/orgs/{org}/public_members/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_public_organization_membership_for_the_authenticated_user(
        self, org, username, params=None, payload=None
    ):
        """
        Summary:
        Remove public organization membership for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#remove-public-organization-membership-for-the-authenticated-user
        """
        url = self._base_url + f"/orgs/{org}/public_members/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_security_manager_teams(self, org, params=None, payload=None):
        """
        Summary:
        List security manager teams
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-security-manager-teams
        """
        url = self._base_url + f"/orgs/{org}/security-managers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_a_security_manager_team(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        Add a security manager team
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#add-a-security-manager-team
        """
        url = self._base_url + f"/orgs/{org}/security-managers/teams/{team_slug}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_security_manager_team(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        Remove a security manager team
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#remove-a-security-manager-team
        """
        url = self._base_url + f"/orgs/{org}/security-managers/teams/{team_slug}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def enable_or_disable_a_security_feature_for_an_organization(
        self, org, security_product, enablement, params=None, payload=None
    ):
        """
        Summary:
        Enable or disable a security feature for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#enable-or-disable-security-product-on-all-org-repos
        """
        url = self._base_url + f"/orgs/{org}/{security_product}/{enablement}"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_organization_memberships_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List organization memberships for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-organization-memberships-for-the-authenticated-user
        """
        url = self._base_url + "/user/memberships/orgs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_membership_for_the_authenticated_user(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        Get an organization membership for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#get-an-organization-membership-for-the-authenticated-user
        """
        url = self._base_url + f"/user/memberships/orgs/{org}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_organization_membership_for_the_authenticated_user(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        Update an organization membership for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#update-an-organization-membership-for-the-authenticated-user
        """
        url = self._base_url + f"/user/memberships/orgs/{org}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_organizations_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List organizations for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-organizations-for-the-authenticated-user
        """
        url = self._base_url + "/user/orgs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organizations_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List organizations for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/orgs#list-organizations-for-a-user
        """
        url = self._base_url + f"/users/{username}/orgs"
        response = self._execute("get", url, params=params, payload=payload)
        return response
