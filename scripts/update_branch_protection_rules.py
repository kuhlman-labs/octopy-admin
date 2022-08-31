"""
This script updates the branch protection rules for a given repository.
"""
from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def update_branch_protection_rules(owner, repo, branch, rules):
    """
    Update the branch protection rules for a given repository.
    """
    try:
        branch_rules = github.repos.update_branch_protection(
            owner=owner, repo=repo, branch=branch, payload=rules
        )
        return branch_rules.json()
    except RestClientError as e:
        print(e)


# example
# update_branch_protection_rules(
#    owner='Engineering',
#    repo='platform',
#    branch='main',
#    rules={"required_status_checks":{"strict":True,"contexts":["continuous-integration/travis-ci"]},
#    "enforce_admins":True,
#    "required_pull_request_reviews":{"dismissal_restrictions":{"users":["octocat"],"teams":["justice-league"]},
#    "dismiss_stale_reviews":True,
#    "require_code_owner_reviews":True,
#    "required_approving_review_count":2,
#    "bypass_pull_request_allowances":{"users":["kuhlman-labs"],"teams":["justice-league"]}},
#    "restrictions":{"users":["kuhlman-labs"],"teams":["justice-league"]},
#    "required_linear_history":True,
#    "allow_force_pushes":True,
#    "allow_deletions":True,
#    "block_creations":True,
#    "required_conversation_resolution":True})
