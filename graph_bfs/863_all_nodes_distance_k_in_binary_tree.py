class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
        
        visited = {target.val}
        q = deque([(target.val, 0)])
        while q:
            size = len(q)
            for _ in range(size):
                n, d = q.popleft()
                if d == k:
                    res.append(n)
                for nei in graph[n]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, d+1))
        
        return res