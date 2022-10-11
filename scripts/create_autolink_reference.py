"""
This script creates an autolink reference for a repository.
"""
from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def create_autolink_reference(owner, repo, payload):
    """
    Create an autolink reference for a repository.
    """
    try:
        reference = github.repos.create_an_autolink_reference_for_a_repository(
            owner=owner, repo=repo, payload=payload
        )
        return reference.json()
    except RestClientError as e:
        print(e)


# example
# create_autolink_reference(owner='Engineering', repo='platform', payload={'key_prefix':'TICKET-','url_template':r'https://example.com/TICKET?query=<num>'})
