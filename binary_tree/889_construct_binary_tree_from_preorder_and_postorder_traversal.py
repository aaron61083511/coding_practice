# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
                return TreeNode(postorder.pop())
        if preorder:
            root = TreeNode(postorder.pop())
            index = preorder.index(postorder[-1])   
            root.right = self.constructFromPrePost(preorder[index:], postorder)    
            root.left = self.constructFromPrePost(preorder[1:index], postorder)
            return root