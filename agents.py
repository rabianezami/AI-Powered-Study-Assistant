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


class SafetyAgent(BaseAgent):
    def __init__(self):
        super().__init__("safety")

    def execute(self, input_data, memory):
        forbidden_topics = ["weapon", "harm", "violence", "drug", "kill"]

        topic = input_data.get("topic", "").lower()

        for bad in forbidden_topics:
            if bad in topic:
                return False
            
            return True

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


class ExplanationAgent(BaseAgent):
    def __init__(self):
        super().__init__("explanation")

    def execute(self, input_data, memory):
        answer = memory.get("answer")

        if not answer:
            return "No answer available to explain."
        
        explanation = (
            f"{answer}\n\n"
            f"Example:\n"
            f"Python is often used for automating tasks, processing data, building web apps, and writing scripts."
        )

        memory.save("explanation", explanation)
        return explanation
    
    
class ResponseAgent(BaseAgent):
    def execute(self, input_data, memory):
        question = input_data.get("question")
        explanation = input_data.get("explanation")

        return (
            f"Generated Question:\n{question}\n\n"
            f"Explanation:\n{explanation}"
        )
