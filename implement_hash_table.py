class HashTable(object):
    def __init__(self):
        self.array = [None] * 50

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

