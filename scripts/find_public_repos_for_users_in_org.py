"""
This script will find all public repos for users in an organization.
"""

from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient, GraphClientError

load_dotenv()
github = GraphClient()

# Get the members of an organization.


def get_org_members(org):
    """
    Get the members of an organization.
    """
    try:
        org_members = []
        results = github.query.get_org_members_with_role(org)
        results = github.query.results_to_list(results)
        for result in results:
            org_members.append(result.get("node").get("login"))
        return org_members
    except GraphClientError as err:
        print(err)


# Get the repos for a user.


def get_public_repos_for_user(user):
    """
    Get the repos for a user.
    """
    try:
        repos = []
        results = github.query.get_users_public_repos(user)
        results = github.query.results_to_list(results)
        for result in results:
            repos.append(result.get("nameWithOwner"))
        return repos
    except GraphClientError as err:
        print(err)


# Get the public repos for all users in the organization.

# Example:

# org_members = get_org_members("engineering")
# for member in org_members:
#    repos = get_public_repos_for_user(member)
#    print(member)
#    print(repos)
