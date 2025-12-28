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
        safety = self.agents.get("safety")
        generator = self.agents.get("question_generator")
        explainer = self.agents.get("explanation")
        responder = self.agents.get("responder")

        input_data = {
            "topic": user_input,
            "difficulty": "easy"
        }

        is_safe = safety.execute(input_data, self.memory)
  
        if not is_safe:
            print("❌ Topic is not allowed.")
            return

        result = generator.execute(input_data, self.memory)
        explanation = explainer.execute(result, self.memory)

        response = responder.execute({
            "question": result["question"],
            "explanation": explanation
        }, self.memory)

        print(response)