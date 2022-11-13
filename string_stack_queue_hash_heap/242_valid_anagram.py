class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict()
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in t:
            if dic.get(c, 0) == 0:
                return False
            dic[c] -= 1
            if dic[c] == 0:
                del dic[c]

        if len(dic) == 0:
            return True
        else:
            return False
