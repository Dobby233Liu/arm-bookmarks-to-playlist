from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import code

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json",
    scopes=["https://www.googleapis.com/auth/youtube"])

credentials = flow.run_local_server(host="localhost",
    port=4000, 
    authorization_prompt_message="Please visit this URL: {url}", 
    success_message="The auth flow is complete; you may close this window.",
    open_browser=True)

yt = build('youtube', 'v3', credentials=credentials)

code.interact(local=locals())
#yt.playlists().list(part="id,snippet", mine=True).execute()