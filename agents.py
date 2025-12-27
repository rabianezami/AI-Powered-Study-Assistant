class BaseAgent:
    def __init__(self, name, allowed_actions=None):
        self.name = name
        self.allowed_actions = allowed_actions or []

    def execute(self, input_data, memory):
        # main function agent runs
        raise NotImplementedError
    
# Placeholder agents
class AnalyzerAgent(BaseAgent):
    def execute(self, input_data, memory):
        memory.save("last_input", input_data)
        return {"text": input_data}

class WorkerAgent(BaseAgent):
    def execute(self, input_data, memory):
        memory.save("processed", input_data)

class ResponseAgent(BaseAgent):
    def execute(self, input_data, memory):
        last = memory.get("last_input")
        return f"I received: {last}"