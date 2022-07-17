import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from dotenv import dotenv_values

from octopy.rest.rest_post import RestPost

ghes = dotenv_values(".env.ghes")
restpost = RestPost(ghes.get("REST_API_URL"), ghes.get("API_TOKEN"))


def test_create_user():
    response = restpost.create_user(login="testuser", email="testuser@email.com")
    assert response.status_code == 201
