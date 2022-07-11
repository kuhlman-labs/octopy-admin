import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from octopy.graph_query import GraphQueryProvider, GraphQueryError
from dotenv import load_dotenv
import pandas as pd

config = load_dotenv()
gql = GraphQueryProvider()

def collaborator_permission_report(enterprise):
    print(f"Getting orgs for the {enterprise} enterprise.")
    orgs = gql.get_org_list(enterprise)
    print(f"Got {len(orgs)} orgs.")
    df = pd.DataFrame()
    try:
        for org in orgs:
            print(f"Getting repos for the {org} organization.")
            repos = gql.get_repo_list(org)
            print(f"Got {len(repos)} repos.")
            for repo in repos:
                print (f"Getting collaborators for the {org}/{repo} repository.")
                collaborators = gql.get_collaborators_permission_list(org, repo)
                print(f"Got {len(collaborators)} collaborators.")
                df = pd.concat([df, pd.DataFrame.from_records([{ 'org': org, 'repo': repo, 'collaborators':collaborators}])], ignore_index=True)
    except GraphQueryError as err:
        print(err)
    return df.to_csv("collaborator-permission-report.csv")

collaborator_permission_report("GitHub")