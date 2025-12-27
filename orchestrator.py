from agents import BaseAgent
from memory import Memory
from permissions import PermissionSystem

class Orchestrator:
    def __init__(self):
        self.memory = Memory()
        self.permissions = PermissionSystem()
        self.agents = {}

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.name] = agent

    def route(self, user_input: str):
        # decide which agent should hande the request
        analyzer = self.agents.get("analyzer")
        worker = self.agents.get("worker")
        responder = self.agents.get("responder")

        if not analyzer or not worker or not responder:
            print("Agents are not registered correctly.")
            return
        
        analysis = analyzer.execute(user_input, self.memory)
        worker.execute(analysis, self.memory)
        response = responder.execute(None, self.memory)

        print(response)