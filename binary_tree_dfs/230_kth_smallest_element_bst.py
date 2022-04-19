# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallest_recursive(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node:
                return inorder(node.left) + [node.val] + inorder(node.right)
            return []
        return inorder(root)[k-1]
