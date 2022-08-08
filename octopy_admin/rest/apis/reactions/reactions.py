"""
Interact with reactions to various GitHub entities.
"""


# pylint: disable=too-many-arguments
class Reactions:
    # pylint: disable=too-many-public-methods
    """
    Interact with reactions to various GitHub entities.
    """

    def __init__(self, client):
        """
        Initialize the Reactions class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_reactions_for_a_team_discussion_comment(
        self, org, team_slug, discussion_number, comment_number, params=None, payload=None
    ):
        """
        List reactions for a team discussion comment
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-team-discussion-comment
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        comment_number
        Payload Parameters:
        content
         per-page
         page
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_team_discussion_comment(
        self, org, team_slug, discussion_number, comment_number, params=None, payload=None
    ):

        """
        Create reaction for a team discussion comment
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-team-discussion-comment
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        comment_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_team_discussion_comment_reaction(
        self,
        org,
        team_slug,
        discussion_number,
        comment_number,
        reaction_id,
        params=None,
        payload=None,
    ):

        """
        Delete team discussion comment reaction
        https://docs.github.com/rest/reference/reactions#delete-team-discussion-comment-reaction
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        comment_number
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_team_discussion(
        self, org, team_slug, discussion_number, params=None, payload=None
    ):
        """
        List reactions for a team discussion
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-team-discussion
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        Payload Parameters:
        content
         per-page
         page
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_team_discussion(
        self, org, team_slug, discussion_number, params=None, payload=None
    ):
        """
        Create reaction for a team discussion
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-team-discussion
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_team_discussion_reaction(
        self, org, team_slug, discussion_number, reaction_id, params=None, payload=None
    ):
        """
        Delete team discussion reaction
        https://docs.github.com/rest/reference/reactions#delete-team-discussion-reaction
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_commit_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        List reactions for a commit comment
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-commit-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:
        content
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_commit_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Create reaction for a commit comment
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-commit-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_commit_comment_reaction(
        self, owner, repo, comment_id, reaction_id, params=None, payload=None
    ):
        """
        Delete a commit comment reaction
        https://docs.github.com/rest/reference/reactions#delete-a-commit-comment-reaction
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_an_issue_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        List reactions for an issue comment
        https://docs.github.com/rest/reference/reactions#list-reactions-for-an-issue-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:
        content
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_an_issue_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Create reaction for an issue comment
        https://docs.github.com/rest/reference/reactions#create-reaction-for-an-issue-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_an_issue_comment_reaction(
        self, owner, repo, comment_id, reaction_id, params=None, payload=None
    ):
        """
        Delete an issue comment reaction
        https://docs.github.com/rest/reference/reactions#delete-an-issue-comment-reaction
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        List reactions for an issue
        https://docs.github.com/rest/reference/reactions#list-reactions-for-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:
        content
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Create reaction for an issue
        https://docs.github.com/rest/reference/reactions#create-reaction-for-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_an_issue_reaction(
        self, owner, repo, issue_number, reaction_id, params=None, payload=None
    ):
        """
        Delete an issue reaction
        https://docs.github.com/rest/reference/reactions#delete-an-issue-reaction
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_pull_request_review_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        List reactions for a pull request review comment
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-pull-request-review-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:
        content
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_pull_request_review_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Create reaction for a pull request review comment
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-pull-request-review-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_pull_request_comment_reaction(
        self, owner, repo, comment_id, reaction_id, params=None, payload=None
    ):

        """
        Delete a pull request comment reaction
        https://docs.github.com/rest/reference/reactions#delete-a-pull-request-comment-reaction
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_pull_request_thread_comment(
        self, owner, repo, pull_number, thread_id, comment_id, params=None, payload=None
    ):

        """
        List reactions for a pull request thread comment
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-pull-request-thread-comment
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        thread_id
        comment_id
        Payload Parameters:
        content
         per-page
         page
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments/{comment_id}/reactions"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_reaction_to_a_pull_request_thread_comment(
        self, owner, repo, pull_number, thread_id, comment_id, params=None, payload=None
    ):

        """
        Create a reaction to a pull request thread comment
        https://docs.github.com/rest/reference/reactions#create-a-reaction-to-a-pull-request-thread-comment
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        thread_id
        comment_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments/{comment_id}/reactions"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_reaction_to_a_pull_request_thread_comment(
        self,
        owner,
        repo,
        pull_number,
        thread_id,
        comment_id,
        reaction_id,
        params=None,
        payload=None,
    ):

        """
        Delete a reaction to a pull request thread comment
        https://docs.github.com/rest/reference/reactions#delete-a-thread-comment-reaction
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        thread_id
        comment_id
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments/{comment_id}/reactions/{reaction_id}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        List reactions for a release
        https://docs.github.com/rest/reference/reactions/#list-reactions-for-a-release
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        Payload Parameters:
        content
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Create reaction for a release
        https://docs.github.com/rest/reference/reactions/#create-reaction-for-a-release
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_release_reaction(
        self, owner, repo, release_id, reaction_id, params=None, payload=None
    ):
        """
        Delete a release reaction
        https://docs.github.com/rest/reference/reactions/#delete-a-release-reaction
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        reaction_id
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_team_discussion_comment__legacy(
        self, team_id, discussion_number, comment_number, params=None, payload=None
    ):
        """
        List reactions for a team discussion comment (Legacy)
        https://docs.github.com/rest/reference/reactions/#list-reactions-for-a-team-discussion-comment-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        comment_number
        Payload Parameters:
        content
         per-page
         page
        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_team_discussion_comment__legacy(
        self, team_id, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Create reaction for a team discussion comment (Legacy)
        https://docs.github.com/rest/reference/reactions/#create-reaction-for-a-team-discussion-comment-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        comment_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_team_discussion__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        List reactions for a team discussion (Legacy)
        https://docs.github.com/rest/reference/reactions/#list-reactions-for-a-team-discussion-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        Payload Parameters:
        content
         per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_team_discussion__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        Create reaction for a team discussion (Legacy)
        https://docs.github.com/rest/reference/reactions/#create-reaction-for-a-team-discussion-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response
