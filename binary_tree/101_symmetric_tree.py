# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compareSides( left, right):
            if left is None and right is None:
                return True
            elif left and right and (left.val == right.val):
                return compareSides(left.left, right.right) and compareSides(left.right, right.left)
            else:
                return False
        return compareSides(root.left, root.right)