# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def helper(node):
            nonlocal res
            if not node:
                return 0
            if low <= node.val <= high:
                res += node.val
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return res