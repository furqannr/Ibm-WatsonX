import requests

def generate_commit_message(diff):
    # Mock request to granite-20b-code-instruct (replace with real API call)
    response = requests.post("https://api.granite-ai.com/commit-message", json={"diff": diff})
    return response.json().get("commit_message", "No message generated")

def generate_summary(title, body, files_changed):
    # Mock request to granite-20b-code-instruct (replace with real API call)
    data = {
        "title": title,
        "body": body,
        "files_changed": files_changed
    }
    response = requests.post("https://api.granite-ai.com/summary", json=data)
    return response.json().get("summary", "No summary generated")
