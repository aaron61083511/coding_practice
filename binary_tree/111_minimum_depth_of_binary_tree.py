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
    
    def minDepth_II(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        depth = 0
        if not root:
            return depth
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not (node.left or node.right):
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
    
    def minDepth_DP(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        
        min_depth = float('inf')
        
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1 