#!/usr/bin/python3

from dotenv import dotenv_values
from github_gql_constructor import GitHubGQLConstructor, GitHubGQLConstructorError
from github_gql_provider import GitHubGQLProvider, GitHubGQLProviderError
from github_rest_contructor import GitHubConstructorRestError, GitHubRestConstructor

conf = dotenv_values()
github_gql_provider = GitHubGQLProvider(conf)
github_gql_constructor = GitHubGQLConstructor(conf)
github_rest_constructor = GitHubRestConstructor(conf)

try:
    organizations = github_gql_provider.get_enterprise_orgs("GitHub")
    for organization in organizations:
        for org in organization["enterprise"]["organizations"]["nodes"]:
            print(org["name"])

except GitHubGQLProviderError as err:
    print(err)

try:
    github_gql_constructor.add_enterprise_org(
        {
            "adminLogins": ["kuhlman-labs"],
            "login": "testorg2",
            "profileName": "testorg2",
            "enterpriseId": "MDEwOkVudGVycHJpc2Ux",
            "billingEmail": "brett@kuhlman-labs.io",
        }
    )
    github_gql_constructor.add_repository(
        {
            "name": "testrepo1",
            "visibility": "PUBLIC",
        }
    )
except GitHubGQLConstructorError as err:
    print(err)

try:
    github_rest_constructor.create_user({"login": "testuser3", "email": "testuser3@kuhlman-labs.io"})
except GitHubConstructorRestError as err:
    print(err)
