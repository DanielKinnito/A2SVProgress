class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(idx, holding):
            if idx >= len(prices):
                return 0
            
            if (idx, holding) not in memo:
                if holding:
                    memo[(idx, holding)] = max(dp(idx + 1, holding), dp(idx + 2, False) + prices[idx])
                else:
                    memo[(idx, holding)] = max(dp(idx + 1, holding), dp(idx + 1, True) - prices[idx])
            
            return memo[(idx, holding)]
        
        memo = {}
        return dp(0, False)