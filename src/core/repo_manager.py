cat <<EOL > src/core/repo_manager.py
class RepoManager:
    def __init__(self, config):
        self.code_plugin = None
        self.issue_plugin = None
EOL