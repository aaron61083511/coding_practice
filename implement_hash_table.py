class HashTable(object):
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None] * self.capacity

