class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]* n for _ in range(m)]
        dp[-1][-1] = 1

        def helper(i, j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if (row, col) == (m - 1, n - 1):
                    continue
                dp[row][col] = helper(row + 1, col) + helper(row, col + 1)
        
        return dp[0][0]