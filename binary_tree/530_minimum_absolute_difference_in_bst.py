# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = float('inf')
       
        def helper(node):
            nonlocal prev, res
            if not node:
                return
            helper(node.left)
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            helper(node.right)
        
        helper(root)
        return res