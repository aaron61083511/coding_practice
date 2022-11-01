# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return
        
        graph = defaultdict(list)
        level = 0
        visited = {start}

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)
        
        q = deque([start])
        while q:
            size = len(q)
            for _ in range(size):
                n = q.popleft()
                for nei in graph[n]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            if q:
                level += 1
        
        return level