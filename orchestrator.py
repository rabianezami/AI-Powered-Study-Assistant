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
      
        print(response)