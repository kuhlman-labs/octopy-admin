"""
Interact with GitHub Pull Requests.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Pulls:
    """
    Interact with GitHub Pull Requests.
    """

    def __init__(self, client):
        """
        Initializes the Pulls class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_pull_requests(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List pull requests
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#list-pull-requests
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_pull_request(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#create-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_review_comments_in_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List review comments in a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#list-review-comments-in-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_review_comment_for_a_pull_request(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Summary:
        Get a review comment for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#get-a-review-comment-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_review_comment_for_a_pull_request(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Summary:
        Update a review comment for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#update-a-review-comment-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_review_comment_for_a_pull_request(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a review comment for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#delete-a-review-comment-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Summary:
        Get a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#get-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Summary:
        Update a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls/#update-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_review_comments_on_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        List review comments on a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#list-review-comments-on-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_review_comment_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        Create a review comment for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#create-a-review-comment-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_reply_for_a_review_comment(
        self, owner, repo, pull_number, comment_id, params=None, payload=None
    ):
        """
        Summary:
        Create a reply for a review comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#create-a-reply-for-a-review-comment
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_commits_on_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Summary:
        List commits on a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#list-commits-on-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_pull_requests_files(self, owner, repo, pull_number, params=None, payload=None):
        """
        Summary:
        List pull requests files
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#list-pull-requests-files
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/files"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_pull_request_has_been_merged(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        Check if a pull request has been merged
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#check-if-a-pull-request-has-been-merged
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/merge"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def merge_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Summary:
        Merge a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#merge-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/merge"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_all_requested_reviewers_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        Get all requested reviewers for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#get-all-requested-reviewers-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def request_reviewers_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        Request reviewers for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#request-reviewers-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def remove_requested_reviewers_from_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        Remove requested reviewers from a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#remove-requested-reviewers-from-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reviews_for_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Summary:
        List reviews for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#list-reviews-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_review_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Summary:
        Create a review for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#create-a-review-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Summary:
        Get a review for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#get-a-review-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Summary:
        Update a review for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#update-a-review-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_pending_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a pending review for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#delete-a-pending-review-for-a-pull-request
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_comments_for_a_pull_request_review(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Summary:
        List comments for a pull request review
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#list-comments-for-a-pull-request-review
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def dismiss_a_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Summary:
        Dismiss a review for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#dismiss-a-review-for-a-pull-request
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def submit_a_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Summary:
        Submit a review for a pull request
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#submit-a-review-for-a-pull-request
        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_a_pull_request_branch(self, owner, repo, pull_number, params=None, payload=None):
        """
        Summary:
        Update a pull request branch
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/pulls#update-a-pull-request-branch
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch"
        response = self._execute("put", url, params=params, payload=payload)
        return response
