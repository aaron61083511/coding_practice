class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        need = {}
        i, j = 0, 0
        valid = 0
        
        if len(s1) > len(s2):
            return ''
        
        for char in s1:
            need[char] = need.get(char, 0) + 1
            
        while j < len(s2):
            if s2[j] in need:
                window[s2[j]] = window.get(s2[j], 0) + 1
                if window[s2[j]] == need[s2[j]]:
                    valid += 1
            j += 1
            
            while j - i >= len(s1):
                if valid == len(need):
                    return True
                
                if s2[i] in need:
                    if window[s2[i]] == need[s2[i]]:
                        valid -= 1
                    window[s2[i]] = window.get(s2[i], 0) - 1
                i += 1
        
        return False