class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def f(n):
            if n <= 1:
                return n
            if n not in memo:
                memo[n] = f(n - 1) + f(n - 2)
            return memo[n]
        return f(n)