class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class HashTable(object):
    def __init__(self):
        self.array = [None] * 10
        self.head = None
        self.tail = None

    def hash(self, key):
        length = len(self.array)
        return key % length

    def print_list_item(self, key):
        if self.array[hash(key)] is not None:
            print_value = self.head
            while print_value is not None:
                print(print_value.value)
                print_value = print_value.next
        else:
            print('Value under this key is None')

# insert here is the default insert: add value at the tail of chain if collision
    def insert(self, key, value):
        new = Node(key, value)
        if self.array[hash(key)] is None:
            self.array[hash(key)] = new
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def remove(self, key, value):
        current = self.array[hash(key)]
        if self.array[hash(key)] is None:
            print('key value pair does not exist')
        else:
            while current is not None:
                if current.value == value:
                    break
                current = current.next
            if current is None:
                print('key value pair does not exist')
            elif current == self.head:
                if current.next is None:
                    self.head = None
                    self.tail = None
                else:
                    current.next.prev = None
                    self.head = current.next
            elif current == self.tail:
                if current.prev is None:
                    self.tail = None
                    self.head = None
                else:
                    current.prev.next = None
                    self.tail = current.prev
            else:
                current.next.prev = current.prev
                current.prev.next = current.next



hashmap = HashTable()
# hashmap.insert(1, 'A')
hashmap.insert(1, 'B')
# hashmap.insert(1, 'C')
hashmap.remove(1, 'B')
hashmap.print_list_item(1)
