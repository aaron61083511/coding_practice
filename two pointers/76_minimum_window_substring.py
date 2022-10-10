class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = {}
        i, j, start, end = 0, 0, -1, -1
        valid = 0
        
        if len(t) > len(s):
            return ''
        
        for char in t:
            need[char] = need.get(char, 0) + 1
        while j < len(s):
            if s[j] in need:
                window[s[j]] = window.get(s[j], 0) + 1
                if window[s[j]] == need[s[j]]:
                    valid += 1
            j += 1
            
            while valid == len(need):
                if start == -1 or j - i < end - start:
                    start = i
                    end = j
                if s[i] in need:
                    if window[s[i]] == need[s[i]]:
                        valid -= 1
                    window[s[i]] = window.get(s[i], 0) - 1
                i += 1
        
        return s[start: end]