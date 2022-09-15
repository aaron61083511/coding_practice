# https://www.lintcode.com/problem/127/description
# input: graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
# output: [0, 1, 2, 3, 4, 5]

# Explanation: https://www.youtube.com/watch?v=ddTC4Zovtbc
# BFS explanation: https://www.youtube.com/watch?v=cIBFEhD77b4&ab_channel=WilliamFiset

# Solution: https://www.lintcode.com/problem/127/solution/56967

# DFS
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
class Solution_dfs:
    def topSort(self, graph):
        self.visited = {}
        self.result = []
        if not graph:
            return

        for vertex in graph:
            if vertex in self.visited:
                continue
            self.dfs(vertex)

        return self.result[::-1]

    def dfs(self, vertex):
        for neighbor in vertex.neighbors:
            if neighbor in self.visited:
                continue
            self.dfs(neighbor)
        self.visited.add(vertex)
        self.result.append(vertex)

class Solution_bfs:
    def topSort(self, graph):
        # record the in-degree
        node_info = dict()
        for vertex in graph:
            for neighbor in vertex.neighbors:
                node_info[neighbor] = node_info.get(neighbor, 0) + 1

        # push record that has in-degree = 0 into queue
        zero_queue = []
        for vertex in graph:
            if node_info.get(vertex, 0) == 0:
                zero_queue.append(vertex)
        # clearer code:
        # zero_queue = [v for v in graph if indegree[v] == 0]

        # BFS
        result = []
        while len(zero_queue):
            vertex = zero_queue.pop(0)
            result.append(vertex)
            for neighbor in vertex.neighbors:
                node_info[neighbor] -= 1
                if node_info[neighbor] == 0:
                    zero_queue.append(neighbor)
        return result
