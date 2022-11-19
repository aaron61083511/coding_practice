# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        a = []
        def list_a(node):
            if not node:
                return
            list_a(node.left)
            a.append(node.val)
            list_a(node.right)
        list_a(root)
        b = a.copy()
        b.append(val)

        def helper(nums=[]):
            if not nums:
                return
            max_value = max(nums)
            node = TreeNode(max_value)
            index = nums.index(max_value)
            node.left = helper(nums[:index])
            node.right = helper(nums[index+1:])
            return node
        
        return helper(b)