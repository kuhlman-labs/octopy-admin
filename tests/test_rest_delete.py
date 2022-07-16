import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from dotenv import dotenv_values

from octopy.rest_delete import RestDelete

ghes = dotenv_values(".env.ghes")

restdelete = RestDelete(ghes.get("REST_API_URL"), ghes.get("API_TOKEN"))


def test_delete_user():
    response = restdelete.delete_user(username="testuser")
    assert response.status_code == 204
