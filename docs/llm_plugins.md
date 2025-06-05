# LLM Plugins

## Supported LLMs
- Grok 3
- OpenAI
- LLaMA
- Claude

## Adding a New LLM Plugin
1. Create `src/llm_plugins/my_llm.py`:
   ```python
   from .base import BaseLLMPlugin

   class MyLLMPlugin(BaseLLMPlugin):
       def __init__(self, api_key):
           self.api_key = api_key
       def generate(self, prompt):
           return {"text": "Response from MyLLM"}