class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        # mp = {}
        # i = 0
        # ans = 0
        #
        # for j in range(n):
        #     if s[j] in mp:
        #         i = max(i, mp[s[j]])
        #     ans = max(ans, j-i+1)
        #     mp[s[j]] = j + 1
        #
        # return ans

        i, j, max_l = 0, 0, 0
        window = set()
        while j < len(s):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            max_l = max(max_l, len(window))
            j += 1
        return max_l
