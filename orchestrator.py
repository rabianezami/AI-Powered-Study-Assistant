from agents import BaseAgent
from memory import memory
from permissions import permissionSystm

class orchestrator:
    def __init__(self):
        self.memory = memory()
        self.permissions = permissionSystm()
        self.agents = {}

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.name] = agent

    def route(self, user_input: str):
        # decide which agent should hande the request
        pass