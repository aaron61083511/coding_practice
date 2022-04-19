# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        result = self.current = TreeNode()

        def inorder(node):
            if node:
                inorder(node.left)
                self.current.right = node
                node.left = None
                self.current = self.current.right
                inorder(node.right)

        inorder(root)
        return result.right
