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

        # ans = []
        # def backtrack(S = [], left = 0, right = 0):
        #     if len(S) == 2 * n:
        #         ans.append("".join(S))
        #         return
        #     if left < n:
        #         S.append("(")
        #         backtrack(S, left+1, right)
        #         S.pop()
        #     if right < left:
        #         S.append(")")
        #         backtrack(S, left, right+1)
        #         S.pop()
        # backtrack()
        # return ans