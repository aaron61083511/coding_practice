# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder_list = []
        def inorder(node):
            if node:
                inorder(node.left)
                inorder_list.append(node.val)
                inorder(node.right)
        inorder(root)

        def build(l, r):
            if l <= r:
                mid = (l+r)//2
                root = TreeNode(inorder_list[mid])
                root.left = build(l, mid-1)
                root.right = build(mid+1, r)
                return root
        
        return build(0, len(inorder_list)-1)