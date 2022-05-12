class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[0])
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        n = len(intervals)
        result = counter = p1 = p2 = 0

        while p1 < n and p2 < n:
            if start[p1] < end[p2]:
                counter += 1
                p1 += 1
            else:
                counter -= 1
                p2 += 1

            result = max(result, counter)

        return result
