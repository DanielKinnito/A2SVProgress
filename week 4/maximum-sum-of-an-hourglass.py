class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_sum = 0

        for i in range(row - 2):
            for j in range(col - 2):
                hour_glass = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]

                max_sum = max(max_sum, hour_glass)

        return max_sum        