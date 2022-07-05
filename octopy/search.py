import asyncio
import csv

import aiohttp

URL_SLUG = ""
TOKEN = ""
url = "https://" + URL_SLUG + "/api/v3/search/code"
headers = {"Authorization": "Bearer " + TOKEN}
CSV_FILE = "test.csv"
REPO_LIST = []

with open(CSV_FILE, newline="") as CSVFILE:
    repos = csv.reader(CSVFILE, delimiter=" ", quotechar="|")
    for repo in repos:
        REPO_LIST.append(repo)


async def main():
    params = {"q": "filename:README filename:main.py repo:kuhlman-labs/test2", "per_page": "100"}
    for repo in REPO_LIST:
        params.update(q="filename:README filename:main.py repo:" + repo[0])
        print(params)

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:

                print("Status:", response.status)
                print("Content-type:", response.headers["content-type"])

                print(await response.text())


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(main())
