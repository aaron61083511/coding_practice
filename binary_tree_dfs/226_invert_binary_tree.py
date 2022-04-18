# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree_recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

#         def invert_dfs(node):
#             if node:
#                 invert_dfs(node.left)
#                 invert_dfs(node.right)
#                 node.left, node.right = node.right, node.left
#             return node

#         return invert_dfs(root)

        root.left, root.right = self.invertTree_recursive(root.right), self.invertTree_recursive(root.left)
        return root

    def invertTree_iterative_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

    def invertTree_iterative_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
