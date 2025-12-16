class permissionSystem:
    def __init__(self):
        self.permissions = {}

    def set_permission(self, agent_name, actions):
        self.permissions[agent_name] = actions

    def check(self, agent_name, action):
        allowed = self.permissions.get(agent_name, [])
        return action in allowed