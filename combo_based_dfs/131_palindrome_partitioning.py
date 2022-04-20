class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispadlindrome(sub):
            l, r = 0, len(sub)-1
            while l <= r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True

        result = []
        def backtracking(s, path=[]):
            if not s:
                result.append(path[:])
                return
            for i in range(1, len(s)+1):
                if ispadlindrome(s[:i]):
                    path.append(s[:i])
                    backtracking(s[i:], path)
                    path.pop()

        backtracking(s)
        return result
