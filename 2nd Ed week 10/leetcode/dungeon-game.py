class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        dp[n][m-1] = dp[n-1][m] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                min_health = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health - dungeon[i][j])
        
        return dp[0][0]