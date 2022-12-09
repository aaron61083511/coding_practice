# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return None, None
        elif root.val <= target:
            sub = self.splitBST(root.right, target)
            root.right = sub[0]
            return root, sub[1]
        else:
            sub = self.splitBST(root.left, target)
            root.left = sub[1]
            return sub[0], root