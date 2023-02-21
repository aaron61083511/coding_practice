# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []
        def helper(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                left = helper(start, i - 1)
                right = helper(i + 1, end)
                for l in left:
                    for r in right:
                        current = TreeNode(i)
                        current.left = l
                        current.right = r
                        res.append(current)
            return res
        return helper(1, n)