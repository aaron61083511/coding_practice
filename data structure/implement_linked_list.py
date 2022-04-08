class Node(object):
    def __init__(self, node = None):
        self.node = node
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_list(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.node)
            printvalue = printvalue.next

    def get_head(self):
        if self.head:
            return self.head.node
        else:
            print('Head is Null')

    def get_length(self):
        count = 0
        val = self.head
        while val:
            count += 1
            val = val.next
        return count

    def add_head(self, newnode):
        new = Node(newnode)
        new.next = self.head
        self.head = new

    def get_tail(self):
        val = self.head
        while val:
            val = val.next
            if val is not None:
                tail = val.node
        return tail

    def add_end(self, newnode):
        val = self.head
        while val.next:
            val = val.next
        val.next = Node(newnode)

    def insert(self, middle_node, newdata):
        if middle_node is None:
            print('No mentioned node')
            return
        newnode = Node(newdata)
        newnode.next = middle_node.next
        middle_node.next = newnode

    def find_index(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.node == value:
                return index
            current = current.next
            index += 1
        return None

    def find_value(self, index):
        current = self.head
        count = 0
        while current is not None:
            if index == count:
                return current.node
            current = current.next
            count += 1
        return None

    def remove_head(self):
        self.head = self.head.next

    def remove_tail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def remove_from_value(self, value):
        current = self.head
        if self.find_index(value) is None:
            print('Item not in list')
        elif current.node == value:
            self.head = current.next
        else:
            while current is not None:
                if current.node == value:
                    break
                pre = current
                current = current.next
            pre.next = current.next

    def remove_from_index(self, index):
        current = self.head
        count = 0
        if self.find_value(index) is None:
            print('Index out of range')
        elif count == index:
            self.head = current.next
        else:
            while current is not None:
                if count == index:
                    break
                pre = current
                current = current.next
                count += 1
            pre.next = current.next

list = LinkedList()
list.head = Node('A')
value2 = Node('B')
value3 = Node('D')
list.head.next = value2
value2.next = value3
# list.add_head('start')
# list.add_head('')
# list.add_head('sd')
# list.add_head(None)
# list.add_tail('xx')
# list.add_tail(None)
list.insert(value2, 'C')
list.insert(value2.next, 'E')
# list.remove_head()
# list.remove_tail()
# list.remove_from_value('G')
list.remove_from_index(4)
list.print_list()
# print(list.get_head())
# print(list.get_end())
# print(list.get_length())
# print(list.find_index('E'))
# print(list.find_value(1))
