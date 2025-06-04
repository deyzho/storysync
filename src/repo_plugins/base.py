cat <<EOL > src/repo_plugins/base.py
class BaseRepoPlugin:
    def configure(self, config):
        raise NotImplementedError

    def clone(self, repo_url, local_path):
        raise NotImplementedError

    def create_pull_request(self, repo_path, branch_name, diff, test_script, commit_message):
        raise NotImplementedError
EOL