# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance_I(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0

        def dfs(node):
            if not node:
                return 0, 0
            
            cnt = 1 if node.val in [p, q] else 0
            lcnt, lpath = dfs(node.left)
            rcnt, rpath = dfs(node.right)
            cnt += lcnt + rcnt
            
            if cnt == 2:
                return 2, lpath + rpath
            elif cnt == 1:
                return 1, max(lpath, rpath) + 1
            return 0, 0
        
        return dfs(root)[1]
    
    def findDistance_II(self, root: TreeNode, p: int, q: int) -> int:
        def dfs(node):
                if not node or node.val == p or node.val == q:
                    return node
                left = dfs(node.left)
                right = dfs(node.right)
                if left and right:
                    return node
                else:
                    return left or right
                
        def dist(node, target):
            if not node:
                return float('inf')
            if node.val == target:
                return 0
            return 1 + min(dist(node.left, target), dist(node.right, target))
        
        lca = dfs(root)
        return dist(lca, p) + dist(lca, q)