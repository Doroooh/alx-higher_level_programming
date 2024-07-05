#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests

def list_recent_commits(repo_name, repo_owner, num_commits=10):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)
    commits = response.json()

    for i in range(min(num_commits, len(commits))):
        sha = commits[i].get("sha")
        author = commits[i].get("commit").get("author").get("name")
        print(f"{sha}: {author}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <repository owner>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]
    list_recent_commits(repo_name, repo_owner)
