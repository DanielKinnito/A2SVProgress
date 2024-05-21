class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]* i for i in range(1, n + 1)]

        for i in range(len(dp[-1])):
            dp[-1][i] = triangle[-1][i]

        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        
        return dp[0][0]