class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        def dp(num):
            if num < 4: return num
                
            if num not in memo:
                memo[num] = 0
                for i in range(1, num + 1):
                    memo[num] = max(memo[num], i * dp(num - i))
            
            return memo[num]
        
        memo = {}
        return dp(n)