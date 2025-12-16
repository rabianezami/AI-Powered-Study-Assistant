class memory:
    def __init__(self):
        self.store = {}

    def save(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key)