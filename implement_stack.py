class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def print_stack(self):
        if self.top is None:
            print('Empty Stack')
        else:
            current = self.top
            while current is not None:
                print(current.value)
                current = current.next

    def push(self, value):
        new = Node(value)
        if self.top is None:
            self.top = new
            self.bottom = new
        else:
            new.next = self.top
            self.top.prev = new
            self.top = new
        self.size += 1

    def pop(self):
        if self.top is None:
            print('Empty Stack')
        elif self.size == 1:
            self.top = None
            self.bottom = None
        else:
            self.top.next.prev = None
            self.top = self.top.next

    def peek_top(self):
        if self.top is not None:
            print(self.top.value)
        return None

    def peek_bottom(self):
        if self.bottom is not None:
            print(self.bottom.value)
        return None

    def get_index(self, value):
        if self.top is None:
            print('Empty Stack')
        else:
            current = self.top
            index = 0
            while current is not None:
                if current.value == value:
                    break
                current = current.next
                index += 1
            if current.value is None:
                print('Value not in Stack')
            else:
                print(index)

    def get_value(self, index):
        if self.top is None:
            print('Empty Stack')
        elif index >= 0:
            current = self.top
            counter = 0
            while current is not None:
                if counter == index:
                    break
                current = current.next
                counter += 1
            if current is None:
                print('Index out of range')
            else:
                print(current.value)
        else:
            current = self.bottom
            counter = -1
            while current is not None:
                if counter == index:
                    break
                current = current.prev
                counter -= 1
            if current is None:
                print('Index out of range')
            else:
                print(current.value)


stack = Stack()
stack.push('A')
stack.push('B')
# stack.pop()
# stack.push('C')
stack.print_stack()
stack.peek_top()
stack.peek_bottom()
stack.get_index('B')
stack.get_value(5)
