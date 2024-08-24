from utils.git_utils import get_commit_messages

repo_path = 'C:\\Users\\T580\\Desktop\\Aspire\\Ibm-WatsonsX\\'  # Update this path to a valid Git repository path
messages = get_commit_messages(repo_path)
print(messages)
