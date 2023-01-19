class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(s, left, right):
            if len(s) == 2*n:
                res.append(s)
            if left < n:
                helper(s+'(', left+1, right)
            if right < left:
                helper(s+')', left, right+1)
        helper('', 0, 0)
        return res