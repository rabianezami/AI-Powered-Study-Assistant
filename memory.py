class Memory:
    def __init__(self):
        self.store = {
            "correct_count": 0,
            "wrong_count": 0
        }
      
    def save(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key, 0)