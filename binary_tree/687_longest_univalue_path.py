# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node, val):
            nonlocal res
            if not node:
                return 0
            left_len = helper(node.left, node.val)
            right_len = helper(node.right, node.val)
            res = max(res, left_len + right_len)
            if node.val != val:
                return 0
            return 1 + max(left_len, right_len)
        if not root:
            return 0
        helper(root, root.val)
        return res