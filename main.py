#!/usr/bin/python3

from dotenv import dotenv_values
from github_provider import GitHubProvider, GitHubProviderError
from github_constructor import GitHubConstructor, GitHubConstructorError

CONF = dotenv_values()
GITHUB_PROVIDER = GitHubProvider(CONF)
GITHUB_CONSTRUCTOR = GitHubConstructor(CONF)

try:
    for REPO in GITHUB_PROVIDER.get_org_repos("Engineering"):
        print(REPO)
    for COLLABORATOR in GITHUB_PROVIDER.get_repo_collaborators(
        "Engineering", "platform"
    ):
        print(COLLABORATOR)
    for ORG in GITHUB_PROVIDER.get_enterprise_orgs("GitHub"):
        print(ORG)
except GitHubProviderError as ERR:
    print(ERR)

try:
    GITHUB_CONSTRUCTOR.add_enterprise_org(
        {
            "adminLogins": ["kuhlman-labs"],
            "login": "testorg1",
            "profileName": "testorg1",
            "enterpriseId": "MDEwOkVudGVycHJpc2Ux",
            "billingEmail": "brett@kuhlman-labs.io",
        }
    )
except GitHubConstructorError as ERR:
    print(ERR)
