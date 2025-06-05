import yaml
import os

def load_config(path):
    with open(path, 'r') as f:
        config = yaml.safe_load(f)

    # Override with environment variables
    config["llm"]["config"]["api_key"] = os.getenv("LLM_API_KEY", config["llm"]["config"].get("api_key"))
    config["repo"]["config"]["token"] = os.getenv("REPO_TOKEN", config["repo"]["config"].get("token"))
    config["repo"]["config"]["url"] = os.getenv("REPO_URL", config["repo"]["config"].get("url"))
    if config.get("issue_tracker"):
        config["issue_tracker"]["config"]["base_url"] = os.getenv("JIRA_BASE_URL", config["issue_tracker"]["config"].get("base_url"))
        config["issue_tracker"]["config"]["api_token"] = os.getenv("JIRA_API_TOKEN", config["issue_tracker"]["config"].get("api_token"))
        config["issue_tracker"]["config"]["email"] = os.getenv("JIRA_EMAIL", config["issue_tracker"]["config"].get("email"))
        config["issue_tracker"]["config"]["project_key"] = os.getenv("JIRA_PROJECT_KEY", config["issue_tracker"]["config"].get("project_key"))

    return config