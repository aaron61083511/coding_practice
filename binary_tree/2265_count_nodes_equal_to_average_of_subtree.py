# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            if not node.left and not node.right:
                count = 1
                sum_sub = node.val
            count_left, sum_left = dfs(node.left)
            count_right, sum_right = dfs(node.right)
            count = count_left + count_right + 1
            sum_sub = sum_left + sum_right + node.val
            avg = sum_sub // count
            if avg == node.val:
                res += 1
            return count, sum_sub
        dfs(root)
        return res