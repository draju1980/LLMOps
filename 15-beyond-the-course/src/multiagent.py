"""Module 15: Multi-Agent Orchestration"""
class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    async def execute(self, task):
        return f"{self.name} ({self.role}) completed: {task}"
