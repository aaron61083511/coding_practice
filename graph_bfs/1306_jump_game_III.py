class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = defaultdict(list)
        queue = deque([])
        
        for i in range(len(arr)):
            graph[i+arr[i]].append(i)
            if i-arr[i] >= 0:
                graph[i-arr[i]].append(i)
            if arr[i] == 0:
                queue.append(i)
        
        visited = set()
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor  == start:
                        return True
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return False