import requests
from utils.model_utils import generate_summary

def fetch_pull_request_data(repo_owner, repo_name, pr_number, github_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(url, headers=headers)
    pr_data = response.json()
    return pr_data

def summarize_pull_request(pr_data):
    title = pr_data.get('title', '')
    body = pr_data.get('body', '')
    files_changed = [file['filename'] for file in pr_data.get('files', [])]
    summary = generate_summary(title, body, files_changed)
    return summary
