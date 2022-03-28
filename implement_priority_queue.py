# A priority queue must at least support the following operations:
#
# is_empty: check whether the queue has no elements.
# insert_with_priority: add an element to the queue with an associated priority.
# pull_highest_priority_element: remove the element from the queue that has the highest priority, and return it.
# This is also known as "pop_element(Off)", "get_maximum_element" or "get_front(most)_element".
# Some conventions reverse the order of priorities, considering lower values to be higher priority, so this may also be known as "get_minimum_element", and is often referred to as "get-min" in the literature.
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


class pqueue(object):
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

    def 
