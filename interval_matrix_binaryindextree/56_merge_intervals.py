class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                result.append(current)
        return result


        # intervals.sort(key = lambda x: x[0])
        # merged = []
        # for i in intervals:
        #     if not merged or merged[-1][1] < i[0]:
        #         merged.append(i)
        #     else:
        #         merged[-1][1] = max(i[1], merged[-1][1])
        # return merged
