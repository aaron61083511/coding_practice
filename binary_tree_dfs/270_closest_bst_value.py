# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack = []
        predecessor = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if target >= predecessor and target < root.val:
                return min(predecessor, root.val, key = lambda x: abs(target-x))

            predecessor = root.val
            root = root.right

        return predecessor

    def closestValue_binary_search(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target-x))
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return closest
