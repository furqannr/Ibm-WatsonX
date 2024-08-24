import git

def get_latest_commit_diff(repo_path):
    import git
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits('HEAD', max_count=2))
    if len(commits) < 2:
        return None
    diff = commits[0].diff(commits[1])
    return diff

def get_commit_messages(repo_path, count=10):
    repo = git.Repo(repo_path)
    return [commit.message for commit in repo.iter_commits('HEAD', max_count=count)]
