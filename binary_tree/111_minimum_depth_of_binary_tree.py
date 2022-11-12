# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([(1, root)])
        if not root:
            return 0
        while queue:
            l, node = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return l
                if node.left:
                    queue.append((l+1, node.left))
                if node.right:
                    queue.append((l+1, node.right))
        return l