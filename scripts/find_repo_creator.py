"""
This script will loop through the commits in a given repository and find the first commit of the user who created the repository.
"""

from dotenv import load_dotenv

from octopy_admin.rest_enterprise_server.rest_enterprise_server_client import (
    RestEnterpriseServerClient,
    RestEnterpriseServerClientError,
)

load_dotenv()

github = RestEnterpriseServerClient()


def get_repo_commits(owner, repo):
    """
    Get the commits for a given repository. Output is a list of dictionaries.
    """
    try:
        repo_commits_query = github.repos.list_commits(
            owner=owner, repo=repo, params={"page": "1", "per_page": "100"}
        )
        responses = github.paginate_request(repo_commits_query)
        commits = []
        for response in responses:
            for commit in response:
                commits.append(commit)
        return commits
    except RestEnterpriseServerClientError as e:
        print(e)


def get_first_commit_author(owner, repo):
    """
    Get the first commit of the repository and return commit author.
    """
    repo_commits = get_repo_commits(owner=owner, repo=repo)
    if repo_commits:
        first_commit = repo_commits[-1]
        commit_author = first_commit.get("commit").get("author").get("name")
        return commit_author


if __name__ == "__main__":
    # Example
    created_by = get_first_commit_author(owner="Engineering", repo="platform")
    print(created_by)
