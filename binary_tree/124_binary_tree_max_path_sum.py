# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            curr = left + right + node.val
            max_sum = max(curr, max_sum)
            return node.val + max(left, right)
        max_gain(root)
        return max_sum