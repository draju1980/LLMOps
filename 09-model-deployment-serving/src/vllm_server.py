"""Module 09: vLLM Async Serving"""
class VLLMServer:
    def __init__(self, model_name, max_model_len=4096):
        self.model_name = model_name
        self.max_model_len = max_model_len

    async def generate(self, prompt, max_tokens=100):
        return {"generated_text": f"Response to: {prompt[:50]}..."}
