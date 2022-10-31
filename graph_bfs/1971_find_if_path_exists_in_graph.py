class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited = set()
        queue = deque([destination])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == source:
                    return True
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        return False