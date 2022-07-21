class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mp = {}
        i = 0
        ans = 0

        for j in range(n):
            if s[j] in mp:
                i = max(i, mp[s[j]])
            ans = max(ans, j-i+1)
            mp[s[j]] = j + 1

        return ans
