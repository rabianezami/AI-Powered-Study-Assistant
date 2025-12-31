from orchestrator import Orchestrator 
from memory import Memory
from agents import (
    SafetyAgent,
    DifficultyControllerAgent,
    QuestionGeneratorAgent,
    ExplanationAgent,
    ResponseAgent
)

memory = Memory()

agents = {
    "safety": SafetyAgent(),
    "difficulty_generator": DifficultyControllerAgent(),
    "question_generator": QuestionGeneratorAgent(),
    "explanation": ExplanationAgent(),
    "responder": ResponseAgent("responder")
}

orc = Orchestrator(agents, memory)

# start 
user_input = input("User: ")
result = orc.run(user_input)

print(result)

