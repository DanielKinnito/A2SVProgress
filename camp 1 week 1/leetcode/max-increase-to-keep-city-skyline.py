class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_comp = []
        for row in grid:
            row_comp.append(max(row))
        col_comp = []
        for j in range(len(grid[0])):
            top = 0
            for i in range(len(grid)):
                top = max(top, grid[i][j])
            col_comp.append(top)
        
        answer = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer += min(row_comp[i], col_comp[j]) - grid[i][j]
        
        return answer