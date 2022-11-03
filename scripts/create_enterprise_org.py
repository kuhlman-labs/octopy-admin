"""
This script will use the GitHub GraphQL API to create an enterprise organization.
"""

from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient, GraphClientError

load_dotenv()
github = GraphClient()


def get_enterprise_id(enterprise_name):
    """
    Get the enterprise ID.
    """
    try:
        query = github.query.get_enterprise_id(enterprise_name)
        print(query)
        return query.get("enterprise").get("id")
    except GraphClientError as e:
        print(e)


def create_enterprise_org(enterprise_id, org_name):
    """
    Create an enterprise organization.
    """
    try:
        query = github.mutation.add_enterprise_org(
            organization={
                "adminLogins": ["kuhlman-labs"],
                "billingEmail": "kuhlman-labs@github.com",
                "enterpriseId": enterprise_id,
                "login": org_name,
                "profileName": org_name,
            }
        )
        print(query)
    except GraphClientError as e:
        print(e)


# example

enterprise_id = get_enterprise_id("GitHub")
org_name = "kuhlman-labs-test-org"

create_enterprise_org(enterprise_id=enterprise_id, org_name=org_name)
