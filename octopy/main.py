#!/usr/bin/python3

from dotenv import dotenv_values
from github_gql_provider import GitHubGQLProvider, GitHubGQLProviderError
from github_gql_constructor import GitHubGQLConstructor, GitHubGQLConstructorError
from github_rest_contructor import GitHubRestConstructor, GitHubConstructorRestError

CONF = dotenv_values()
GITHUB_PROVIDER = GitHubGQLProvider(CONF)
GITHUB_CONSTRUCTOR = GitHubGQLConstructor(CONF)
GITHUB_REST_CONSTRUCTOR = GitHubRestConstructor(CONF)

try:
    for REPO in GITHUB_PROVIDER.get_org_repos("Engineering"):
        print(REPO)
    for COLLABORATOR in GITHUB_PROVIDER.get_repo_collaborators(
        "Engineering", "platform"
    ):
        print(COLLABORATOR)
    # for ORG in GITHUB_PROVIDER.get_enterprise_orgs("GitHub"):
    #    print(ORG)
    for ORG in GITHUB_PROVIDER.test_get_enterprise_orgs("GitHub"):
        print(ORG)
except GitHubGQLProviderError as ERR:
    print(ERR)

try:
    GITHUB_CONSTRUCTOR.add_enterprise_org(
        {
            "adminLogins": ["kuhlman-labs"],
            "login": "testorg2",
            "profileName": "testorg2",
            "enterpriseId": "MDEwOkVudGVycHJpc2Ux",
            "billingEmail": "brett@kuhlman-labs.io",
        }
    )
    GITHUB_CONSTRUCTOR.add_repository(
        {
            "name": "testrepo1",
            "visibility": "PUBLIC",
        }
    )
except GitHubGQLConstructorError as ERR:
    print(ERR)

try:
    GITHUB_REST_CONSTRUCTOR.create_user(
        {"login": "testuser3", "email": "testuser3@kuhlman-labs.io"}
    )
except GitHubConstructorRestError as ERR:
    print(ERR)
