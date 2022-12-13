class MemoryStore(object):
    def __init__(self):
        self.mem = {}

    def get(self, key):
        return self.mem[key]

    def set(self, key, value):
        self.mem[key] = value

    def exists(self, key):
        return key in self.mem