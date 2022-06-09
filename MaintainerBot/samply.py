import requests

url = "https://api.github.com/repos/PixelOS-Releases/releases/actions/workflows/17046064/dispatches"

token = "token actualtoken"

# https://api.github.com/repos/OWNER/REPO/actions/workflows

DataStuff = {
    'Accept': 'application/vnd.github.v3+json',
    "Authorization" : token,
}

a = requests.get(url, headers=DataStuff)

print(a.content)