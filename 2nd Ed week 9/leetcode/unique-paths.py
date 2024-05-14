class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(x, y):
            if x == n-1 and y == m-1:
                return 1
            if x >= n or y >= m:
                return 0

            if (x, y) not in memo:
                down = dp(x + 1, y)
                right = dp(x, y + 1)
                
                memo[(x, y)] = down + right
            
            return memo[(x, y)]
        
        memo = {}
        return dp(0, 0)