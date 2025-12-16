from orchestrator import Orchestrator 
from agents import AnalyzerAgent, WorkerAgent, ResponseAgent

orc = Orchestrator()

# real actions add in phase 2
orc.register_agent(AnalyzerAgent("analyzer"))
orc.register_agent(WorkerAgent("worker"))
orc.register_agent(ResponseAgent("responder"))

# start 
user_input = input("User: ")
orc.route(user_input)

