"""
This module contains scripts to generate reports on the branch
protection rules at the Enterprise, and Repository level.
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


def enterpise_repo_branch_protection_report(enterprise):
    """
    This function generates a report on the branch protection rules at the
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
                print(f"Getting branch protection rules for the {org}/{repo} repository.")
                rules_query = graphquery.query.get_repo_branch_protection_rules(org, repo)
                rules = graphquery.query.results_to_list(rules_query)
                print(f"Got {len(rules)} branch protection rules.")
                data_frame = pd.concat(
                    [
                        data_frame,
                        pd.DataFrame.from_records(
                            [{"org": org, "repo": repo, "rules": rules}],
                        ),
                    ],
                    ignore_index=True,
                )
    except GraphClientError as err:
        print(err)
    return data_frame.to_csv("enterprise-repo-branch-protection-report.csv")


def repo_branch_protection_report(org, repo):
    """
    This function generates a report on the branch protection rules at the
    Repository level.
    """
    data_frame = pd.DataFrame()
    try:
        print(f"Getting branch protection rules for the {org}/{repo} repository.")
        rule_query = graphquery.query.get_repo_branch_protection_rules(org, repo)
        rules = graphquery.query.results_to_list(rule_query)
        print(f"Got {len(rules)} branch protection rules.")
        data_frame = pd.concat(
            [
                data_frame,
                pd.DataFrame.from_records(
                    [{"org": org, "repo": repo, "rules": rules}],
                ),
            ],
            ignore_index=True,
        )
    except GraphClientError as err:
        print(err)
    return data_frame.to_csv("repo-branch-protection-report.csv")
