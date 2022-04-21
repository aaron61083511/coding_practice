class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoTail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoTail(node)
            node.value = value         # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromHead()
            node = ListNode(key,value)
            self.dic[key] = node
            self.insertIntoTail(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoTail(self, node):
        tailprev = self.tail.prev
        tailprev.next = node
        node.prev = tailprev
        node.next = self.tail
        self.tail.prev = node

    def removeFromHead(self):
        if len(self.dic) == 0: return
        head_node = self.head.next
        del self.dic[head_node.key]
        self.removeFromList(head_node)
