class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for temp_am in range(1, amount + 1):
                dp[i][temp_am] = dp[i - 1][temp_am]
                if temp_am >= coins[i - 1]:
                    dp[i][temp_am] += dp[i][temp_am - coins[i - 1]]

        return dp[n][amount]