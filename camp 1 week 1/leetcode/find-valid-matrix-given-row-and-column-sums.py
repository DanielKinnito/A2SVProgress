class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        numRow = len(rowSum)
        numCol = len(colSum)

        grid = []
        for _ in range(numRow):
            grid.append([0]*numCol)
        
        for i in range(numRow):
            for j in range(numCol):
                if rowSum[i] <= colSum[j]:
                    grid[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] -= rowSum[i]
                else:
                    grid[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] -= colSum[j]
        
        return grid