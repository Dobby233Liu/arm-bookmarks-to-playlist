from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
from itertools import islice
import asyncio
import urllib.parse
import pickle
import os

def batched(iterable, n):
    iterator = iter(iterable)
    return iter(
        lambda: tuple(islice(iterator, n)),
        tuple()
    )

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json",
    scopes=["https://www.googleapis.com/auth/youtube"])

credentials = None
def actually_auth():
    global credentials
    credentials = flow.run_local_server(host="localhost",
        port=4000, 
        authorization_prompt_message="Please visit this URL: {url}", 
        success_message="The auth flow is complete; you may close this window.",
        open_browser=True)
    with open("auth.pickle", "wb") as p:
        pickle.dump(credentials, p)
if not os.path.exists("auth.pickle"):
    actually_auth()
else:
    with open("auth.pickle", "rb") as p:
        credentials = pickle.load(p)

yt = build('youtube', 'v3', credentials=credentials)

pl = "PLsNfuSXkz2wVixE8nfCilAtXe70tZrRX-"
startsfrom = "https://m.youtube.com/watch?v=SyX4rgXygwk"

async def main():
    with open("dump/-awesome random music-.json","r",encoding="utf-8") as f:
        l = json.load(f)
        if startsfrom:
            l = l[l.index(startsfrom):]
        for i in batched(l, 5):
            for j in i:
                print(j)
                jl = urllib.parse.urlparse(j)
                if not jl.hostname.endswith("youtube.com"):
                    print("not yt")
                    await asyncio.sleep(0.2)
                    continue
                jq = urllib.parse.parse_qs(jl.query)
                if not "v" in jq:
                    print("no vid")
                    await asyncio.sleep(0.2)
                    continue
                yt.playlistItems().insert(part="snippet", body={
                    "snippet": {
                        "playlistId": pl,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": jq["v"][0]
                        }
                    }
                }).execute()
                await asyncio.sleep(0.05)
            await asyncio.sleep(0.8)
asyncio.run(main())