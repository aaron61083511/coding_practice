class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        
        graph = defaultdict(set)
        for i in connections:
            graph[i[0]].add((i[1], i[2]))
            graph[i[1]].add((i[0], i[2]))

        visited = set()
        queue = [(0, 1)]
        # heapq will use the first element to heapify
        while queue:
            d, node = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                res += d
            for nei in graph[node]:
                if nei[0] not in visited:
                    heapq.heappush(queue, (nei[1], nei[0]))

        return -1 if len(visited) != n else res