class Node:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

lru = LRUCache(2)
print(lru.head.next.value)