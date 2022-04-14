# https://leetcode.com/discuss/interview-question/372434
def unique_pairs(nums, target):
    # hash (O(N))
    ans, comp = set(), set()
    for n in nums:
        c = target - n
        if c in comp:
            res = (n, c) if n > c else (c, n)
            if res not in ans:
                ans.add(res)
        comp.add(n)
    return len(ans)

    # If smaller space then use sort and two pointers
