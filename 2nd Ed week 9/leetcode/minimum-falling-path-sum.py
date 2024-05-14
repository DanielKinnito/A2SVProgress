class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dp(x, y):
            if x == n - 1 and 0 <= y < n:
                return matrix[x][y]
            if y < 0 or y >= n:
                return float('inf')
           
            if (x, y) not in memo:
                left_diagonal = dp(x + 1, y - 1)
                right_diagonal = dp(x + 1, y + 1)
                down = dp(x + 1, y)
                                
                memo[(x, y)] = min(down, left_diagonal, right_diagonal) + matrix[x][y]
            
            return memo[(x, y)]
        
        n = len(matrix)
        memo = {}
        answer = float('inf')
        for i in range(n):
            answer = min(answer, dp(0, i))
        
        return answer