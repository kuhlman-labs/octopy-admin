"""
This module contains scripts to generate reports on the Collaborator
Permissions at the Enterprise, Organization, and Repository level.
"""
# pylint: disable=duplicate-code
import os
import sys

import pandas as pd
from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient, GraphClientError

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

load_dotenv()
graphquery = GraphClient()


def enterpise_collaborator_permission_report(enterprise):
    """
    This function generates a report on the Collaborator Permissions at the
    Enterprise level.
    """
    data_frame = pd.DataFrame()
    try:
        print(f"Getting orgs for the {enterprise} enterprise.")
        org_query = graphquery.query.get_enterprise_orgs(enterprise)
        orgs = graphquery.query.results_to_list(org_query)
        print(f"Got {len(orgs)} orgs.")
        for org in orgs:
            org = org.get("login")
            print(f"Getting repos for the {org} organization.")
            repo_query = graphquery.query.get_org_repos(org)
            repos = graphquery.query.results_to_list(repo_query)
            print(f"Got {len(repos)} repos.")
            for repo in repos:
                repo = repo.get("node").get("name")
                print(f"Getting collaborators for the {org}/{repo} repository.")
                collaborator_query = graphquery.query.get_repo_collaborators(org, repo)
                collaborators = graphquery.query.results_to_list(collaborator_query)
                print(f"Got {len(collaborators)} collaborators.")
                data_frame = pd.concat(
                    [
                        data_frame,
                        pd.DataFrame.from_records(
                            [{"org": org, "repo": repo, "collaborators": collaborators}]
                        ),
                    ],
                    ignore_index=True,
                )
    except GraphClientError as err:
        print(err)
    return data_frame.to_csv("enterprise-collaborator-permission-report.csv")


def org_collaborator_permission_report(org):
    """
    This function generates a report on the Collaborator Permissions at the
    Organization level.
    """
    data_frame = pd.DataFrame()
    try:
        print(f"Getting repos for the {org} organization.")
        repo_query = graphquery.query.get_org_repos(org)
        repos = graphquery.query.results_to_list(repo_query)
        print(f"Got {len(repos)} repos.")
        for repo in repos:
            repo = repo.get("node").get("name")
            print(f"Getting collaborators for the {org}/{repo} repository.")
            collaborator_query = graphquery.query.get_repo_collaborators(org, repo)
            collaborators = graphquery.query.results_to_list(collaborator_query)
            print(f"Got {len(collaborators)} collaborators.")
            data_frame = pd.concat(
                [
                    data_frame,
                    pd.DataFrame.from_records(
                        [{"org": org, "repo": repo, "collaborators": collaborators}]
                    ),
                ],
                ignore_index=True,
            )
    except GraphClientError as err:
        print(err)
    return data_frame.to_csv("org-collaborator-permission-report.csv")


def repo_collaborator_permission_report(org, repo):
    """
    This function generates a report on the Collaborator Permissions at the
    Repository level.
    """
    data_frame = pd.DataFrame()
    try:
        print(f"Getting collaborators for the {repo} repository.")
        collaborator_query = graphquery.query.get_repo_collaborators(org, repo)
        collaborators = graphquery.query.results_to_list(collaborator_query)
        print(f"Got {len(collaborators)} collaborators.")
        data_frame = pd.concat(
            [
                data_frame,
                pd.DataFrame.from_records([{"repo": repo, "collaborators": collaborators}]),
            ],
            ignore_index=False,
        )
    except GraphClientError as err:
        print(err)
    return data_frame.to_csv("repo-collaborator-permission-report.csv")
