# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:   
        def helper(node):
            if not node:
                return True
            return 1 + max(helper(node.left), helper(node.right))

        if not root:
            return True
        return abs(helper(root.left)-helper(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)