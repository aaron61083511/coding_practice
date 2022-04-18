from collections import deque
# def canFinish_dfs(numCourses, prerequisites):
def canFinish_bfs(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1
    bfs_queue = deque(v for v in range(numCourses) if indegree[v] == 0)
    # here bfs_queue is the same as visited
    size = len(bfs_queue)
    while bfs_queue:
        vertex = bfs_queue.popleft()
        for course in graph[vertex]:
            indegree[course] -= 1
            if indegree[course] == 0:
                size += 1
                bfs_queue.append(course)
    return size == numCourses


numCourses = 2
prerequisites = [[1,0]]
print(canFinish_bfs(numCourses, prerequisites))


# another one with clean explanation
# def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
#
#         then = [[] for _ in range(n)]
#         # or then = collections.defaultdict(list), identical
#         need = [0 for _ in range(n)]
#
#         for [a,b] in prerequisites:
#             # for every prerequisite b, it's needed before take it's value in dict
#             then[b].append(a)
#             # number of courses need to take before take a
#             need[a] += 1
#
#         # index of courses that can be taken without any other prerequisites
#         bfs = [i for i in range(n) if not need[i]]
#
#         # these courses become the prerequisites of other courses
#         for pre in bfs:
#             # loop through the courses that need it as a prerequisite
#             for course in then[pre]:
#                 # decrement it in 'need'
#                 need[course] -= 1
#                 # if there is no other prerequisite needed
#                 if not need[course]:
#                     # append it to bfs, for further searching
#                     bfs.append(course)
#
#         # if every course, as a node, is visited, then it's stored in bfs
#         # so return the length of bfs equaling to n
#         return len(bfs) == n
