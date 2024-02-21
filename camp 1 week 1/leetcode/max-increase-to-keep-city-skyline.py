class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        row_comp = []
        for row in grid:
            row_comp.append(max(row))
        col_comp = []
        for j in range(col_len):
            top = 0
            for i in range(row_len):
                top = max(top, grid[i][j])
            col_comp.append(top)
        
        answer = 0

        for i in range(row_len):
            for j in range(col_len):
                answer += min(row_comp[i], col_comp[j]) - grid[i][j]
        
        return answer