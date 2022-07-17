import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from dotenv import dotenv_values, load_dotenv

from octopy.rest.rest_patch import RestPatch

load_dotenv()
ghes = dotenv_values(".env.ghes")

restpatch = RestPatch()


def test_update_repo_webhook_config():
    response = restpatch.update_repo_webhook_config(
        owner="Outer-Planets-Alliance",
        repo="test",
        hook_id="368519137",
        config={"url": "https://example.com/webhook"},
    )
    assert response.status_code == 200


def test_update_org_webhook_config():
    response = restpatch.update_org_webhook_config(
        owner="Outer-Planets-Alliance",
        hook_id="340083281",
        config={"url": "https://example.com/webhook"},
    )
    assert response.status_code == 200
