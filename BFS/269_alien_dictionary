class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        indegree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""

        zero = deque(c for c in indegree if indegree[c]==0)
        res = []

        while zero:
            word = zero.popleft()
            res.append(word)
            for c in graph[word]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    zero.append(c)

        if len(indegree) == len(res):
            return ''.join(res)

        return ""