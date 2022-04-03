# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


class Heap(object):
    def __init__(self):
        self.root = None
        self.list = []
        self.max_heap_list = []
        self.min_heap_list = []

    def get_root(self, method):
        if method == 'max':
            if not self.list:
                print('Empty Heap')
            else:
                print(self.max_heap_list[0])
        if method == 'min':
            if not self.list:
                print('Empty Heap')
            else:
                print(self.min_heap_list[0])

    def get_list(self):
        print(self.list)

    def insert(self, value, method):
        self.list.append(value)
        if method == 'min':
            self.build_min_heap()
        if method == 'max':
            self.build_max_heap()

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.max_heap_list) and self.max_heap_list[left] > self.max_heap_list[i]:
            current = left
        else:
            current = i
        if right < len(self.max_heap_list) and self.max_heap_list[right] > self.max_heap_list[current]:
            current = right
        if current != i:
            self.max_heap_list[i], self.max_heap_list[current] = self.max_heap_list[current], self.max_heap_list[i]
            self.max_heapify(current)

    def build_max_heap(self):
        self.max_heap_list = self.list.copy()
        n = int((len(self.max_heap_list) // 2) - 1)
        for i in range(n, -1, -1):
            self.max_heapify(i)

    def get_max_heapify_list(self):
        print(self.max_heap_list)


heap_list = Heap()
heap_list.insert(6, 'max')
heap_list.insert(9, 'max')
heap_list.insert(15, 'max')
heap_list.insert(8, 'max')
heap_list.insert(11, 'max')
heap_list.insert(4, 'max')
heap_list.insert(7, 'max')
heap_list.insert(20, 'max')
heap_list.get_list()
heap_list.get_max_heapify_list()
heap_list.get_root('max')
