class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_queue(self):
        if self.size == 0:
            print('Queue is empty')
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

    def enqueue(self, value):
        new = Node(value)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print('Queue is empty')
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1

    def peek(self):
        if self.head is not None:
            print(self.head.value)
        return None

    def get_index(self, value):
        if self.head is None:
            print('Empty queue')
        else:
            index = 0
            current = self.head
            while current is not None:
                if current.value == value:
                    break
                current = current.next
                index += 1
            if current is None:
                print('Item not in queue')
            else:
                print(index)

    def get_value(self, index):
        if self.head is None:
            print('Empty queue')
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



queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
# queue.dequeue()
queue.peek()
# queue.print_queue()
queue.get_index('B')
queue.get_value(-1)
