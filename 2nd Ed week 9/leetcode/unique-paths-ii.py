class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dp(x, y):
            if x == n-1 and y == m-1:
                return 1 if obstacleGrid[x][y] == 0 else 0
            if x >= n or y >= m:
                return 0

            if (x, y) not in memo:
                down, right = 0, 0
                if obstacleGrid[x][y] != 1:
                    down = dp(x + 1, y)
                    right = dp(x, y + 1)

                memo[(x, y)] = down + right
            
            return memo[(x, y)]
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        return dp(0, 0)