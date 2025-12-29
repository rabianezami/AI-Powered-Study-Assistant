from orchestrator import Orchestrator 
from agents import AnalyzerAgent, WorkerAgent, ResponseAgent, SafetyAgent, QuestionGeneratorAgent, ExplanationAgent

orc = Orchestrator()

# real actions add in phase 2
orc.register_agent(SafetyAgent())
orc.register_agent(QuestionGeneratorAgent())
orc.register_agent(ExplanationAgent())
orc.register_agent(AnalyzerAgent("analyzer"))
orc.register_agent(WorkerAgent("worker"))
orc.register_agent(ResponseAgent("responder"))

# start 
user_input = input("User: ")
orc.route(user_input)

