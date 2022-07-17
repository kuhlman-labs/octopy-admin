import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import pandas as pd
from dotenv import load_dotenv

from octopy.graph.graph_query_converter import GraphQueryConverter, GraphRequestError

load_dotenv()
graphquery = GraphQueryConverter()


def enterpise_repo_branch_protection_report(enterprise):
    df = pd.DataFrame()
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
                df = pd.concat(
                    [
                        df,
                        pd.DataFrame.from_records(
                            [{"org": org, "repo": repo, "rules": rules}],
                        ),
                    ],
                    ignore_index=True,
                )
    except GraphRequestError as err:
        print(err)
    return df.to_csv("enterprise-repo-branch-protection-report.csv")


def repo_branch_protection_report(org, repo):
    df = pd.DataFrame()
    try:
        print(f"Getting branch protection rules for the {org}/{repo} repository.")
        rules = graphquery.get_repo_branch_protection_rule_list(org, repo)
        print(f"Got {len(rules)} branch protection rules.")
        df = pd.concat(
            [
                df,
                pd.DataFrame.from_records(
                    [{"org": org, "repo": repo, "rules": rules}],
                ),
            ],
            ignore_index=True,
        )
    except GraphRequestError as err:
        print(err)
    return df.to_csv("repo-branch-protection-report.csv")


enterpise_repo_branch_protection_report("github")
