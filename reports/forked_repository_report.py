"""
This module will generate a report on forked repositories in a GHES instance.
"""

import csv

from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient, GraphClientError
from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
restclient = RestClient()
graphclient = GraphClient()


def get_orgs(enterprise):
    """
    Get the list of orgs.
    """
    try:
        results = graphclient.query.get_enterprise_orgs(enterprise)
        org_list = graphclient.query.results_to_list(results)
        return org_list
    except GraphClientError as e:
        print(e)


def get_repos(org):
    """
    Get the list of repos.
    """
    try:
        results = graphclient.query.get_org_repos(org)
        repo_list = graphclient.query.results_to_list(results)
        return repo_list
    except GraphClientError as e:
        print(e)


def get_forked_repos(org, repo):
    """
    Get the list of forked repos in an org.
    """
    try:
        results = restclient.repos.list_forks(org, repo)
        forked_repo_list = results.json()
        return forked_repo_list
    except RestClientError as e:
        print(e)


def get_forked_repo_info(org, repo):
    """
    Get the list of forked repos in an org.
    """
    try:
        results = restclient.repos.get_a_repository(org, repo)
        forked_repo_info = results.json()
        return forked_repo_info
    except RestClientError as e:
        print(e)


def forked_repo_enterpsie_report(enterprise):
    """
    Generate a report on forked repos in an enterprise.
    """
    print(f"Generating forked repo report for {enterprise}...")
    print(f"Finding all orgs in {enterprise}...")
    orgs = get_orgs(enterprise)
    with open("forked_repo_report.csv", "w") as csvfile:
        fieldnames = [
            "source_repo",
            "forked_repo_full_name",
            "forked_repo_visibility",
            "fork_created_at",
            "fork_updated_at",
            "forked_repo_url",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for org in orgs:
            org_login = org["login"]
            print(f"Finding all repos in {org_login}...")
            repos = get_repos(org_login)
            if repos is None:
                continue
            for repo in repos:
                repo_name = repo["name"]
                repo_full_name = f"{org_login}/{repo_name}"
                print(f"Finding all forked repos for {repo_full_name}...")
                forked_repos = get_forked_repos(org_login, repo_name)
                print(f"Found {len(forked_repos)} forked repos for {repo_full_name}...")
                if forked_repos == []:
                    print(f"No forked repos found for {repo_full_name}...")
                    continue
                for forked_repo in forked_repos:
                    forked_repo_full_name = forked_repo["full_name"]
                    forked_repo_visibility = forked_repo["visibility"]
                    fork_created_at = forked_repo["created_at"]
                    fork_updated_at = forked_repo["updated_at"]
                    print(f"Writing info for {forked_repo_full_name}...")
                    writer.writerow(
                        {
                            "source_repo": repo_full_name,
                            "forked_repo_full_name": forked_repo_full_name,
                            "forked_repo_visibility": forked_repo_visibility,
                            "fork_created_at": fork_created_at,
                            "fork_updated_at": fork_updated_at,
                            "forked_repo_url": forked_repo["html_url"],
                        }
                    )


def forked_repo_org_report(org):
    """
    Generate a report on forked repos in an org.
    """
    print(f"Generating forked repo report for {org}...")
    print(f"Finding all repos in {org}...")
    repos = get_repos(org)
    if repos is None:
        return
    with open("forked_repo_report.csv", "w") as csvfile:
        fieldnames = [
            "source_repo",
            "forked_repo_full_name",
            "forked_repo_visibility",
            "fork_created_at",
            "fork_updated_at",
            "forked_repo_url",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in repos:
            repo_name = repo["name"]
            repo_full_name = f"{org}/{repo_name}"
            print(f"Finding all forked repos for {repo_full_name}...")
            forked_repos = get_forked_repos(org, repo_name)
            print(f"Found {len(forked_repos)} forked repos for {repo_full_name}...")
            if forked_repos == []:
                print(f"No forked repos found for {repo_full_name}...")
                continue
            for forked_repo in forked_repos:
                forked_repo_full_name = forked_repo["full_name"]
                forked_repo_visibility = forked_repo["visibility"]
                fork_created_at = forked_repo["created_at"]
                fork_updated_at = forked_repo["updated_at"]
                print(f"Writing info for {forked_repo_full_name}...")
                writer.writerow(
                    {
                        "source_repo": repo_full_name,
                        "forked_repo_full_name": forked_repo_full_name,
                        "forked_repo_visibility": forked_repo_visibility,
                        "fork_created_at": fork_created_at,
                        "fork_updated_at": fork_updated_at,
                        "forked_repo_url": forked_repo["html_url"],
                    }
                )


# examples

# run this to generate a report on all forked repos in an enterprise
# forked_repo_report('enterprise_slug')

# run this to generate a report on all forked repos in an org
# forked_repo_report('org_login')
