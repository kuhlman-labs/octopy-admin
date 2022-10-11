"""
This script creates an autolink reference for a repository.
"""
from dotenv import load_dotenv

from octopy_admin.rest_public.rest_public_client import (
    RestPublicClient,
    RestPublicClientError,
)

load_dotenv()
github = RestPublicClient()


def create_autolink_reference(owner, repo, payload):
    """
    Create an autolink reference for a repository.
    """
    try:
        reference = github.repos.create_an_autolink_reference_for_a_repository(
            owner=owner, repo=repo, payload=payload
        )
        return reference.json()
    except RestPublicClientError as e:
        print(e)


# example
# create_autolink_reference(owner='Engineering', repo='platform', payload={'key_prefix':'TICKET-','url_template':r'https://example.com/TICKET?query=<num>'})
