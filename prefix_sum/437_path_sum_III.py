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

    def pathSum_alternative(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = curr_sum = 0
        h = defaultdict(int)

        def helper(node, curr_sum):
            nonlocal count, h
            if not node:
                return 0
            curr_sum += node.val
            if curr_sum == targetSum:
                count += 1
            count += h[curr_sum-targetSum]
            h[curr_sum] += 1
            helper(node.left, curr_sum)
            helper(node.right, curr_sum)
            h[curr_sum] -= 1
        
        helper(root, curr_sum)
        return count