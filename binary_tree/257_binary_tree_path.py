# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths_iterative(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return None
        result = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
            if not node.left and not node.right:
                result.append(path)
        return result

    def binaryTreePaths_recursive(self, root: Optional[TreeNode]) -> List[str]:
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths
