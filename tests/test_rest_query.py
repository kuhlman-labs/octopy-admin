import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from octopy.rest_query import RestGetProvider, RestPatchProducer, RestPostProducer, RestDelete
from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env.ghes")

restquery = RestGetProvider()
restpatch = RestPatchProducer()
restpost = RestPostProducer(config.get("REST_API_URL"), config.get("API_TOKEN"))
restdelete = RestDelete(config.get("REST_API_URL"), config.get("API_TOKEN"))


def test_get_repo_list():
    response = restquery.get_repo_list("Outer-Planets-Alliance")
    assert response.status_code == 200

def test_get_repo():
    response = restquery.get_repo("kuhlman-labs", "kuhlman-labs")
    assert response.status_code == 200

def test_get_org():
    response = restquery.get_org("Outer-Planets-Alliance")
    assert response.status_code == 200

def test_get_user():
    response = restquery.get_user("kuhlman-labs")
    assert response.status_code == 200

def test_get_collaborators():
    response = restquery.get_collaborators("kuhlman-labs", "kuhlman-labs")
    assert response.status_code == 200

def test_get_collaborator_permission():
    response = restquery.get_collaborator_permission("kuhlman-labs", "kuhlman-labs", "kuhlman-labs")
    assert response.status_code == 200

def test_get_repo_webhook_list():
    response = restquery.get_repo_webhook_list("kuhlman-labs", "kuhlman-labs")
    assert  response.status_code == 200

def test_get_repo_webhook():
    response = restquery.get_repo_webhook("Outer-Planets-Alliance", "test", "368519137")
    assert response.status_code == 200

def test_get_org_webhooks():
    response = restquery.get_org_webhook_list("Outer-Planets-Alliance")
    assert response.status_code == 200

def test_get_org_webhook():
    response = restquery.get_org_webhook("Outer-Planets-Alliance", "340083281")
    assert response.status_code == 200

def test_update_repo_webhook_config():
    response = restpatch.update_repo_webhook_config(owner="Outer-Planets-Alliance", repo="test", hook_id="368519137", config={"url":"https://example.com/webhook"})
    assert response.status_code == 200

def test_update_org_webhook_config():
    response = restpatch.update_org_webhook_config(owner="Outer-Planets-Alliance", hook_id="340083281", config={"url":"https://example.com/webhook"})
    assert response.status_code == 200

def test_create_user():
    response = restpost.create_user(login="testuser", email="testuser@email.com")
    assert response.status_code == 201

def test_delete_user():
    response = restdelete.delete_user(username="testuser")
    assert response.status_code == 204