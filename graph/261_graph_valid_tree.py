class Solution:
    def validTree_dfs_recursive(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False
    
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)
        
        dfs(0)
        return len(seen) == n


    def validTree_dfs_iterative(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False
    
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbour in adj_list[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)

        return len(seen) == n