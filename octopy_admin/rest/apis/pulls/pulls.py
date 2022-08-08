"""
Interact with GitHub Pull Requests.
"""


# pylint: disable=too-many-arguments
class Pulls:
    # pylint: disable=too-many-public-methods
    """
    Interact with GitHub Pull Requests.
    """

    def __init__(self, client):
        """
        Initialize the Pulls class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_pull_requests(self, owner, repo, params=None, payload=None):
        """
        List pull requests
        https://docs.github.com/rest/reference/pulls#list-pull-requests
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        state
         head
         base
         sort
         direction
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_pull_request(self, owner, repo, params=None, payload=None):
        """
        Create a pull request
        https://docs.github.com/rest/reference/pulls#create-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_review_comments_in_a_repository(self, owner, repo, params=None, payload=None):
        """
        List review comments in a repository
        https://docs.github.com/rest/reference/pulls#list-review-comments-in-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        sort
         direction
         since
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_review_comment_for_a_pull_request(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Get a review comment for a pull request
        https://docs.github.com/rest/reference/pulls#get-a-review-comment-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_review_comment_for_a_pull_request(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Update a review comment for a pull request
        https://docs.github.com/rest/reference/pulls#update-a-review-comment-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_review_comment_for_a_pull_request(
        self, owner, repo, comment_id, params=None, payload=None
    ):
        """
        Delete a review comment for a pull request
        https://docs.github.com/rest/reference/pulls#delete-a-review-comment-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Get a pull request
        https://docs.github.com/rest/reference/pulls#get-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Update a pull request
        https://docs.github.com/rest/reference/pulls/#update-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_review_comments_on_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        List review comments on a pull request
        https://docs.github.com/rest/reference/pulls#list-review-comments-on-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:
        sort
         direction
         since
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_review_comment_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Create a review comment for a pull request
        https://docs.github.com/rest/reference/pulls#create-a-review-comment-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_reply_for_a_review_comment(
        self, owner, repo, pull_number, comment_id, params=None, payload=None
    ):
        """
        Create a reply for a review comment
        https://docs.github.com/rest/reference/pulls#create-a-reply-for-a-review-comment
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        comment_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_commits_on_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        List commits on a pull request
        https://docs.github.com/rest/reference/pulls#list-commits-on-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_pull_requests_files(self, owner, repo, pull_number, params=None, payload=None):
        """
        List pull requests files
        https://docs.github.com/rest/reference/pulls#list-pull-requests-files
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/files"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_pull_request_has_been_merged(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Check if a pull request has been merged
        https://docs.github.com/rest/reference/pulls#check-if-a-pull-request-has-been-merged
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/merge"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def merge_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        Merge a pull request
        https://docs.github.com/rest/reference/pulls#merge-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/merge"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_requested_reviewers_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        List requested reviewers for a pull request
        https://docs.github.com/rest/reference/pulls#list-requested-reviewers-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def request_reviewers_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Request reviewers for a pull request
        https://docs.github.com/rest/reference/pulls#request-reviewers-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def remove_requested_reviewers_from_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Remove requested reviewers from a pull request
        https://docs.github.com/rest/reference/pulls#remove-requested-reviewers-from-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_reviews_for_a_pull_request(self, owner, repo, pull_number, params=None, payload=None):
        """
        List reviews for a pull request
        https://docs.github.com/rest/reference/pulls#list-reviews-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_review_for_a_pull_request(
        self, owner, repo, pull_number, params=None, payload=None
    ):
        """
        Create a review for a pull request
        https://docs.github.com/rest/reference/pulls#create-a-review-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Get a review for a pull request
        https://docs.github.com/rest/reference/pulls#get-a-review-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        review_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Update a review for a pull request
        https://docs.github.com/rest/reference/pulls#update-a-review-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        review_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_pending_review_for_a_pull_request(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        Delete a pending review for a pull request
        https://docs.github.com/rest/reference/pulls#delete-a-pending-review-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        review_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_comments_for_a_pull_request_review(
        self, owner, repo, pull_number, review_id, params=None, payload=None
    ):
        """
        List comments for a pull request review
        https://docs.github.com/rest/reference/pulls#list-comments-for-a-pull-request-review
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        review_id
        Payload Parameters:
        per-page
         page
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
        Dismiss a review for a pull request
        https://docs.github.com/rest/reference/pulls#dismiss-a-review-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        review_id
        Payload Parameters:

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
        Submit a review for a pull request
        https://docs.github.com/rest/reference/pulls#submit-a-review-for-a-pull-request
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        review_id
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_comments_in_a_pull_request_thread(
        self, owner, repo, pull_number, thread_id, params=None, payload=None
    ):
        """
        List comments in a pull request thread
        https://docs.github.com/rest/reference/pulls#list-thread-comments-in-a-thread
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        thread_id
        Payload Parameters:
        per-page
         page
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_pull_request_thread_comment(
        self, owner, repo, pull_number, thread_id, params=None, payload=None
    ):
        """
        Create a pull request thread comment
        https://docs.github.com/rest/reference/pulls#create-a-thread-comment
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        thread_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_pull_request_thread_comment(
        self, owner, repo, pull_number, thread_id, comment_id, params=None, payload=None
    ):

        """
        Get a pull request thread comment
        https://docs.github.com/rest/reference/pulls#get-a-thread-comment
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
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments/{comment_id}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_pull_request_thread_comment(
        self, owner, repo, pull_number, thread_id, comment_id, params=None, payload=None
    ):

        """
        Update a pull request thread comment
        https://docs.github.com/rest/reference/pulls#update-a-thread-comment
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
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments/{comment_id}"
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_pull_request_thread_comment(
        self, owner, repo, pull_number, thread_id, comment_id, params=None, payload=None
    ):

        """
        Delete a pull request thread comment
        https://docs.github.com/rest/reference/pulls#delete-a-thread-comment
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
            + f"/repos/{owner}/{repo}/pulls/{pull_number}/threads/{thread_id}/comments/{comment_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def update_a_pull_request_branch(self, owner, repo, pull_number, params=None, payload=None):
        """
        Update a pull request branch
        https://docs.github.com/rest/reference/pulls#update-a-pull-request-branch
        Attributes:
        Path Parameters:
        owner
        repo
        pull_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch"
        response = self._execute("put", url, params=params, payload=payload)
        return response
