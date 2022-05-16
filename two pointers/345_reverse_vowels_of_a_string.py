class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s)-1
        vowels = ('aeiouAEIOU')
        while left <= right:
            while left <= right and s[left] not in vowels:
                left += 1
            while left <= right and s[right] not in vowels:
                right -= 1
            if left > right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
