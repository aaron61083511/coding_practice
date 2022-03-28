# A priority queue must at least support the following operations:
#
# is_empty: check whether the queue has no elements.
#   insert_with_priority: add an element to the queue with an associated priority.
#   pull_highest_priority_element: remove the element from the queue that has the highest priority, and return it.
#   This is also known as "pop_element(Off)", "get_maximum_element" or "get_front(most)_element".
#   Some conventions reverse the order of priorities, considering lower values to be higher priority, so this may also be known as "get_minimum_element", and is often referred to as "get-min" in the literature.
# This may instead be specified as separate "peek_at_highest_priority_element" and "delete_element" functions, which can be combined to produce "pull_highest_priority_element".
# In addition, peek (in this context often called find-max or find-min), which returns the highest-priority element but does not modify the queue, is very frequently implemented, and nearly always executes in O(1) time. This operation and its O(1) performance is crucial to many applications of priority queues.
#
# More advanced implementations may support more complicated operations, such as pull_lowest_priority_element, inspecting the first few highest- or lowest-priority elements, clearing the queue, clearing subsets of the queue, performing a batch insert, merging two or more queues into one, incrementing priority of any element, etc.

class Node(object):
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.prev = None
        self.next = None


class Pqueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_pq(self):
        if self.head is None:
            print('Empty PQ')
        else:
            current = self.head
            while current is not None:
                print(current.priority, current.value)
                current = current.next

    def insert_with_priority(self, value, priority):
        new = Node(value, priority)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            current = self.tail
            while current is not None:
                if current.priority >= new.priority:
                    break
                current = current.prev
            if current is None:
                self.head.prev = new
                new.next = self.head
                self.head = new
            elif current == self.tail:
                self.tail.next = new
                new.prev = self.tail
                self.tail = new
            else:
                new.next = current.next
                new.prev = current
                current.next.prev = new
                current.next = new
        self.size += 1

    def pull_highest_priority_element(self):
        if self.head is None:
            print('Empty PQ')
        else:
            # print(self.head.priority, self.head.value)
            self.head = self.head.next
            self.head.next.prev = None
        self.size -= 1

    def peek_highest_priority(self):
        if self.head is None:
            print('Empty PQ')
        else:
            print(self.head.priority, self.head.value)

    def peek_lowest_priority(self):
        if self.tail is None:
            print('Empty PQ')
        else:
            print(self.tail.priority, self.tail.value)

    def get_index_from_value(self, value):
        # get the index of value with highest priority
        if self.head is None:
            print('Empty PQ')
        else:
            current = self.head
            index = 0
            while current is not None:
                if current.value == value:
                    break
                current = current.next
                index += 1
            if current is None:
                print('Value is not in PQ')
            else:
                print(index)

    def get_index_from_priority(self, priority):
        # get first value index of input priority level
        if self.head is None:
            print('Empty PQ')
        else:
            current = self.head
            index = 0
            while current is not None:
                if current.priority == priority:
                    break
                current = current.next
                index += 1
            if current is None:
                print('Priority out of range')
            else:
                print(index)

    def get_priority_from_value(self, value):
        # print highest priority
        if self.head is None:
            print('Empty PQ')
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    break
                current = current.next
            if current is None:
                print('Value is not in PQ')
            else:
                print(current.priority)

    def get_value_from_priority(self, priority):
        # print first value under same priority
        if self.head is None:
            print('Empty PQ')
        else:
            current = self.head
            while current is not None:
                if current.priority == priority:
                    break
                current = current.next
            if current is None:
                print('Priority out of range')
            else:
                print(current.value)

    def get_value_priority_from_index(self, index):
        if self.head is None:
            print('Empty QP')
        elif index >= 0:
            current = self.head
            counter = 0
            while current is not None:
                if counter == index:
                    break
                current = current.next
                counter += 1
            if current is None:
                print('Index out of range')
            else:
                print(current.priority, current.value)
        else:
            current = self.tail
            counter = -1
            while current is not None:
                print(current.priority, current.value, counter)
                if counter == index:
                    break
                current = current.prev
                counter -= 1
            if current is None:
                print('Index out of range')
            else:
                print(current.priority, current.value)


    # def remove_item_from_index(self, index):
    #
    # def remove_item_from_value(self, value):
    #
    # def remove_item_from_priority(self, priority):



pq = Pqueue()
pq.insert_with_priority('A', 0)
pq.insert_with_priority('B', 0)
pq.insert_with_priority('AA', 1)
pq.insert_with_priority('BB', 1)
pq.insert_with_priority('AAA', 3)
pq.insert_with_priority('AA2', 2)
# pq.pull_highest_priority_element()
# pq.peek_lowest_priority()
# pq.peek_highest_priority()
# pq.get_index_from_value('BB')
# pq.get_index_from_priority(2)
# pq.get_priority_from_value('AAA')
# pq.get_value_from_priority(5)
pq.get_value_priority_from_index(-4)
pq.print_pq()
