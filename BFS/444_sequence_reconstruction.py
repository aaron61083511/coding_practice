class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = {s: 0 for sequence in sequences for s in sequence}
        for sequence in sequences:
            for i in range(len(sequence)-1):
                graph[sequence[i]].append(sequence[i+1])
                indegree[sequence[i+1]] += 1

        zero = deque(c for c in indegree if indegree[c] == 0)
        res = []
        while zero:
            if len(zero) != 1:
                return False
            sequence = zero.popleft()
            res.append(sequence)
            for s in graph[sequence]:
                indegree[s] -= 1
                if indegree[s] == 0:
                    zero.append(s)

        if res == nums:
            return True

        return False