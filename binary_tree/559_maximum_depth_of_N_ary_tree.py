"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        queue = deque([root])

        if not root:
            return depth

        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.children:
                    for c in node.children:
                        queue.append(c)
        return depth
    
    def maxDepth_DP(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        if root.children:
            for c in root.children:
                depth = max(self.maxDepth(c), depth)
        return depth + 1
    
    def maxDepth_Backtracking(self, root: 'Node') -> int:
        depth, res = 0, 0
        def dfs(node):
            nonlocal depth, res
            if not node:
                return
            depth += 1
            res = max(depth, res)
            if node.children:
                for c in node.children:
                    dfs(c)
            depth -= 1
        
        dfs(root)
        return res