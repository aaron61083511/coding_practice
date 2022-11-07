# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                if root.left is None and root.right is None:
                    root = None
                elif root.right is not None:
                    current = root.right
                    while current.left is not None:
                        current = current.left
                    root.val = current.val
                    root.right = self.deleteNode(root.right, root.val)
                else:
                    current = root.left
                    while current.right is not None:
                        current = current.right
                    root.val = current.val
                    root.left = self.deleteNode(root.left, root.val)
            return root
