class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        if digits is None or len(digits) == 0:
            return result

        def backtracking(index=0, path=[]):
            if len(path) == len(digits):
                result.append(''.join(path))
                return
            options = mapping[digits[index]]
            for letter in options:
                path.append(letter)
                backtracking(index+1, path)
                path.pop()

        backtracking()
        return result
