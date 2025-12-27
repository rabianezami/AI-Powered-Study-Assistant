import random

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
    pass 

class QuestionGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("question_generator")

    def execute(self, input_data, memory):
        topic = input_data.get("topic")
        difficulty = input_data.get("difficulty", "easy")

        questions = {
            "python": {
                "easy": [
                    ("What is python", "Python is a programming language.")
                ],
                "medium": [
                    ("What is a list in python?", "A list is a collection of items.")
                ],
                "hard": [
                    ("Explain list comperhension", "A concise way to creat lists.")
                ]
            }
        }

        topic_data = questions.get(topic, questions["python"])
        question, answer = random.choice(topic_data[difficulty])

        memory.save("question", question)
        memory.save("answer", answer)

        return {
            "question": question,
            "answer": answer,
            "difficulty": difficulty
        }
