class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        def helper(N):
            if N in cache:
                return cache[N]
            if N < 2:
                result = N
            else:
                result = helper(N-1) + helper(N-2)
            cache[N] = result
            return result
        helper(N)
        return cache[N]
    
    def fib_II(self, N: int) -> int:
        if N <= 1:
            return N
        
        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]

    def fib_III(self, N: int) -> int:
        if (N <= 1):
            return N

        current = 0
        prev1 = 1
        prev2 = 0

        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current