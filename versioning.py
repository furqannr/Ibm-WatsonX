from utils.git_utils import get_commit_messages
from utils.model_utils import generate_version_suggestion

def determine_version_increment(commit_messages):
    return generate_version_suggestion(commit_messages)

def update_version(version_file_path, increment):
    with open(version_file_path, 'r') as file:
        version = file.read().strip()

    major, minor, patch = map(int, version.split('.'))

    if increment == 'major':
        major += 1
        minor = 0
        patch = 0
    elif increment == 'minor':
        minor += 1
        patch = 0
    else:
        patch += 1

    new_version = f"{major}.{minor}.{patch}"

    with open(version_file_path, 'w') as file:
        file.write(new_version)

    return new_version
