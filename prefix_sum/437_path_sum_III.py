# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, prevSum, sum_):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            if currSum - sum_ in rec:
                count += rec[currSum - sum_]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            count += dfs(root.left, currSum, sum_)
            count += dfs(root.right, currSum, sum_)
            rec[currSum] -= 1
            return count
            
        rec = {0:1}
        return dfs(root, 0, targetSum)