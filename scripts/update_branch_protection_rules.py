"""
This script updates the branch protection rules for a given repository.
"""
from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def update_branch_protection_rules(owner, repo, branch):
    """
    Update the branch protection rules for a given repository.

    input:
        owner: the owner of the repository
        repo: the name of the repository
        branch: the name of the branch

    output:
        json: the response from the GitHub API
    """
    branch_protection_rules = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "required_approving_review_count": 2,
        },
        "restrictions": None,
    }
    try:
        updated_branch_rules = github.repos.update_branch_protection(
            owner=owner, repo=repo, branch=branch, payload=branch_protection_rules
        )
        return updated_branch_rules.json()
    except RestClientError as e:
        print(e)


print(update_branch_protection_rules("bean-dips", "beans", "main"))
