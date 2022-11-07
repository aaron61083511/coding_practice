# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        
        def dfs(node,ht):
            if ht==depth-1:
                cur1, cur2 = TreeNode(val), TreeNode(val)
                cur1.left, cur2.right = node.left, node.right
                node.left, node.right = cur1, cur2
                
            if node.left:
                dfs(node.left,ht+1)
            if node.right:
                dfs(node.right,ht+1)
            
            
        dfs(root,1)
        return root
                