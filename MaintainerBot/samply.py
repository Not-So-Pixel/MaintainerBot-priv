# import requests

# url = "https://api.github.com/repos/PixelOS-Releases/releases/actions/workflows/17046064/dispatches"

# token = "token actualtoken"

# # https://api.github.com/repos/OWNER/REPO/actions/workflows

# DataStuff = {
#     'Accept': 'application/vnd.github.v3+json',
#     "Authorization" : token,
# }

# a = requests.get(url, headers=DataStuff)

# print(a.content)

import os

commands = [
#     "curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg",
# "echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null",
# "sudo apt update",
# "sudo apt install gh",
    "cd releases && echo $(pwd) && gh workflow run mojito-s.yml"
]

for command in commands:
    os.system(command)