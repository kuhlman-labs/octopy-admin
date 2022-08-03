from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient

load_dotenv()


class TestGraphClient:

    graph_client = GraphClient()

    def test_get_the_authenticated_user(self):
        response = self.graph_client.query.get_the_authenticated_user()
        assert response.get("viewer").get("login") is not None

    def test_get_enterprise_orgs(self):
        responses = self.graph_client.query.get_enterprise_orgs("github")
        for response in responses:
            assert response.get("enterprise").get("organizations") is not None
