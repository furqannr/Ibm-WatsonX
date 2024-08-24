import git

def get_latest_commit_diff(repo_path):
    repo = git.Repo(repo_path)
    diff = repo.git.diff('HEAD~1', 'HEAD')
    return diff

def get_commit_messages(repo_path, count=10):
    repo = git.Repo(repo_path)
    return [commit.message for commit in repo.iter_commits('HEAD', max_count=count)]
