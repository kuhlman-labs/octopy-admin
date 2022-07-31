"""
This module contains scripts to generate reports on the branch
protection rules at the Enterprise, and Repository level.
"""
# pylint: disable=duplicate-code
import os
import sys

import pandas as pd
from dotenv import load_dotenv

from octopy_admin.graph.graph_query_converter import (
    GraphQueryConverter,
    GraphRequestError,
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

load_dotenv()
graphquery = GraphQueryConverter()


def enterpise_repo_branch_protection_report(enterprise):
    """
    This function generates a report on the branch protection rules at the
    Enterprise level.
    """
    data_frame = pd.DataFrame()
    try:
        print(f"Getting orgs for the {enterprise} enterprise.")
        orgs = graphquery.get_org_list(enterprise)
        print(f"Got {len(orgs)} orgs.")
        for org in orgs:
            print(f"Getting repos for the {org} organization.")
            repos = graphquery.get_repo_list(org)
            print(f"Got {len(repos)} repos.")
            for repo in repos:
                print(f"Getting branch protection rules for the {org}/{repo} repository.")
                rules = graphquery.get_repo_branch_protection_rule_list(org, repo)
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
    except GraphRequestError as err:
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
        rules = graphquery.get_repo_branch_protection_rule_list(org, repo)
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
    except GraphRequestError as err:
        print(err)
    return data_frame.to_csv("repo-branch-protection-report.csv")
