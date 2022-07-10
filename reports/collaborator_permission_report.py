import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from octopyadmin.gql_provider import GitHubGQLProvider, GitHubGQLProviderError
from dotenv import load_dotenv
import pandas as pd

config = load_dotenv()
gql = GitHubGQLProvider()

def get_org_list(enterprise):
    org_list = list()
    try:
        org_results = gql.get_enterprise_orgs(enterprise)
        for organizations in org_results:
            for org in organizations["enterprise"]["organizations"]["nodes"]:
                org_list.append(org.get("name"))
    except GitHubGQLProviderError as err:
        print(err)
    return org_list

def get_repo_list(org):
    repo_list = list()
    try:
        repo_results = gql.get_org_repos(org)
        for repositories in repo_results:
            for repo in repositories["organization"]["repositories"]["edges"]:
                repo_list.append(repo.get("node").get("name"))
    except GitHubGQLProviderError as err:
        print(err)
    return repo_list

def get_collaborator_permission_list(org, repo):
    collaborator_list = list()
    try:
        collaborator_results = gql.get_repo_collaborators(org, repo)
        for collaborators in collaborator_results:
            for collaborator in collaborators["repository"]["collaborators"]["edges"]:
                collaborator_list.append([collaborator.get("node").get("login"), collaborator.get("permission")])
    except GitHubGQLProviderError as err:
        print(err)
    return collaborator_list
    

orgs = get_org_list("GitHub")
df = pd.DataFrame()
for org in orgs:
    repos = get_repo_list(org)
    for repo in repos:
        collaborators = get_collaborator_permission_list(org, repo)
        for collaborator in collaborators:
            df = pd.concat([df, pd.DataFrame.from_records([{ 'org': org, 'repo': repo, 'username':collaborator[0], 'permission': collaborator[1] }])], ignore_index=True)

df.to_csv("collaborator-permission-report.csv")