class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for i in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if i != '#':
                slots += 2
        return slots == 0