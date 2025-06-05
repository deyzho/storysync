cat <<EOL > README.md
# StorySync

StorySync is an open-source framework for automating story-driven development, analyzing code repositories, suggesting code changes, and generating tests for Python, Java, and JavaScript projects.

## Features
- Repository analysis with \`tree-sitter\` for Python, Java, JavaScript.
- Basic code and test generation using LLMs (Grok 3, OpenAI, LLaMA, Claude).
- Repository plugins: GitHub, GitLab, Bitbucket.
- Basic Jira integration (issue creation, status retrieval).
- MIT License.

## Documentation
- [Quickstart](docs/quickstart.md)
- [Usage](docs/usage.md)
- [LLM Plugins](docs/llm_plugins.md)
- [Repository Plugins](docs/repo_plugins.md)
- [Contributing](docs/contributing.md)

## Installation
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Quick Start
1. Configure in \`examples/config.yaml\`:
   \`\`\`yaml
   llm:
     type: llm
     config:
       api_key: your_api_key
   repo:
     platform: github
     config:
       token: your_github_token
       url: https://github.com/user/repo
   issue_tracker:
     platform: jira
     config:
       base_url: https://your-domain.atlassian.net
       api_token: your_jira_api_token
       email: your_email@example.com
       project_key: PROJ
   \`\`\`
2. Run StorySync:
   \`\`\`bash
   python -m src.main --config examples/config.yaml --story "As a user, I want to add a login endpoint"
   \`\`\`

## Contributing
See [CONTRIBUTING.md](docs/contributing.md).
