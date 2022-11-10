# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        queue = []
        def dfs(node):
            if node:
                heapq.heappush(queue, node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        if queue:
            num = heapq.heappop(queue)
        while queue:
            new = heapq.heappop(queue)
            if num < new:
                return new
        return -1
    
    def findSecondMinimumValue_1(self, root):
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1