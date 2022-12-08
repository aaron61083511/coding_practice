# Test Case1:
# n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
# Output: 3

# Test Case2:
# n = 10, headID = 3, manager = [8,9,8,-1,7,1,2,0,3,0], informTime = [224,943,160,909,0,0,0,643,867,722]
# Output: 3665

# Test Case3:
# n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
# Output: 21
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if i not in graph:
                graph[i]=[]
            if manager[i] != -1:
                graph[manager[i]].append(i)
        queue = deque([(headID, informTime[headID])])
        max_time = informTime[headID]
        while queue:
            size = len(queue)
            for _ in range(size):
                node, time = queue.popleft()
                if graph[node]:
                    for s in graph[node]:
                        queue.append((s, time + informTime[s]))
                        max_time = max(max_time, time + informTime[s])
        return max_time