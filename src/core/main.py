cat <<EOL > src/main.py
import argparse
from src.core.story_processor import StoryProcessor
from src.core.repo_manager import RepoManager
from src.utils.config import load_config

def main():
    parser = argparse.ArgumentParser(description="StorySync: Story-driven development framework")
    parser.add_argument("--config", required=True, help="Path to config.yaml")
    parser.add_argument("--story", required=True, help="User story to process")
    args = parser.parse_args()

    config = load_config(args.config)
    repo_manager = RepoManager(config)
    llm_plugin = None  # Placeholder for LLM plugin
    processor = StoryProcessor(llm_plugin, repo_manager)
    result = processor.process(args.story)
    print(result)

if __name__ == "__main__":
    main()
EOL