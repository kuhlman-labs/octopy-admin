import aiohttp
import asyncio
import csv

URL_SLUG = ""
TOKEN = ""
URL = "https://" + URL_SLUG + "/api/v3/search/code"
HEADERS={"Authorization": "Bearer " + TOKEN}
CSV_FILE = "test.csv"
REPO_LIST = []

with open(CSV_FILE, newline="") as CSVFILE:
    REPOS = csv.reader(CSVFILE, delimiter=" ", quotechar="|")
    for REPO in REPOS:
        REPO_LIST.append(REPO)

async def main():
    PARAMS = {"q":"filename:README filename:main.py repo:kuhlman-labs/test2","per_page":"100"}
    for REPO in REPO_LIST:
        PARAMS.update(q="filename:README filename:main.py repo:" + REPO[0])
        print(PARAMS)

        async with aiohttp.ClientSession() as session:
            async with session.get(URL, headers=HEADERS, params=PARAMS) as RESPONSE:

                print("Status:", RESPONSE.status)
                print("Content-type:", RESPONSE.headers['content-type'])

                print(await RESPONSE.text())
            

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(main())