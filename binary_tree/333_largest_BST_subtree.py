# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0 
        if not root:
            return res
        
        if self.valid(root):
            return self.size(root)
        
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
        
    def valid(self, root_node):
        upper, lower = float('inf'), float('-inf')

        def check(node, upper, lower):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return check(node.left, node.val, lower) and check(node.right, upper, node.val)
        
        return check(root_node, upper, lower)
            
    def size(self, node):
        if not node:
            return 0
        return self.size(node.left) + 1 + self.size(node.right)

    
# Short solution:
    def largestBSTSubtree(self, root):
        def dfs(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
        return dfs(root)[0]