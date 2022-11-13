class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word = set(wordDict)
        queue = deque()
        visited = set()

        queue.append(0)
        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word:
                    queue.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False

    def wordBreak_II(self, s: str, wordDict: List[str]) -> bool:
        queue = deque([s])
        visited = set()

        while queue:
            node = queue.popleft()
            for i in wordDict:
                if node[:len(i)] == i:
                    if len(node[len(i):]) == 0:
                        return True
                    if node[len(i):] not in visited:
                        queue.append(node[len(i):])
                        visited.add(node[len(i):])

        return False