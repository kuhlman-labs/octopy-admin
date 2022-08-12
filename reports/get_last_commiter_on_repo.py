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
    Input: repo full name.
    Output: userid, last commit datetime, branch name.
    """
    try:
        response = github.repos.list_commits(owner=owner, repo=repo)
        response = response.json()
        return (
            response.get("author").get("login"),
            response.get("commit").get("author").get("date"),
            response.get("ref"),
        )
    except RestClientError as e:
        print(e)


def get_last_commiter_on_repo_list(repo_list):
    """
    Get the last commiter information for a repo.
    Input: repo full name.
    Output: userid, last commit datetime, branch name.
    """
    with open("last_commiter_on_repo.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["userid", "last_commit_datetime", "branch_name"])
        for repo in repo_list:
            userid, last_commit_datetime, branch_name = get_last_commiter_on_repo(
                repo.get("owner"), repo.get("name")
            )
            writer.writerow([userid, last_commit_datetime, branch_name])


def get_repo_list(file_name):
    """
    Get the repo list from a CSV file.
    Input: CSV file with repo full names.
    Output: list of repo full names.
    """
    repo_list = []
    with open(file_name, "r") as infile:
        reader = csv.reader(infile)
        for row in reader:
            repo_list.append(row)
    return repo_list
