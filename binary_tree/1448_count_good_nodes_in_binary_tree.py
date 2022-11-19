# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(node, path_max):
            nonlocal count
            if not node:
                return
            if path_max <= node.val:
                count += 1
            path_max = max(path_max, node.val)
            helper(node.left, path_max)
            helper(node.right, path_max)
        helper(root, root.val)
        return count