# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque([])
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
    def inorderTraversal_recurrsive(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        inorder(root)
        return res