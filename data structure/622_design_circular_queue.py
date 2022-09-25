class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.list = []

    def enQueue(self, value: int) -> bool:
        if len(self.list) < self.size:
            self.list.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.list.pop(0)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[-1]

    def isEmpty(self) -> bool:
        if len(self.list) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.list) == self.size:
            return True
        return False