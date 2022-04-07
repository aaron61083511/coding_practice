graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# Use loop
def dfs(graph1, node):
    visited, stack = set(), [node]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph1[vertex] - visited)
    return visited

# use recursive
def dfs1(graph1, node, visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    for next in graph1[node] - visited:
        dfs1(graph1, next, visited)
    return visited


print(dfs(graph, 'A'))
print(dfs1(graph, 'A'))
