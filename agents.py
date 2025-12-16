class BaseAgent:
    def __init__(self, name, allowed_actions=None):
        self.name = name
        self.allowed_actions = allowed_actions or []

    def execute(self, input_data, memory):
        # main function agent runs
        raise NotImplementedError
    
class AnalyzerAgent(BaseAgent):
    pass # logic in phase 2

class WorkerAgent(BaseAgent):
    pass # logic in phase 2

class ResponseAgent(BaseAgent):
    pass # logic in phase 2