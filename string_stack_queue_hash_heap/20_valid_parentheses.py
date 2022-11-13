class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i not in mapping:
                stack.append(i)
            elif stack and stack[-1] == mapping[i]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
