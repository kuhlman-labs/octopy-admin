"""
This script will create branch protection rules for a given owner, repo and pattern.

Available rule arguments:
https://docs.github.com/en/graphql/reference/input-objects#createbranchprotectionruleinput

allowsForcePushes: Boolean
Are force pushes allowed on this branch.

blocksCreations: Boolean
Is branch creation a protected operation.

bypassForcePushActorIds: [ID!]
A list of User or Team IDs allowed to bypass force push targeting matching branches.

bypassPullRequestActorIds: [ID!]
A list of User or Team IDs allowed to bypass pull requests targeting matching branches.

clientMutationId: String
A unique identifier for the client performing the mutation.

dismissesStaleReviews: Boolean
Will new commits pushed to matching branches dismiss pull request review approvals.

isAdminEnforced: Boolean
Can admins overwrite branch protection.

pattern: String!
The glob-like pattern used to determine matching branches.

pushActorIds: [ID!]
A list of User, Team or App IDs allowed to push to matching branches.

repositoryId: ID!
The global relay id of the repository in which a new branch protection rule should be created in.

requiredApprovingReviewCount: Int
Number of approving reviews required to update matching branches.

requiredStatusCheckContexts: [String!]
List of required status check contexts that must pass for commits to be accepted to matching branches.

requiredStatusChecks: [RequiredStatusCheckInput!]
The list of required status checks

requiresApprovingReviews: Boolean
Are approving reviews required to update matching branches.

requiresCodeOwnerReviews: Boolean
Are reviews from code owners required to update matching branches.

requiresCommitSignatures: Boolean
Are commits required to be signed.

requiresConversationResolution: Boolean
Are conversations required to be resolved before merging.

requiresLinearHistory: Boolean
Are merge commits prohibited from being pushed to this branch.

requiresStatusChecks: Boolean
Are status checks required to update matching branches.

requiresStrictStatusChecks: Boolean
Are branches required to be up to date before merging.

restrictsPushes: Boolean
Is pushing to matching branches restricted.

restrictsReviewDismissals: Boolean
Is dismissal of pull request reviews restricted.

reviewDismissalActorIds: [ID!]
A list of User or Team IDs allowed to dismiss reviews on pull requests targeting matching branches.
"""

from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient, GraphClientError

load_dotenv()
github = GraphClient()


def get_repo_id(owner, name):
    """
    Get the repo id.
    """
    try:
        results = github.query.get_repo_id(owner, name)
        return results.get("repository").get("id")
    except GraphClientError as e:
        print(e)


def create_branch_protection_rule(owner, repo, pattern):
    """
    Create a branch protection rule.
    """
    try:
        rule = {
            "allowsDeletions": True,
            "pattern": pattern,
            "repositoryId": get_repo_id(owner, repo),
        }
        results = github.mutation.create_branch_protection_rule(rule)
        return print(results)
    except GraphClientError as e:
        print(e)


# example
# create_branch_protection_rule(owner="Engineering", repo="platform", pattern="release")
