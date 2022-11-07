# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def insertIntoBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while current:
            if current.val < val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    return root
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    return root
        return TreeNode(val)


