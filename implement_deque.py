class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_deque(self):
        if self.size == 0:
            print('Deque is empty')
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

    def add_tail(self, value):
        new = Node(value)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.size += 1

    def add_head(self, value):
        new = Node(value)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new
        self.size += 1

    def remove_head(self):
        if self.size == 0:
            print('Deque is empty')
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1

    def remove_tail(self):
        if self.size == 0:
            print('Deque is empty')
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.size -= 1

    def peek_head(self):
        if self.head is not None:
            print(self.head.value)
        return None

    def peek_tail(self):
        if self.tail is not None:
            print(self.tail.value)
        return None

    def get_index(self, value):
        if self.head is None:
            print('Empty deque')
        else:
            index = 0
            current = self.head
            while current is not None:
                if current.value == value:
                    break
                current = current.next
                index += 1
            if current is None:
                print('Item not in deque')
            else:
                print(index)

    def get_value(self, index):
        if self.head is None:
            print('Empty deque')
        elif index >= 0:
            counter = 0
            current = self.head
            while current:
                if counter == index:
                    break
                current = current.next
                counter += 1
            if current is None:
                print('Index out of range')
            else:
                print(current.value)
        else:
            counter = -1
            current = self.tail
            while current:
                if counter == index:
                    break
                current = current.prev
                counter -= 1
            if current is None:
                print('Index out of range')
            else:
                print(current.value)

    def get_length(self):
        print(self.size)


deque = Deque()
deque.add_head('A')
deque.add_head('B')
# deque.add_tail('C')
deque.get_length()
# deque.remove_head()
# deque.remove_tail()
# deque.peek_head()
deque.peek_tail()
deque.print_deque()
deque.get_index('B')
deque.get_value(-5)
