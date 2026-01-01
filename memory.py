class Memory:
    def __init__(self):
        self.store = {
            "correct_count": 0,
            "wrong_count": 0,
            "difficulty": "easy"
        }
      
    def save(self, key, value):
        self.store[key] = value

    def get(self, key, default=None):
        return self.store.get(key, default)
    
    def increment(self, key, amount=1):
        self.store[key] = self.store.get(key, 0) + amount
        return self.store[key]
    
    def reset(self, key):
        self.store[key] = 0