"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph_bfs(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited, queue = dict(), [node]
        visited[node] = Node(node.val, [])
        while queue:
            neighbor = queue.pop(0)
            for n in neighbor.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    queue.append(n)
                visited[neighbor].neighbors.append(visited[n])
        return visited[node]

    def cloneGraph_dfs_recursive(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = dict()
        def helper(node):
            if node in visited:
                return visited[node]
            clone_node = Node(node.val, [])
            visited[node] = clone_node
            if node.neighbors is not None:
                for n in node.neighbors:
                    clone_node.neighbors.append(helper(n))
            # or
            # clone_node.neighbors = [helper(n) for n in node.neighbors]
            return clone_node
        return helper(node)

    def cloneGraph_dfs_iterative(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited, stack = dict(), [node]
        visited[node] = Node(node.val, [])
        while stack:
            neighbor = stack.pop()
            for n in neighbor.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    stack.append(n)
                visited[neighbor].neighbors.append(visited[n])
        return visited[node]
