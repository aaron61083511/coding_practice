class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = {}
        need = {}
        i, j = 0, 0
        valid = 0
        res = []
        
        if len(p) > len(s):
            return ''
        
        for char in p:
            need[char] = need.get(char, 0) + 1
            
        while j < len(s):
            if s[j] in need:
                window[s[j]] = window.get(s[j], 0) + 1
                if window[s[j]] == need[s[j]]:
                    valid += 1
            j += 1
            
            while j - i >= len(p):
                if valid == len(need):
                    res.append(i)
                
                if s[i] in need:
                    if window[s[i]] == need[s[i]]:
                        valid -= 1
                    window[s[i]] = window.get(s[i], 0) - 1
                i += 1
        
        return res