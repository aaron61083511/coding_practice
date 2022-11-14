# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def helper(node, len_path, parent_val):
            if not node:
                return 0
            if parent_val + 1 == node.val:
                len_path += 1
            else:
                len_path = 1
            left = helper(node.left, len_path, node.val)
            right = helper(node.right, len_path, node.val)
            return max(left, right, len_path)
        
        return helper(root, 1, float('-inf'))