# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node):
            if not node or node.val in [startValue, destValue]:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            else:
                return left or right
                
        def findPath(node, target, path):
            if not node:
                return
            if node.val == target:
                return path
            path.append('L')
            left = findPath(node.left, target, path)
            if left:
                return left
            path.pop()
            
            path.append('R')
            right = findPath(node.right, target, path)
            if right:
                return right
            path.pop()
        
        lca = dfs(root)
        return 'U' * len(findPath(lca, startValue, [])) + ''.join(findPath(lca, destValue, []))