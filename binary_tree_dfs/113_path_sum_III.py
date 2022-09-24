class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, remainingSum, visited):
            if not node:
                return None
            visited.append(node.val)
            remainingSum -= node.val
            if not node.left and not node.right and remainingSum == 0:
                res.append(visited.copy())
            else:
                dfs(node.left, remainingSum, visited)
                dfs(node.right, remainingSum, visited)
            visited.pop()

        res = []
        dfs(root, targetSum, [])
        return res