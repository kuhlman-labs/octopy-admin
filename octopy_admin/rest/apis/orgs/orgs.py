"""
Interact with GitHub Orgs.
"""


# pylint: disable=too-many-arguments
class Orgs:
    # pylint: disable=too-many-public-methods
    """
    Interact with GitHub Orgs.
    """

    def __init__(self, client):
        """
        Initialize the Orgs class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organizations(self, params=None, payload=None):
        """
        List organizations
        https://docs.github.com/rest/reference/orgs#list-organizations
        Attributes:
        Path Parameters:

        Payload Parameters:
        since-org
         per-page
        """
        url = self._base_url + "/organizations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_custom_repository_roles_in_an_organization(
        self, organization_id, params=None, payload=None
    ):
        """
        List custom repository roles in an organization
        https://docs.github.com/rest/reference/orgs#list-custom-repository-roles-in-an-organization
        Attributes:
        Path Parameters:
        organization_id
        Payload Parameters:

        """
        url = self._base_url + f"/organizations/{organization_id}/custom_roles"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization(self, org, params=None, payload=None):
        """
        Get an organization
        https://docs.github.com/rest/reference/orgs#get-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_organization(self, org, params=None, payload=None):
        """
        Update an organization
        https://docs.github.com/rest/reference/orgs/#update-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_the_audit_log_for_an_organization(self, org, params=None, payload=None):
        """
        Get the audit log for an organization
        https://docs.github.com/rest/reference/orgs#get-audit-log
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        audit-log-phrase
         audit-log-include
         audit-log-after
         audit-log-before
         audit-log-order
         per-page
        """
        url = self._base_url + f"/orgs/{org}/audit-log"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_users_blocked_by_an_organization(self, org, params=None, payload=None):
        """
        List users blocked by an organization
        https://docs.github.com/rest/reference/orgs#list-users-blocked-by-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/blocks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_user_is_blocked_by_an_organization(
        self, org, username, params=None, payload=None
    ):
        """
        Check if a user is blocked by an organization
        https://docs.github.com/rest/reference/orgs#check-if-a-user-is-blocked-by-an-organization
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/blocks/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def block_a_user_from_an_organization(self, org, username, params=None, payload=None):
        """
        Block a user from an organization
        https://docs.github.com/rest/reference/orgs#block-a-user-from-an-organization
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/blocks/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unblock_a_user_from_an_organization(self, org, username, params=None, payload=None):
        """
        Unblock a user from an organization
        https://docs.github.com/rest/reference/orgs#unblock-a-user-from-an-organization
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/blocks/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_saml_sso_authorizations_for_an_organization(self, org, params=None, payload=None):
        """
        List SAML SSO authorizations for an organization
        https://docs.github.com/rest/reference/orgs#list-saml-sso-authorizations-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
         login
        """
        url = self._base_url + f"/orgs/{org}/credential-authorizations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def remove_a_saml_sso_authorization_for_an_organization(
        self, org, credential_id, params=None, payload=None
    ):
        """
        Remove a SAML SSO authorization for an organization
        https://docs.github.com/rest/reference/orgs#remove-a-saml-sso-authorization-for-an-organization
        Attributes:
        Path Parameters:
        org
        credential_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/credential-authorizations/{credential_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_failed_organization_invitations(self, org, params=None, payload=None):
        """
        List failed organization invitations
        https://docs.github.com/rest/reference/orgs#list-failed-organization-invitations
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/failed_invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organization_webhooks(self, org, params=None, payload=None):
        """
        List organization webhooks
        https://docs.github.com/rest/reference/orgs#list-organization-webhooks
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_webhook(self, org, params=None, payload=None):
        """
        Create an organization webhook
        https://docs.github.com/rest/reference/orgs#create-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Get an organization webhook
        https://docs.github.com/rest/reference/orgs#get-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Update an organization webhook
        https://docs.github.com/rest/reference/orgs#update-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Delete an organization webhook
        https://docs.github.com/rest/reference/orgs#delete-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_webhook_configuration_for_an_organization(
        self, org, hook_id, params=None, payload=None
    ):
        """
        Get a webhook configuration for an organization
        https://docs.github.com/rest/reference/orgs#get-a-webhook-configuration-for-an-organization
        Attributes:
        Path Parameters:
        org
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/config"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_webhook_configuration_for_an_organization(
        self, org, hook_id, params=None, payload=None
    ):
        """
        Update a webhook configuration for an organization
        https://docs.github.com/rest/reference/orgs#update-a-webhook-configuration-for-an-organization
        Attributes:
        Path Parameters:
        org
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/config"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_deliveries_for_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        List deliveries for an organization webhook
        https://docs.github.com/rest/reference/orgs#list-deliveries-for-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        hook_id
        Payload Parameters:
        per-page
         cursor
        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/deliveries"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_webhook_delivery_for_an_organization_webhook(
        self, org, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Get a webhook delivery for an organization webhook
        https://docs.github.com/rest/reference/orgs#get-a-webhook-delivery-for-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        hook_id
        delivery_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def redeliver_a_delivery_for_an_organization_webhook(
        self, org, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Redeliver a delivery for an organization webhook
        https://docs.github.com/rest/reference/orgs#redeliver-a-delivery-for-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        hook_id
        delivery_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def ping_an_organization_webhook(self, org, hook_id, params=None, payload=None):
        """
        Ping an organization webhook
        https://docs.github.com/rest/reference/orgs#ping-an-organization-webhook
        Attributes:
        Path Parameters:
        org
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}/pings"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_app_installations_for_an_organization(self, org, params=None, payload=None):
        """
        List app installations for an organization
        https://docs.github.com/rest/reference/orgs#list-app-installations-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/installations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_pending_organization_invitations(self, org, params=None, payload=None):
        """
        List pending organization invitations
        https://docs.github.com/rest/reference/orgs#list-pending-organization-invitations
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_invitation(self, org, params=None, payload=None):
        """
        Create an organization invitation
        https://docs.github.com/rest/reference/orgs#create-an-organization-invitation
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/invitations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def cancel_an_organization_invitation(self, org, invitation_id, params=None, payload=None):
        """
        Cancel an organization invitation
        https://docs.github.com/rest/reference/orgs#cancel-an-organization-invitation
        Attributes:
        Path Parameters:
        org
        invitation_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/invitations/{invitation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_organization_invitation_teams(self, org, invitation_id, params=None, payload=None):
        """
        List organization invitation teams
        https://docs.github.com/rest/reference/orgs#list-organization-invitation-teams
        Attributes:
        Path Parameters:
        org
        invitation_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/invitations/{invitation_id}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organization_members(self, org, params=None, payload=None):
        """
        List organization members
        https://docs.github.com/rest/reference/orgs#list-organization-members
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        filter
         role
         per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Check organization membership for a user
        https://docs.github.com/rest/reference/orgs#check-organization-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/members/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def remove_an_organization_member(self, org, username, params=None, payload=None):
        """
        Remove an organization member
        https://docs.github.com/rest/reference/orgs#remove-an-organization-member
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/members/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Get organization membership for a user
        https://docs.github.com/rest/reference/orgs#get-organization-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/memberships/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Set organization membership for a user
        https://docs.github.com/rest/reference/orgs#set-organization-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/memberships/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_organization_membership_for_a_user(self, org, username, params=None, payload=None):
        """
        Remove organization membership for a user
        https://docs.github.com/rest/reference/orgs#remove-organization-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/memberships/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_outside_collaborators_for_an_organization(self, org, params=None, payload=None):
        """
        List outside collaborators for an organization
        https://docs.github.com/rest/reference/orgs#list-outside-collaborators-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        filter
         per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/outside_collaborators"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def convert_an_organization_member_to_outside_collaborator(
        self, org, username, params=None, payload=None
    ):
        """
        Convert an organization member to outside collaborator
        https://docs.github.com/rest/reference/orgs#convert-an-organization-member-to-outside-collaborator
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/outside_collaborators/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_outside_collaborator_from_an_organization(
        self, org, username, params=None, payload=None
    ):
        """
        Remove outside collaborator from an organization
        https://docs.github.com/rest/reference/orgs#remove-outside-collaborator-from-an-organization
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/outside_collaborators/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_public_organization_members(self, org, params=None, payload=None):
        """
        List public organization members
        https://docs.github.com/rest/reference/orgs#list-public-organization-members
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/public_members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_public_organization_membership_for_a_user(
        self, org, username, params=None, payload=None
    ):
        """
        Check public organization membership for a user
        https://docs.github.com/rest/reference/orgs#check-public-organization-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/public_members/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_public_organization_membership_for_the_authenticated_user(
        self, org, username, params=None, payload=None
    ):
        """
        Set public organization membership for the authenticated user
        https://docs.github.com/rest/reference/orgs#set-public-organization-membership-for-the-authenticated-user
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/public_members/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_public_organization_membership_for_the_authenticated_user(
        self, org, username, params=None, payload=None
    ):
        """
        Remove public organization membership for the authenticated user
        https://docs.github.com/rest/reference/orgs#remove-public-organization-membership-for-the-authenticated-user
        Attributes:
        Path Parameters:
        org
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/public_members/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_organization_memberships_for_the_authenticated_user(self, params=None, payload=None):
        """
        List organization memberships for the authenticated user
        https://docs.github.com/rest/reference/orgs#list-organization-memberships-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        state
         per-page
         page
        """
        url = self._base_url + "/user/memberships/orgs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_membership_for_the_authenticated_user(
        self, org, params=None, payload=None
    ):
        """
        Get an organization membership for the authenticated user
        https://docs.github.com/rest/reference/orgs#get-an-organization-membership-for-the-authenticated-user
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/user/memberships/orgs/{org}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_organization_membership_for_the_authenticated_user(
        self, org, params=None, payload=None
    ):
        """
        Update an organization membership for the authenticated user
        https://docs.github.com/rest/reference/orgs#update-an-organization-membership-for-the-authenticated-user
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/user/memberships/orgs/{org}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_organizations_for_the_authenticated_user(self, params=None, payload=None):
        """
        List organizations for the authenticated user
        https://docs.github.com/rest/reference/orgs#list-organizations-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/orgs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organizations_for_a_user(self, username, params=None, payload=None):
        """
        List organizations for a user
        https://docs.github.com/rest/reference/orgs#list-organizations-for-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/users/{username}/orgs"
        response = self._execute("get", url, params=params, payload=payload)
        return response
