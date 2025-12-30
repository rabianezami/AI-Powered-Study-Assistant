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

        pipeline = {
            "difficulty_controller",
            "question_generator",
            "explanation",
            "responder"
        }

        data = input_data

        for agent_name in pipeline:
            agent = self.get_agent(agent_name)
            result = agent.execute(data, self.memory)

            if isinstance(result, dict):
                data = result
        return result