class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dp(x, y):
            if x == n-1 and y == m-1:
                return grid[x][y]
            if x >= n or y >= m:
                return float('inf')

            if (x, y) not in memo:
                down = dp(x + 1, y) + grid[x][y]
                right = dp(x, y + 1) + grid[x][y]
                
                memo[(x, y)] = min(down, right)
            
            return memo[(x, y)]
        n, m = len(grid), len(grid[0])
        memo = {}
        return dp(0, 0)