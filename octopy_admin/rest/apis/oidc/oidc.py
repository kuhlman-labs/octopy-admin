"""
Endpoints to manage GitHub OIDC configuration using the REST API.
"""


class Oidc:
    """
    Endpoints to manage GitHub OIDC configuration using the REST API.
    """

    def __init__(self, client):
        """
        Initialize the Oidc class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_the_customization_template_for_an_oidc_subject_claim_for_an_organization(
        self, org, payload=None
    ):
        """
        Get the customization template for an OIDC subject claim for an organization
        https://docs.github.com/rest/actions/oidc#get-the-customization-template-for-an-oidc-subject-claim-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/oidc/customization/sub"
        response = self._execute("get", url, payload)
        return response

    def set_the_customization_template_for_an_oidc_subject_claim_for_an_organization(
        self, org, payload=None
    ):
        """
        Set the customization template for an OIDC subject claim for an organization
        https://docs.github.com/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/actions/oidc/customization/sub"
        response = self._execute("put", url, payload)
        return response
