import os
from utils.git_utils import get_commit_messages

repo_path = 'C:/Users/T580/Desktop/Aspire/Ibm-WatsonX'  # Ensure this path is correct

# Debugging outputs
print("Testing Path:", repo_path)
print("Is Path Directory:", os.path.isdir(repo_path))
print("Is .git Directory:", os.path.isdir(os.path.join(repo_path, '.git')))

# Check if the path is valid and if it contains a .git directory
if os.path.isdir(repo_path) and os.path.isdir(os.path.join(repo_path, '.git')):
    print("Path is valid and is a Git repository.")
    try:
        messages = get_commit_messages(repo_path)
        print("Commit Messages:", messages)
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Path is invalid or not a Git repository.")

