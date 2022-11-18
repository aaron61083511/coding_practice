# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = []
        self.left_most(root)
        self.pointer = -1
    
    def left_most(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.pointer + 1 < len(self.cur)

    def next(self) -> int:
        if self.pointer + 1 < len(self.cur):
            self.pointer += 1
            return self.cur[self.pointer]
        else:
            num = self.stack.pop()
            self.cur.append(num.val)
            self.pointer += 1

            if num.right:
                self.left_most(num.right)
            return num.val

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.cur[self.pointer]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()