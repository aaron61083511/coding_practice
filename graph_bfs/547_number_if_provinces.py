class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res