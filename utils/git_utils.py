# Add this to the top of git_utils.py
import inspect
print(inspect.getmembers(inspect.getmodule(inspect.currentframe()), inspect.isfunction))

import git

def get_commit_messages(repo_path, count=10):
    """
    Get the last 'count' commit messages from the specified repository.
    
    :param repo_path: Path to the Git repository.
    :param count: Number of commit messages to retrieve.
    :return: List of commit messages.
    """
    repo = git.Repo(repo_path)
    return [commit.message for commit in repo.iter_commits('HEAD', max_count=count)]
