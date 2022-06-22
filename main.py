#!/usr/bin/python3

from dotenv import dotenv_values
from org_repos_provider import OrgRepoProvider, OrgRepoProviderError
from repo_collaborators_provider import RepoCollaboratorProvider, RepoCollaboratorProviderError

CONF = dotenv_values()
ORG_REPO_PROVIDER = OrgRepoProvider(CONF)
REPO_COLLABORATOR_PROVIDER = RepoCollaboratorProvider(CONF)

try:
    for REPO in ORG_REPO_PROVIDER.get_org_repos("Engineering"):
      print(REPO["node"])
except OrgRepoProviderError as ERR:
    print(ERR)

try:
    for COLLABORATOR in REPO_COLLABORATOR_PROVIDER.get_repo_collaborators("Engineering", "platform"):
      print(COLLABORATOR)
except RepoCollaboratorProviderError as ERR:
    print(ERR)