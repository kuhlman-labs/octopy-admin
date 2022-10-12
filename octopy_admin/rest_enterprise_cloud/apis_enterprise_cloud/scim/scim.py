"""
Provisioning of GitHub organization membership for SCIM-enabled providers.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Scim:
    """
    Provisioning of GitHub organization membership for SCIM-enabled providers.
    """

    def __init__(self, client):
        """
        Initializes the Scim class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_scim_provisioned_identities(self, org, params=None, payload=None):
        """
        Summary:
        List SCIM provisioned identities
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/scim#list-scim-provisioned-identities
        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def provision_and_invite_a_scim_user(self, org, params=None, payload=None):
        """
        Summary:
        Provision and invite a SCIM user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/scim#provision-and-invite-a-scim-user
        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_scim_provisioning_information_for_a_user(
        self, org, scim_user_id, params=None, payload=None
    ):
        """
        Summary:
        Get SCIM provisioning information for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/scim#get-scim-provisioning-information-for-a-user
        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_provisioned_organization_membership(
        self, org, scim_user_id, params=None, payload=None
    ):
        """
        Summary:
        Update a provisioned organization membership
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/scim#set-scim-information-for-a-provisioned-user
        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_attribute_for_a_scim_user(self, org, scim_user_id, params=None, payload=None):
        """
        Summary:
        Update an attribute for a SCIM user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/scim#update-an-attribute-for-a-scim-user
        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_scim_user_from_an_organization(self, org, scim_user_id, params=None, payload=None):
        """
        Summary:
        Delete a SCIM user from an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/scim#delete-a-scim-user-from-an-organization
        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response
