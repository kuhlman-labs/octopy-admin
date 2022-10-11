"""
This script runs a report on the enterprise environment to get the following information:
- number of orgs
- number of repos
- number of users
- number of BoC (Bytes of Code) by language per repo
- number of pull requests per month per repo
- number of commits per month per repo
- last use of a repo
- last use of a org
"""

import csv
from datetime import datetime, timedelta

from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient, GraphClientError
from octopy_admin.rest_public.rest_public_client import (
    RestPublicClient,
    RestPublicClientError,
)

load_dotenv()

github_graph = GraphClient()
github_rest = RestPublicClient()

time = datetime.now()
time_range = timedelta(days=30)

# Helper methods to generate report for enterprise


def get_orgs(enterprise):
    """
    Get the list of orgs.
    """
    try:
        results = github_graph.query.get_enterprise_orgs(enterprise)
        org_list = github_graph.query.results_to_list(results)
        return org_list
    except GraphClientError as e:
        print(e)


def get_enterprise_members(enterprise):
    """
    Get the list of members for an enterprise.
    """
    try:
        results = github_graph.query.get_enterprise_members(enterprise)
        member_list = github_graph.query.results_to_list(results)
        return member_list
    except GraphClientError as e:
        print(e)


def get_enterprise_admins(enterprise):
    """
    Get the list of admins for an enterprise.
    """
    try:
        results = github_graph.query.get_enterprise_admins(enterprise)
        admin_list = github_graph.query.results_to_list(results)
        return admin_list
    except GraphClientError as e:
        print(e)


def get_repos(org):
    """
    Get the list of repos.
    """
    try:
        results = github_graph.query.get_org_repos(org)
        repo_list = github_graph.query.results_to_list(results)
        return repo_list
    except GraphClientError as e:
        print(e)


def get_repo_prs(owner, name):
    """
    Get the list of pull requests for a repo.
    """
    try:
        results = github_graph.query.get_repo_prs(owner, name)
        pr_list = github_graph.query.results_to_list(results)
        return pr_list
    except GraphClientError as e:
        print(e)


def get_repo_languages(owner, name):
    """
    Get the list of languages for a repo.
    """
    try:
        results = github_graph.query.get_repo_languages(owner, name)
        language_list = github_graph.query.results_to_list(results)
        return language_list
    except RestPublicClientError as e:
        print(e)


def get_repo_commits_for_past_month(owner, name):
    """
    Get the list of commits for a repo.
    """
    try:
        results = github_rest.repos.list_commits(
            owner, name, params={"per_page": 100, "since": time - time_range}
        )
        return results.json()
    except RestPublicClientError as e:
        print(e)


# Generate Report that outputs to a CSV file


def generate_report(enterprise):
    """
    Generate a report for an enterprise.
    Input: enterprise name.
    Output: CSV file with report.
    """
    print(f"Generating report for the {enterprise} enterprise...")
    members = get_enterprise_members(enterprise)
    admins = get_enterprise_admins(enterprise)
    organizations = get_orgs(enterprise)
    print(
        f"Found {len(organizations)} organizations, {len(members)} members, and {len(admins)} admins in the {enterprise} enterprise."
    )
    report_time = datetime.now()
    report_time = time.isoformat("T", "seconds")
    with open(
        f"{report_time}-{enterprise}-enterprise-stats-report.csv", "w", newline=""
    ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Organizations", "Admins", "Members"])
        writer.writerow([len(organizations), len(admins), len(members)])
    for org in organizations:
        org_login = org.get("login")
        org_updated_at = org.get("updatedAt")
        org_repos = get_repos(org_login)
        print(f"Found {len(org_repos)} repos in the {org_login} organization.")
        with open(
            f"{report_time}-{enterprise}-enterprise-stats-report.csv", "a", newline=""
        ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Organization", "Repositories", "Last Updated"])
            writer.writerow([org_login, len(org_repos), org_updated_at])
        repo_rows = []
        for org_repo in org_repos:
            repo_name = org_repo.get("name")
            repo_updated_at = org_repo.get("updatedAt")
            repo_commits = get_repo_commits_for_past_month(org_login, repo_name)
            if not repo_commits:
                repo_commits = []
            pr_list = []
            repo_prs = get_repo_prs(org_login, repo_name)
            for pr in repo_prs:
                pr_created_at = datetime.strptime(pr.get("createdAt"), "%Y-%m-%dT%H:%M:%SZ")
                if pr_created_at > time - time_range:
                    pr_list.append(pr)
            print(
                f"Repo: {org_login}/{repo_name} has {len(repo_prs)} PRs and {len(repo_commits)} commits in the past month."
            )
            repo_languages = get_repo_languages(org_login, repo_name)
            languages = []
            for language in repo_languages:
                language_name = language.get("node").get("name")
                language_size = language.get("size")
                languages.append(f"{language_name}-({language_size})")
                print(f"Repo: {repo_name} - Language: {language_name} - Size: {language_size}")
            repo_rows.append(
                [repo_name, len(repo_commits), len(pr_list), languages, repo_updated_at]
            )
        with open(
            f"{report_time}-{enterprise}-enterprise-stats-report.csv", "a", newline=""
        ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Repository", "Commits", "PRs", "Languages", "Last Updated"])
            writer.writerows(repo_rows)


# Example

# generate_report("GitHub")
