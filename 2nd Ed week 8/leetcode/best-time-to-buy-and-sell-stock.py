class Solution:
    def maxProfit(self, prices):
        def dp(idx, fl):
            if idx >= len(prices) - 1:
                if fl: return 0
                return prices[idx]
            
            if (idx, fl) not in memo:
                if fl: memo[((idx, fl))] = max(dp(idx + 1, fl), dp(idx + 1, not fl) - prices[idx])
                else: memo[(idx, fl)] = max(dp(idx + 1, fl), prices[idx])
            
            return memo[(idx, fl)]
        
        memo = {}
        return dp(0, True)