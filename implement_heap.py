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

    def insert(self, value):
        self.list.append(value)

    def build_heap(self, method):
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

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.min_heap_list) and self.min_heap_list[left] < self.min_heap_list[i]:
            current = left
        else:
            current = i
        if right < len(self.min_heap_list) and self.min_heap_list[right] < self.min_heap_list[current]:
            current = right
        if current != i:
            self.min_heap_list[i], self.min_heap_list[current] = self.min_heap_list[current], self.min_heap_list[i]
            self.min_heapify(current)

    def build_max_heap(self):
        self.max_heap_list = self.list.copy()
        n = int((len(self.max_heap_list) // 2) - 1)
        for i in range(n, -1, -1):
            self.max_heapify(i)

    def build_min_heap(self):
        self.min_heap_list = self.list.copy()
        n = int((len(self.min_heap_list)//2) - 1)
        for i in range(n, -1, -1):
            self.min_heapify(i)

    def get_max_heapify_list(self):
        print(self.max_heap_list)
        return self.max_heap_list

    def get_min_heapify_list(self):
        print(self.min_heap_list)
        return self.min_heap_list

    def remove_item_max_heap(self, max_list, value):
        if value not in max_list:
            print('Value not in list')
        else:
            current = max_list.index(value)
            max_list[current] = max_list[len(max_list) - 1]
            max_list.pop()
            self.max_heap_list = max_list.copy()
            n = int((len(self.max_heap_list) // 2) - 1)
            for i in range(n, -1, -1):
                self.max_heapify(i)

    def remove_item_min_heap(self, min_list, value):
        if value not in min_list:
            print('Value not in list')
        else:
            current = min_list.index(value)
            min_list[current] = min_list[len(min_list)-1]
            min_list.pop()
            self.min_heap_list = min_list.copy()
            n = int((len(self.min_heap_list)//2)-1)
            for i in range(n, -1, -1):
                self.min_heapify(i)


heap_list = Heap()
heap_list.insert(6)
heap_list.insert(9)
heap_list.insert(15)
heap_list.insert(8)
heap_list.insert(11)
heap_list.insert(4)
heap_list.insert(7)
heap_list.insert(20)
heap_list.insert(25)
heap_list.build_heap('max')
heap_list.build_heap('min')
max_heap_list = heap_list.get_max_heapify_list()
min_heap_list = heap_list.get_min_heapify_list()
heap_list.remove_item_max_heap(max_heap_list, 9)
heap_list.remove_item_min_heap(min_heap_list, 11)
heap_list.get_list()
heap_list.get_max_heapify_list()
heap_list.get_min_heapify_list()
# heap_list.get_root('max')
