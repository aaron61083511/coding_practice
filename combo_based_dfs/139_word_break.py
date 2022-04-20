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
