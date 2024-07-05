#!/usr/bin/python3
"""Using  GitHub API, it will display a GitHub identity that is based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - it will use Basic Authentication processes in accessing theidentity - ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

def get_github_user_id(username, password):
    auth = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)
    return response.json().get("id")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    user_id = get_github_user_id(username, password)
    print(user_id)
