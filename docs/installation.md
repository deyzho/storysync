cat <<EOL > docs/installation.md
# Installation

## Prerequisites
- Python 3.10+
- Git

## Steps
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/your-org/storysync.git
   cd storysync
   \`
2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`
3. Configure \`examples/config.yaml\` with your API keys.

## Environment Variables
Override `config.yaml` with:
- `LLM_API_KEY`: LLM API key
- `REPO_TOKEN`: GitHub/GitLab/Bitbucket token
- `REPO_URL`: Repository URL
- `JIRA_BASE_URL`: Jira base URL
- `JIRA_API_TOKEN`: Jira API token
- `JIRA_EMAIL`: Jira email
- `JIRA_PROJECT_KEY`: Jira project key

Example:
```bash
export LLM_API_KEY=your_grok3_key
python -m src.main --config config.yaml --story "Test story"