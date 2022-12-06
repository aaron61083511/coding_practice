# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            if not node.left and not node.right:
                sum_sub = node.val
            sum_sub = dfs(node.left) + dfs(node.right) + node.val
            if sum_sub - node.val == node.val:
                res += 1
            return sum_sub
        dfs(root)
        return res