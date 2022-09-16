# https://leetcode.com/problems/course-schedule-ii/discuss/266867/Python-Topological-Sort-BFS-and-DFS-(reserve-order)
# https://leetcode.com/problems/course-schedule-ii/discuss/762346/Python-BFS-beats-98-with-Detailed-Explanation-and-Comments!

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_info = {i: 0 for i in range(numCourses)}
        graph = collections.defaultdict(set)
        for course in prerequisites:
            graph[course[1]].add(course[0])

        for course in graph:
            for c in graph[course]:
                course_info[c] += 1
        zero = deque(c for c in course_info if course_info[c] == 0)
        size = len(zero)

        result = []
        while zero:
            course = zero.popleft()
            result.append(course)
            for c in graph[course]:
                course_info[c] -= 1
                if course_info[c] == 0:
                    size += 1
                    zero.append(c)
        if size == numCourses:
            return result

        return []
