#!/usr/bin/python3
"""
Use the  GitHub API, displays the GitHub identity based on given credentials.

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
