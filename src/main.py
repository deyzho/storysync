import argparse
from src.core.story_processor import StoryProcessor
from src.core.repo_manager import RepoManager
from src.utils.config import load_config

def main():
    parser = argparse.ArgumentParser(description="StorySync: Story-driven development framework")
    parser.add_argument("--config", required=True, help="Path to config.yaml")
    parser.add_argument("--story", required=True, help="User story to process")
    args = parser.parse_args()

    try:
        config = load_config(args.config)
    except FileNotFoundError:
        print(f"Error: Config file {args.config} not found.")
        exit(1)
    except Exception as e:
        print(f"Error loading config: {e}")
        exit(1)

    repo_manager = RepoManager(config)
    llm_plugin = None  # Placeholder for LLM plugin
    processor = StoryProcessor(llm_plugin, repo_manager)
    result = processor.process(args.story)
    print(result)

if __name__ == "__main__":
    main()