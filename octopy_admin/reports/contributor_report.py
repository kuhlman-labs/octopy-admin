from dotenv import load_dotenv
import octopy_admin.gql_provider as gqlp
config = load_dotenv()
gql_provider = gqlp.GitHubGqlProvider()

try:
    org_results = gql_provider.get_enterprise_orgs("GitHub")
    for organizations in org_results:
        total_count = organizations["enterprise"]["organizations"]["totalCount"]
        print(total_count)
        for org in organizations["enterprise"]["organizations"]["nodes"]:
            print(org["name"])

except gqlp.GitHubGqlProviderError as err:
    print(err)
