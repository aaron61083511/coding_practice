# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre, min_val, max_val):
            node = None
            if pre and min_val < pre[0] < max_val:
                node = TreeNode(pre.popleft())
                node.left = dfs(pre, min_val, node.val)
                node.right = dfs(pre, node.val, max_val)
            return node
        return dfs(deque(preorder), float('-inf'), float('inf'))