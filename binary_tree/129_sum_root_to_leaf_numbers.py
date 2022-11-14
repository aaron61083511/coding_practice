# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        res = 0
        def dfs(node, path):
            if not node:
                return 
            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append(path.copy())
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        for i in paths:
            res += int(''.join(i))
        
        return res