class Solution:
    def countComponents_dfs_recursive(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
            
        return res
    
    def countComponents_dfs_iterative(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            res += 1
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        return res