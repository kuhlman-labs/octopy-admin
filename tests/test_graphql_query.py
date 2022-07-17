from dotenv import load_dotenv

from octopy.graph.graph_query import GraphQuery

load_dotenv()


def test_get_enterprise_orgs():
    graphquery = GraphQuery()
    responses = graphquery.get_enterprise_orgs("GitHub")
    for response in responses:
        assert response.get("enterprise") is not None
