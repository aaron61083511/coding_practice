class Node(object):
    def __init__(self, key, node):
        self.key = key
        self.node = node
        self.next = None
        self.prev = None

class HashTable(object):
    def __init__(self):
        self.array = [None] * 50
        self.head = None
        self.tail = None

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        index = self.hash(key)
        node = self.array[index]
        new = Node(key, value)
        if node is None:
            self.array[index] = new




