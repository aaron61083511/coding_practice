class Node(object):
    def __init__(self, node=None):
        self.node = node
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        print_value = self.head
        while print_value is not None:
            print(print_value.node)
            print_value = print_value.next

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

    # push without tail (O(1))
    def add_head(self, new_node):
        new = Node(new_node)
        new.next = self.head
        new.prev = None
        if self.head is not None:
            self.head.prev = new
        self.head = new

    # push with tail (O(1))
    def add_head_withtail(self, new_node):
        new = Node(new_node)
        new.next = self.head
        new.prev = None

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.head.prev = new
            self.head = new

    # without tail (O(n))
    def get_tail(self):
        val = self.head
        while val:
            val = val.next
            if val is not None:
                end = val.node
        return end

    # with tail (O(1))
    def get_tail_withtail(self):
        if self.tail is None:
            print('Empty')
        else:
            return self.tail.node

    # push without tail (O(n))
    def add_end(self, new_node):
        new = Node(new_node)
        val = self.head
        new.next = None
        if self.head is None:
            new.prev = None
            self.head = new
        while val.next:
            val = val.next
        val.next = new
        new.prev = val

    # Use tail in push function (O(1))
    def add_end_withtail(self, new_node):
        new = Node(new_node)
        new.next = None
        new.prev = self.tail

        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def insert(self, middle_node, new_data):
        if middle_node is None:
            print('No mentioned node')
            return
        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node
        new_node.prev = middle_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def insert_after_item(self, item, new_data):
        if self.head is None:
            print('Empty List')
        else:
            new = Node(new_data)
            current = self.head
            while current is not None:
                if current.node == item:
                    break
                current = current.next
            if current is None:
                print('Item Not Found')
            elif current == self.tail:
                new.next = None
                new.prev = current
                current.next = new
                self.tail = new
            else:
                new.next = current.next
                new.prev = current
                current.next = new

    def insert_before_item(self, item, new_data):
        if self.head is None:
            print('Empty List')
        else:
            new = Node(new_data)
            current = self.head
            while current is not None:
                if current.node == item:
                    break
                current = current.next
            if current is None:
                print('Item Not Found')
            elif current == self.head:
                new.prev = None
                current.prev = new
                new.next = current
                self.head = new
            else:
                new.prev = current.prev
                current.prev = new
                new.next = current

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
        if self.head is None:
            print('Empty List')
        else:
            self.head = self.head.next
            self.head.next.prev = None

    def remove_tail(self):
        if self.head is None:
            print('Empty List')
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.prev.next = None

    def remove_from_value(self, value):
        if self.head is None:
            print('Emtpy List')
        else:
            current = self.head
            while current is not None:
                if current.node == value:
                    break
                current = current.next
            if current is None:
                print('Item not in list')
            elif current == self.head:
                current.next.pre = None
                self.head = current.next
            elif current == self.tail:
                current.prev.next = None
                self.tail = current.prev
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

    def remove_from_index(self, index):
        if self.head is None:
            print('Empty List')
        elif index >= 0:
            current = self.head
            count = 0
            while current is not None:
                if count == index:
                    break
                current = current.next
                count += 1
            if current is None:
                print('Index out of range')
            elif current == self.head:
                current.next.prev = None
                self.head = current.next
            elif current == self.tail:
                current.prev.next = None
                self.tail = current.prev
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
        else:
            current = self.tail
            count = -1
            while current is not None:
                if count == index:
                    break
                current = current.prev
                count -= 1
            if current is None:
                print('Index out of range')
            elif current == self.tail:
                current.prev.next = None
                self.tail = current.prev
            elif current == self.head:
                current.next.prev = None
                self.head = current.next
            else:
                current.next.prev = current.prev
                current.prev.next = current.next


list = DoublyLinkedList()
list.add_head_withtail('AA')
list.add_end_withtail('BB')
list.insert_after_item('BB', 'B')
list.insert_before_item('AA', 'A')
# print(list.get_tail_withtail())
# list.print_list()
# list.remove_from_value('AA')
# list.remove_from_index(-5)
# list.remove_tail()
# list.remove_head()
# list.head = Node('A')
# value2 = Node('B')
# value3 = Node('D')
# list.head.next = value2
# value2.next = value3
# list.add_head('start')
# list.add_head('')
# list.add_head('sd')
# list.add_head(None)
# list.add_tail('xx')
# list.add_tail(None)
# list.insert(value2, 'C')
# list.insert(value2.next, 'E')
# list.remove_head()
# list.remove_tail()
# list.remove_from_value('G')
# list.remove_from_index(5)
list.print_list()
# print(list.get_head())
# print(list.get_end())
# print(list.get_length())
# print(list.find_index('E'))
# print(list.find_value(1))
