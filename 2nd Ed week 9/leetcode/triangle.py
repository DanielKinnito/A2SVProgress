class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dp(x, y):
            if x == n - 1:
                return triangle[x][y]
            if x >= n or y >= len(triangle[x]):
                return float('inf')

            if (x, y) not in memo:
                diaonal = dp(x + 1, y + 1)
                down = dp(x + 1, y)
                                
                memo[(x, y)] = min(down, diaonal) + triangle[x][y]
            
            return memo[(x, y)]
        
        n = len(triangle)
        memo = {}
        return dp(0, 0)