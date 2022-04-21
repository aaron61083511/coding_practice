import random
class RandomizedSet:

    def __init__(self):
        self.dic = dict()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dic:
            last, index = self.list[-1], self.dic[val]
            self.list[index], self.dic[last] = last, index
            self.list.pop()
            del self.dic[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]
