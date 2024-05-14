class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def dp(x, y):
            if x >= n or y >= m:
                return 0
           
            if (x, y) not in memo:
                if matrix[x][y] == '1':
                    memo[(x, y)] = min(dp(x + 1, y), dp(x, y + 1), dp(x + 1, y + 1)) + 1
                else:
                    memo[(x, y)] = 0
            
            return memo[(x, y)]
        
        n, m = len(matrix), len(matrix[0])
        memo = {}
        
        answer = 0
        for i in range(n):
            for j in range(m):
                answer = max(answer, dp(i, j))
        
        return answer ** 2