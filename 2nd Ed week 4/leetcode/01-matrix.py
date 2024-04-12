from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        INF = float('inf')

        answer = [[INF] * n for _ in range(m)]

        def inbound(x, y):
            return (0 <= x < m) and (0 <= y < n)

        directions = [
            (0, 1), (0, -1),
            (1, 0), (-1, 0)
            ]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    queue.append((i, j))

        
        while queue:
            row, col = queue.popleft()
            
            for x, y in directions:
                new_row, new_col = row + x, col + y
                
                if inbound(new_row, new_col):
                    if answer[new_row][new_col] > answer[row][col] + 1:
                        
                        answer[new_row][new_col] = answer[row][col] + 1
                        queue.append((new_row, new_col))

        return answer