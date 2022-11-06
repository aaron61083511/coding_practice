class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        res = []
        queue.append((0, [0]))
        target = len(graph) - 1
        while queue:
            node, path = queue.popleft()
            if node == target:
                res.append(path)
            for n in graph[node]:
                queue.append((n, path + [n]))
        return res