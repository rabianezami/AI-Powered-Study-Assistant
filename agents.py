import random

class BaseAgent:
    def __init__(self, name, allowed_actions=None):
        self.name = name
        self.allowed_actions = allowed_actions or []

    def execute(self, input_data, memory):
       
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
        
class DifficultyControllerAgent(BaseAgent):
    def __init__(self):
        super().__init__("difficulty_controller")

    def execute(self, input_data, memory):
        difficulty = memory.get("difficulty", "easy")
        input_data["difficulty"] = difficulty
        return input_data

class QuestionGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("question_generator")

    def execute(self, input_data, memory):
        topic = input_data.get("topic", "python")
        difficulty = input_data.get("difficulty", "easy")

        questions = {
            "python": {
                "easy": [
                    ("What is python", "Python is a programming language."),
                    ("Who created Python?", "Python was created by Guido van Rossum."),
                    ("Is Python interpreted?", "Yes, Python is an interpreted language.")
                ],
                "medium": [
                    ("What is a list in python?", "A list is a collection of items."),
                    ("Difference between list and tuple?", "Lists are mutable, tuples are immutable."),
                    ("What is a dictionary?", "A dictionary stores key-value pairs.")
                ],
                "hard": [
                    ("Explain list comperhension", "A concise way to creat lists."),
                     ("What is a generator?", "A function that yields values one at a time."),
                    ("Explain decorators", "Functions that modify other functions.")
                ]
            }
        }

        all_questions = questions.get(topic, questions["python"])[difficulty]

        asked_questions = memory.get("asked_questions", {})
        topic_asked = asked_questions.setdefault(topic, {})
        asked_for_difficulty = topic_asked.setdefault(difficulty, [])

        available = [
            qa for qa in all_questions
            if qa[0] not in asked_for_difficulty
        ]

        if not available: 
            asked_for_difficulty.clear()
            available = all_questions

        question, answer = random.choice(available)

        asked_for_difficulty.append(question)
        memory.save("asked_questions", asked_questions)

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
        else:
            explanation = (
            f"{answer}\n\n"
            f"Example:\n"
            f"Python is often used for automating tasks, processing data, building web apps, and writing scripts."
        )

        memory.save("explanation", explanation)
        input_data["explanation"] = explanation
        return input_data
    

class FeedbackAgent(BaseAgent):
    def __init__(self):
        super().__init__("feedback")

    def execute(self, input_data, memory):
      """
      input_data: 
      {
          "is_correct": True | False
      }
      """

      is_correct = input_data.get("is_correct")

      if is_correct is None:
          return input_data
      
      if is_correct:
          memory.increment("correct_count")
          memory.reset("wrong_count")
          memory.save("last_feedback", "correct")
      else:
          memory.increment("wrong_count")
          memory.reset("correct_count")
          memory.save("last_feedback", "wrong")

      if memory.get("correct_count") >= 3:
           memory.save("difficulty", "hard")

      elif memory.get("wrong_count") >= 2:
          memory.save("difficulty", "easy")
   
      return input_data
    
class ResponseAgent(BaseAgent):
    def execute(self, input_data, memory):
        question = input_data.get("question")
        explanation = input_data.get("explanation")

        return (
            f"Generated Question:\n{question}\n\n"
            f"Explanation:\n{explanation}"
        )
    
class EvaluationAgent(BaseAgent):
    def __init__(self):
        super().__init__("evaluation")
        
    def execute(self, input_data, memory):
        user_answer = input_data.get("user_answer", "").lower().strip()
        correct_answer = memory.get("answer", "").lower().strip()

        if not user_answer or not correct_answer:
            return {"is_correct": False}
        
        is_correct = user_answer in correct_answer or correct_answer in user_answer

        memory.save("last_result", is_correct)

        return {"is_correct": is_correct}