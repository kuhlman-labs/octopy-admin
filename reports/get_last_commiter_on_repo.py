"""
This script will get the last commiter information for a repo.
Input: CSV file with repo full names.
Output: CSV file with userid, last commit datetime, branch name.
"""

import csv

from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def get_last_commiter_on_repo(owner, repo):
    """
    Get the last commiter information for a repo.
    Input: owner, repo.
    Output: last commit json object.
    """
    try:
        response = github.repos.list_commits(owner=owner, repo=repo)
        response = response.json()
        last_commit = response[0]
        return last_commit
    except RestClientError as e:
        print(e)


# example

# last_commiter= get_last_commiter_on_repo('engineering', 'platform')
# print(last_commiter)
