# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor

    def inorderSuccessor_alternaltive(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = []
        def helper(node):
            while node:
                stack.append(node)
                node = node.left
        cur = root
        helper(cur)
        while stack:
            num = stack.pop()
            if num.right:
                helper(num.right)
            if num.val == p.val:
                if not stack:
                    return None
                return stack.pop()
            
        return None