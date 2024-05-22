class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(idx, transactions, holding):
            if idx >= len(prices) or transactions == 2:
                return 0
            
            if (idx, transactions, holding) not in memo:
                do_nothing = dp(idx + 1, transactions, holding)
                if holding:
                    sell = prices[idx] + dp(idx + 1, transactions + 1, False)
                    memo[(idx, transactions, holding)] = max(do_nothing, sell)
                else:
                    buy = -prices[idx] + dp(idx + 1, transactions, True)
                    memo[(idx, transactions, holding)] = max(do_nothing, buy)
            
            return memo[(idx, transactions, holding)]
        
        memo = {}
        return dp(0, 0, False)