import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from octopyadmin.gql_provider import GitHubGqlProvider, GitHubGqlProviderError
from dotenv import load_dotenv

config = load_dotenv()
gql = GitHubGqlProvider()

try:
    org_results = gql.get_enterprise_orgs("GitHub")
    for organizations in org_results:
        total_count = organizations["enterprise"]["organizations"]["totalCount"]
        print(total_count)
        for org in organizations["enterprise"]["organizations"]["nodes"]:
            print(org["name"])

except GitHubGqlProviderError as err:
    print(err)
