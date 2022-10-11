"""
Interact with reactions to various GitHub entities.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Reactions:
    """
    Interact with reactions to various GitHub entities.
    """

    def __init__(self, client):
        """
        Initializes the Reactions class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_reactions_for_a_team_discussion_comment(
        self,
        org,
        team_slug,
        discussion_number,
        comment_number,
        params=None,
        payload=None,
    ):
        """
        Summary:
        List reactions for a team discussion comment
        Docs:
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-team-discussion-comment
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_team_discussion_comment(
        self,
        org,
        team_slug,
        discussion_number,
        comment_number,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Create reaction for a team discussion comment
        Docs:
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-team-discussion-comment
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"
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
        Summary:
        Delete team discussion comment reaction
        Docs:
        https://docs.github.com/rest/reference/reactions#delete-team-discussion-comment-reaction
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_team_discussion(
        self, org, team_slug, discussion_number, params=None, payload=None
    ):
        """
        Summary:
        List reactions for a team discussion
        Docs:
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-team-discussion
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
        Summary:
        Create reaction for a team discussion
        Docs:
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-team-discussion
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
        Summary:
        Delete team discussion reaction
        Docs:
        https://docs.github.com/rest/reference/reactions#delete-team-discussion-reaction
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_commit_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Summary:
        List reactions for a commit comment
        Docs:
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-commit-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_commit_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Summary:
        Create reaction for a commit comment
        Docs:
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-commit-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_commit_comment_reaction(
        self, owner, repo, comment_id, reaction_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a commit comment reaction
        Docs:
        https://docs.github.com/rest/reference/reactions#delete-a-commit-comment-reaction
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
        Summary:
        List reactions for an issue comment
        Docs:
        https://docs.github.com/rest/reference/reactions#list-reactions-for-an-issue-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_an_issue_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Summary:
        Create reaction for an issue comment
        Docs:
        https://docs.github.com/rest/reference/reactions#create-reaction-for-an-issue-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_an_issue_comment_reaction(
        self, owner, repo, comment_id, reaction_id, params=None, payload=None
    ):
        """
        Summary:
        Delete an issue comment reaction
        Docs:
        https://docs.github.com/rest/reference/reactions#delete-an-issue-comment-reaction
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        List reactions for an issue
        Docs:
        https://docs.github.com/rest/reference/reactions#list-reactions-for-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Create reaction for an issue
        Docs:
        https://docs.github.com/rest/reference/reactions#create-reaction-for-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_an_issue_reaction(
        self, owner, repo, issue_number, reaction_id, params=None, payload=None
    ):
        """
        Summary:
        Delete an issue reaction
        Docs:
        https://docs.github.com/rest/reference/reactions#delete-an-issue-reaction
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
        Summary:
        List reactions for a pull request review comment
        Docs:
        https://docs.github.com/rest/reference/reactions#list-reactions-for-a-pull-request-review-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_pull_request_review_comment(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Summary:
        Create reaction for a pull request review comment
        Docs:
        https://docs.github.com/rest/reference/reactions#create-reaction-for-a-pull-request-review-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_pull_request_comment_reaction(
        self, owner, repo, comment_id, reaction_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a pull request comment reaction
        Docs:
        https://docs.github.com/rest/reference/reactions#delete-a-pull-request-comment-reaction
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Summary:
        List reactions for a release
        Docs:
        https://docs.github.com/rest/reference/reactions/#list-reactions-for-a-release
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Summary:
        Create reaction for a release
        Docs:
        https://docs.github.com/rest/reference/reactions/#create-reaction-for-a-release
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_release_reaction(
        self, owner, repo, release_id, reaction_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a release reaction
        Docs:
        https://docs.github.com/rest/reference/reactions/#delete-a-release-reaction
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
        Summary:
        List reactions for a team discussion comment (Legacy)
        Docs:
        https://docs.github.com/rest/reference/reactions/#list-reactions-for-a-team-discussion-comment-legacy
        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_team_discussion_comment__legacy(
        self, team_id, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Summary:
        Create reaction for a team discussion comment (Legacy)
        Docs:
        https://docs.github.com/rest/reference/reactions/#create-reaction-for-a-team-discussion-comment-legacy
        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_reactions_for_a_team_discussion__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        Summary:
        List reactions for a team discussion (Legacy)
        Docs:
        https://docs.github.com/rest/reference/reactions/#list-reactions-for-a-team-discussion-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/reactions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_reaction_for_a_team_discussion__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        Summary:
        Create reaction for a team discussion (Legacy)
        Docs:
        https://docs.github.com/rest/reference/reactions/#create-reaction-for-a-team-discussion-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/reactions"
        response = self._execute("post", url, params=params, payload=payload)
        return response
