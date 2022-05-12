class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        output = []
        for i in range(len(intervals)):
            if intervals[i][0] < newInterval[0]:
                output.append(intervals[i])
            else:
                break
        index = i

        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newInterval[1])

        while index < len(intervals):
            if intervals[index][0] > output[-1][1]:
                output.append(intervals[index])
            else:
                output[-1][1] = max(output[-1][1], intervals[index][1])
            index += 1

        return output
