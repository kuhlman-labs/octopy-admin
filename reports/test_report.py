import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from octopy.graph_query import GraphQueryProvider, GraphQueryError
from dotenv import load_dotenv

config = load_dotenv()
gql = GraphQueryProvider()

organizations = gql._test_get_enterprise_orgs("GitHub")
print(organizations)