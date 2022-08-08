"""
Provisioning of GitHub organization membership for SCIM-enabled providers.
"""


# pylint: disable=too-many-arguments
class Scim:
    """
    Provisioning of GitHub organization membership for SCIM-enabled providers.
    """

    def __init__(self, client):
        """
        Initialize the Scim class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_scim_provisioned_identities(self, org, params=None, payload=None):
        """
        List SCIM provisioned identities
        https://docs.github.com/rest/reference/scim#list-scim-provisioned-identities
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        startIndex
         count
         filter
        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def provision_and_invite_a_scim_user(self, org, params=None, payload=None):
        """
        Provision and invite a SCIM user
        https://docs.github.com/rest/reference/scim#provision-and-invite-a-scim-user
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_scim_provisioning_information_for_a_user(
        self, org, scim_user_id, params=None, payload=None
    ):
        """
        Get SCIM provisioning information for a user
        https://docs.github.com/rest/reference/scim#get-scim-provisioning-information-for-a-user
        Attributes:
        Path Parameters:
        org
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_provisioned_organization_membership(
        self, org, scim_user_id, params=None, payload=None
    ):
        """
        Update a provisioned organization membership
        https://docs.github.com/rest/reference/scim#set-scim-information-for-a-provisioned-user
        Attributes:
        Path Parameters:
        org
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_attribute_for_a_scim_user(self, org, scim_user_id, params=None, payload=None):
        """
        Update an attribute for a SCIM user
        https://docs.github.com/rest/reference/scim#update-an-attribute-for-a-scim-user
        Attributes:
        Path Parameters:
        org
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_scim_user_from_an_organization(self, org, scim_user_id, params=None, payload=None):
        """
        Delete a SCIM user from an organization
        https://docs.github.com/rest/reference/scim#delete-a-scim-user-from-an-organization
        Attributes:
        Path Parameters:
        org
        scim_user_id
        Payload Parameters:

        """
        url = self._base_url + f"/scim/v2/organizations/{org}/Users/{scim_user_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response
