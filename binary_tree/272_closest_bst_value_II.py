# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        visited = []
        res = []
        def helper(node):
            if node:
                heapq.heappush(visited, (abs(node.val - target), node.val))
                helper(node.left)
                helper(node.right)
        helper(root)
        while k:
            res.append(heapq.heappop(visited)[1])
            k -= 1
        return res