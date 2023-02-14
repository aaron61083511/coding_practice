# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST_I(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root

    def searchBST_R(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        return self.searchBST_R(root.left, val) if root.val > val else self.searchBST_R(root.right, val)