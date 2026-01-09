class Orchestrator:
    def __init__(self, agents, memory):
        self.agents = agents
        self.memory = memory

    def get_agent(self, name):
        agent = self.agents.get(name)
        if not agent:
            raise ValueError(f"Agent '{name}' not found")
        return agent
    
    def run(self, user_input):
        input_data = {"topic": user_input}

        pipeline = [
            "difficulty_controller",
            "question_generator",
            "explanation",
            "responder"
        ]

        data = input_data

        for agent_name in pipeline:
            agent = self.get_agent(agent_name)
            result = agent.execute(data, self.memory)

            if isinstance(result, dict):
                data = result

        print(f"Question: {data.get('question')}")

        user_answer = input("Your answer: ")

        evaluator = self.get_agent("evaluation")
        evaluation = evaluator.execute(
            {"user_answer": user_answer},
            self.memory
        )

        if evaluation["is_correct"]:
            print("✔ Correct! Well done.")
        else:
            print("❌ Not quite. Let's try another one.")

        if not evaluation["is_correct"]:
            explanation = self.memory.get("explanation")
            if explanation: 
                print("\nExplanation")
                print(explanation)

        feedback_agent = self.get_agent("feedback")
        feedback_agent.execute(evaluation, self.memory)

        return evaluation
