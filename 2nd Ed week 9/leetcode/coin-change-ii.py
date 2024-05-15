class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp(idx, curr):
            if idx >= n or curr < 0:
                return 0
            
            if curr == 0:
                return 1
            
            if (idx, curr) not in memo:
                take = dp(idx, curr - coins[idx])
                leave = dp(idx + 1, curr)
                
                memo[(idx, curr)] = take + leave
            
            return memo[(idx, curr)]
        memo = {}
        n = len(coins)
        return dp(0, amount)