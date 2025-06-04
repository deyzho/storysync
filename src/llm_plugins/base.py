cat <<EOL > src/llm_plugins/base.py
class BaseLLMPlugin:
    def generate(self, prompt):
        raise NotImplementedError
EOL