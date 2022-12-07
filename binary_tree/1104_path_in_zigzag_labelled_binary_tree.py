class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        for i in range(21):
            if 2**i > label:
                break
        level = i - 1
        res.append(label)
        while level > 0:
            label = pow(2, level) - 1 - (label - pow(2, level)) // 2
            res.append(label)
            level -= 1
        
        return res[::-1]