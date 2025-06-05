import yaml
import os
from getpass import getpass

def run_setup():
    config = {
        "llm": {"type": "", "config": {"api_key": ""}},
        "repo": {"platform": "", "config": {"token": "", "url": ""}},
        "issue_tracker": {"platform": "", "config": {"base_url": "", "api_token": "", "email": "", "project_key": ""}}
    }

    print("Welcome to StorySync Setup Wizard!")
    llm_choice = input("Choose LLM (grok3/openai/llama/claude): ").lower()
    while llm_choice not in ["grok3", "openai", "llama", "claude"]:
        llm_choice = input("Invalid choice. Choose LLM (grok3/openai/llama/claude): ").lower()
    config["llm"]["type"] = llm_choice
    if llm_choice != "llama":
        config["llm"]["config"]["api_key"] = getpass(f"Enter {llm_choice} API key: ")

    repo_platform = input("Choose repo platform (github/gitlab/bitbucket): ").lower()
    while repo_platform not in ["github", "gitlab", "bitbucket"]:
        repo_platform = input("Invalid choice. Choose repo platform (github/gitlab/bitbucket): ").lower()
    config["repo"]["platform"] = repo_platform
    config["repo"]["config"]["token"] = getpass(f"Enter {repo_platform} token: ")
    config["repo"]["config"]["url"] = input(f"Enter {repo_platform} repository URL: ")

    use_jira = input("Configure Jira integration? (y/n): ").lower() == "y"
    if use_jira:
        config["issue_tracker"]["platform"] = "jira"
        config["issue_tracker"]["config"]["base_url"] = input("Enter Jira base URL (e.g., https://your-domain.atlassian.net): ")
        config["issue_tracker"]["config"]["api_token"] = getpass("Enter Jira API token: ")
        config["issue_tracker"]["config"]["email"] = input("Enter Jira email: ")
        config["issue_tracker"]["config"]["project_key"] = input("Enter Jira project key (e.g., PROJ): ")

    config_path = input("Save config to (default: config.yaml): ") or "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
    print(f"Configuration saved to {config_path}")

if __name__ == "__main__":
    run_setup()