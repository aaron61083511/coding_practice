# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node, p, q):
            if not node or node in (p, q):
                return node
            left = helper(node.left, p, q)
            right = helper(node.right, p, q)

            if left and right:
                return node
            return left or right
        
        def find(root, node):
            if not root:
                return False
            return root == node or find(root.left, node) or find(root.right, node)
        
        if find(root, p) and find(root, q):
            return helper(root, p, q)
        return None