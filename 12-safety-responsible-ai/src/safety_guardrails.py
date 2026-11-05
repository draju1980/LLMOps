"""Module 12: Safety Guardrails"""
class SafetyGuardrails:
    def check_prompt_injection(self, prompt):
        dangerous_patterns = ["__", "eval(", "exec(", "import "]
        return any(pattern in prompt for pattern in dangerous_patterns)

    def check_pii(self, text):
        import re
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        return bool(re.search(email_pattern, text))
