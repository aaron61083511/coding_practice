# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum_dfs(self, root: Optional[TreeNode]) -> int:
        res, max_depth = 0, 0
        def dfs(node, depth):
            nonlocal res, max_depth
            if not node:
                return
            if depth > max_depth:
                res = node.val
                max_depth = depth
            elif depth == max_depth:
                res += node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 1)
        return res
    
    def deepestLeavesSum_bfs(self, root: Optional[TreeNode]) -> int:
        res, lvl, max_depth = 0, 0, 0
        queue = deque([root])
        while queue:
            lvl += 1
            if lvl > max_depth:
                max_depth = lvl
                res = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                res += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
    
    def deepestLeavesSum_bfs_II(self, root: Optional[TreeNode]) -> int:
        res, lvl = 0, 0
        queue = deque([root])
        visited = defaultdict(list)
        while queue:
            lvl += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                visited[lvl].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum(visited[lvl])