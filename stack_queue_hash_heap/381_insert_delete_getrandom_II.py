from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.dic = defaultdict(set)


    def insert(self, val: int) -> bool:

        self.dic[val].add(len(self.list))
        self.list.append(val)
        if len(self.dic[val]) == 1:
            return True
        return False


    def remove(self, val: int) -> bool:
        if self.dic[val]:
            last, index = self.list[-1], self.dic[val].pop()
            self.list[index] = last
            self.dic[last].add(index)
            self.dic[last].discard(len(self.list)-1)
            self.list.pop()
            return True
        return False


    def getRandom(self) -> int:
        return choice(self.list)
