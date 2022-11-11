# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST_iterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)

    def isValidBST_inorder_recursive(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

    def isValidBST_inorder_iterative(self, root: Optional[TreeNode]) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        c = float('+inf')
        f = float('-inf')
        
        def dfs(x, c, f): 
            if x is None:
                return True
            if not c > x.val > f:
                return False
				
			#update ceiling and floor:	
            #left child: ceiling is parent's val floor is parent's floor
            #right child: ceiling is parent's ceiling floor is parent's val
            return dfs(x.left, x.val, f) and dfs(x.right, c, x.val)
        
        return dfs(root, c, f)