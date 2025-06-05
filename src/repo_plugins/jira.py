import json
import os
from jira import JIRA
from .base import BaseRepoPlugin

class JiraPlugin(BaseRepoPlugin):
    def __init__(self):
        self.client = None
        self.project_key = None
        self.cache_file = "jira_cache.json"
        self.cache = self.load_cache()

    def load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        return {}

    def save_cache(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f)

    def configure(self, config):
        self.base_url = config.get("base_url")
        self.api_token = config.get("api_token")
        self.email = config.get("email")
        self.project_key = config.get("project_key")
        if not all([self.base_url, self.api_token, self.email, self.project_key]):
            raise ValueError("Jira base_url, api_token, email, project_key required")
        self.client = JIRA(server=self.base_url, basic_auth=(self.email, self.api_token))

    def create_issue(self, story, requirements=None):
        if not requirements:
            requirements = []
        issue_key = f"{self.project_key}-{hash(story) % 1000}"  # Mock key for demo
        if issue_key in self.cache:
            return self.cache[issue_key]
        issue_dict = {
            'project': {'key': self.project_key},
            'summary': story,
            'description': '\n'.join(requirements) if requirements else '',
            'issuetype': {'name': 'Story'}
        }
        issue = self.client.create_issue(fields=issue_dict)
        self.cache[issue.key] = {"permalink": issue.permalink(), "status": issue.fields.status.name}
        self.save_cache()
        return self.cache[issue.key]

    def get_status(self, issue_key):
        if issue_key in self.cache:
            return self.cache[issue_key]["status"]
        issue = self.client.issue(issue_key)
        status = issue.fields.status.name
        self.cache[issue_key] = {"permalink": issue.permalink(), "status": status}
        self.save_cache()
        return status

    def create_pull_request(self, repo_path, branch_name, diff, test_script, commit_message):
        issue = self.create_issue(commit_message, [f"Diff:\n```diff\n{diff}\n```", f"Tests:\n```python\n{test_script}\n```"])
        return issue["permalink"]