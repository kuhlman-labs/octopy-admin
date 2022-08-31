"""
This script will create a given team in an given organization.
"""
from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def create_team_in_org(org, parameters):
    """
    Create a team in an organization.
    """
    try:
        team = github.teams.create_a_team(org=org, payload=parameters)
        return team.json()
    except RestClientError as e:
        print(e)


# example
# print(create_team_in_org(
#    org='Engineering',
#    parameters={
#    'name':'Engineering Team 2',
#    'description':'The team that engineers work for.',
#    'maintainers':['kuhlman-labs'],
#    'repo_names':['engineering/platform'],
#    'privacy':'closed'}
#    ))
