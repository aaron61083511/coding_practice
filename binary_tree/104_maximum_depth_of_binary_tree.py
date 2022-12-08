# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        queue = deque([root])
        
        if not root:
            return level
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return level
    
    def maxDepth_DP(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        res = max(left, right) + 1
        return res
    
    def maxDepth_Backtracking(self, root: Optional[TreeNode]) -> int:
        depth = 0
        res = 0
        def dfs(node):
            nonlocal depth, res
            if not node:
                return
            depth += 1
            res = max(depth, res)
            dfs(node.left)
            dfs(node.right)
            depth -= 1
        
        dfs(root)
        return res