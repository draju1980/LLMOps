"""Module 11: Prompt Registry"""
class PromptRegistry:
    def __init__(self):
        self.prompts = {}

    def register(self, name, version, template):
        self.prompts[f"{name}:{version}"] = {"template": template, "hash": hash(template)}

    def get_prompt(self, name, version):
        return self.prompts.get(f"{name}:{version}")
