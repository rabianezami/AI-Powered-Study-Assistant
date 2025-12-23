class BaseAgent:
    def __init__(self, name, allowed_actions=None):
        self.name = name
        self.allowed_actions = allowed_actions or []

    def execute(self, input_data, memory):
        # main function agent runs
        raise NotImplementedError
    
class AnalyzerAgent(BaseAgent):
    pass 

class WorkerAgent(BaseAgent):
    pass 

class ResponseAgent(BaseAgent):
    pass 