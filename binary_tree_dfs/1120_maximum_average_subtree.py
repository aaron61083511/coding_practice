# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree_recursive(self, root: Optional[TreeNode]) -> float:
        if root is None:
            return None

        def dfs(node):
            if node is None:
                return (0, 0, 0)
            sum_left, n_left, max_val_left = dfs(node.left)
            sum_right, n_right, max_val_right = dfs(node.right)
            sum_total = sum_left + sum_right + node.val
            n_total = n_left + n_right + 1
            avg_node = sum_total/n_total
            return sum_total, n_total, max(max_val_left, max_val_right, avg_node)

        return dfs(root)[2]

    def maximumAverageSubtree_iterative(self, root: Optional[TreeNode]) -> float:
        if root is None:
            return None

        queue = [root]
        max_val = 0
        visited = {None:(0,0)}

        while queue:
            node = queue.pop()
            if node:
                if node.left in visited and node.right in visited:
                    sum_left, n_left = visited[node.left]
                    sum_right, n_right = visited[node.right]
                    sum_node = node.val + sum_left + sum_right
                    n_node = 1 + n_left + n_right
                    visited[node] = sum_node, n_node
                    max_val = max(max_val, sum_node/n_node)
                else:
                    queue.append(node)
                    queue.append(node.left)
                    queue.append(node.right)
        return max_val
