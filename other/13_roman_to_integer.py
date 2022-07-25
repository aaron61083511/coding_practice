class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = dic[s[0]]
        for i in range(1, n):
            result += dic[s[i]]
            if s[i-1] == 'I' and s[i] in ['V', 'X']:
                result -= 2
            if s[i-1] == 'X' and s[i] in ['L', 'C']:
                result -= 20
            if s[i-1] == 'C' and s[i] in ['D', 'M']:
                result -= 200
        return result
