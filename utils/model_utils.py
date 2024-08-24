import requests

def generate_commit_message(diff):
    # Replace with your GenAI API request
    response = requests.post("https://api.genai.com/generate_commit_message", json={"diff": diff})
    return response.json().get("commit_message", "No message generated")

def generate_summary(title, body, files_changed):
    # Replace with your GenAI API request
    data = {
        "title": title,
        "body": body,
        "files_changed": files_changed
    }
    response = requests.post("https://api.genai.com/generate_summary", json=data)
    return response.json().get("summary", "No summary generated")

def generate_version_suggestion(commit_messages):
    # Replace with your GenAI API request
    response = requests.post("https://api.genai.com/generate_version_suggestion", json={"commit_messages": commit_messages})
    return response.json().get("suggested_version", "patch")
