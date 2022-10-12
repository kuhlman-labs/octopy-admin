"""
Interact with GitHub Issues.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Issues:
    """
    Interact with GitHub Issues.
    """

    def __init__(self, client):
        """
        Initializes the Issues class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_issues_assigned_to_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List issues assigned to the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-issues-assigned-to-the-authenticated-user
        """
        url = self._base_url + "/issues"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organization_issues_assigned_to_the_authenticated_user(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        List organization issues assigned to the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-organization-issues-assigned-to-the-authenticated-user
        """
        url = self._base_url + f"/orgs/{org}/issues"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_assignees(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List assignees
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-assignees
        """
        url = self._base_url + f"/repos/{owner}/{repo}/assignees"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_user_can_be_assigned(self, owner, repo, assignee, params=None, payload=None):
        """
        Summary:
        Check if a user can be assigned
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#check-if-a-user-can-be-assigned
        """
        url = self._base_url + f"/repos/{owner}/{repo}/assignees/{assignee}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_issues(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository issues
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-repository-issues
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_issue(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#create-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_issue_comments_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List issue comments for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-issue-comments-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_issue_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Summary:
        Get an issue comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#get-an-issue-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_issue_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Summary:
        Update an issue comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#update-an-issue-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_an_issue_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Summary:
        Delete an issue comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#delete-an-issue-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_issue_events_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List issue events for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-issue-events-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_issue_event(self, owner, repo, event_id, params=None, payload=None):
        """
        Summary:
        Get an issue event
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#get-an-issue-event
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/events/{event_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Get an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#get-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Update an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues/#update-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def add_assignees_to_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Add assignees to an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#add-assignees-to-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def remove_assignees_from_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Remove assignees from an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#remove-assignees-from-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_issue_comments(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        List issue comments
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-issue-comments
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_issue_comment(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Create an issue comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#create-an-issue-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_issue_events(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        List issue events
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-issue-events
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_labels_for_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        List labels for an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-labels-for-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_labels_to_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Add labels to an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#add-labels-to-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_labels_for_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Set labels for an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#set-labels-for-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_all_labels_from_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Remove all labels from an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#remove-all-labels-from-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def remove_a_label_from_an_issue(
        self, owner, repo, issue_number, name, params=None, payload=None
    ):
        """
        Summary:
        Remove a label from an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#remove-a-label-from-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def lock_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Lock an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#lock-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/lock"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unlock_an_issue(self, owner, repo, issue_number, params=None, payload=None):
        """
        Summary:
        Unlock an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#unlock-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/lock"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_timeline_events_for_an_issue(
        self, owner, repo, issue_number, params=None, payload=None
    ):
        """
        Summary:
        List timeline events for an issue
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-timeline-events-for-an-issue
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/timeline"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_labels_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List labels for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-labels-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_label(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a label
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#create-a-label
        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_label(self, owner, repo, name, params=None, payload=None):
        """
        Summary:
        Get a label
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#get-a-label
        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels/{name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_label(self, owner, repo, name, params=None, payload=None):
        """
        Summary:
        Update a label
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#update-a-label
        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels/{name}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_label(self, owner, repo, name, params=None, payload=None):
        """
        Summary:
        Delete a label
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#delete-a-label
        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels/{name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_milestones(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List milestones
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-milestones
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_milestone(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a milestone
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#create-a-milestone
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_milestone(self, owner, repo, milestone_number, params=None, payload=None):
        """
        Summary:
        Get a milestone
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#get-a-milestone
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_milestone(self, owner, repo, milestone_number, params=None, payload=None):
        """
        Summary:
        Update a milestone
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#update-a-milestone
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_milestone(self, owner, repo, milestone_number, params=None, payload=None):
        """
        Summary:
        Delete a milestone
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#delete-a-milestone
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_labels_for_issues_in_a_milestone(
        self, owner, repo, milestone_number, params=None, payload=None
    ):
        """
        Summary:
        List labels for issues in a milestone
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-labels-for-issues-in-a-milestone
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_user_account_issues_assigned_to_the_authenticated_user(
        self, params=None, payload=None
    ):
        """
        Summary:
        List user account issues assigned to the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/issues#list-user-account-issues-assigned-to-the-authenticated-user
        """
        url = self._base_url + "/user/issues"
        response = self._execute("get", url, params=params, payload=payload)
        return response
