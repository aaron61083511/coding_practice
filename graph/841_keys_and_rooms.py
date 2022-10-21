class Solution:
    def canVisitAllRooms_dfs_iterative(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if i not in visited:
                    visited.add(i)
                    stack.append(i)
                    
        return len(visited) == len(rooms)
    
    def canVisitAllRooms_dfs_recursive(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in rooms[node]:
                dfs(i)
        dfs(0)
        return len(visited) == len(rooms)