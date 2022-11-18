# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]: 
        def dfs_left_boundary(node):
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)
            if node.left:
                dfs_left_boundary(node.left)
            else:
                dfs_left_boundary(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_right_boundary(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                dfs_right_boundary(node.right)
            else:
                dfs_right_boundary(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_left_boundary(root.left)
        dfs_leaves(root)
        dfs_right_boundary(root.right)
        return boundary