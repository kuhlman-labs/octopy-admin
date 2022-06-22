#!/usr/bin/python3

from dotenv import dotenv_values
from org_repos_provider import OrgReposProvider, OrgReposProviderError
from repo_collaborators_provider import RepoCollaboratorsProvider, RepoCollaboratorsProviderError

CONF = dotenv_values()
ORG_REPO_PROVIDER = OrgReposProvider(CONF)
REPO_COLLABORATOR_PROVIDER = RepoCollaboratorsProvider(CONF)

try:
    for REPO in ORG_REPO_PROVIDER.get_org_repos("Engineering"):
      print(REPO)
except OrgReposProviderError as ERR:
    print(ERR)

try:
    for COLLABORATOR in REPO_COLLABORATOR_PROVIDER.get_repo_collaborators("Engineering", "platform"):
      print(COLLABORATOR)
except RepoCollaboratorsProviderError as ERR:
    print(ERR)