"""
This script will create a given team in an given organization.
"""
from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()

# Create a team in the organization
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

# Add a user to a team
def add_user_to_team(org, team_slug, username):
    """
    Add a user to a team.
    """
    try:
        user = github.teams.add_or_update_team_membership_for_a_user(
            org=org, team_slug=team_slug, username=username
        )
        return user.json()
    except RestClientError as e:
        print(e)


# example
# print(add_user_to_team(
#    org='Engineering',
#    team_slug='engineering-team-2',
#    username='brett'
#    ))
