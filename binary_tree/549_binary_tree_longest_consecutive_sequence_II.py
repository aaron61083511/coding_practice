# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int: 
        def helper(node):
            nonlocal res
            if not node:
                return [0, 0]
            asc, des = 1, 1
            if node.left:
                left = helper(node.left)
                if node.val == node.left.val + 1:
                    des = left[1] + 1
                elif node.val == node.left.val - 1:
                    asc = left[0] + 1
            if node.right:
                right = helper(node.right)
                if node.val == node.right.val + 1:
                    des = max(right[1]+1, des)
                elif node.val == node.right.val - 1:
                    asc = max(right[0]+1, asc)
            res = max(res, asc + des - 1)
            return [asc, des]
        
        res = 0
        helper(root)
        return res