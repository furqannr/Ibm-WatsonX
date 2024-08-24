from utils.git_utils import get_latest_commit_diff
from utils.model_utils import generate_commit_message

def create_commit_message(repo_path):
    diff = get_latest_commit_diff(repo_path)
    commit_message = generate_commit_message(diff)
    return commit_message
