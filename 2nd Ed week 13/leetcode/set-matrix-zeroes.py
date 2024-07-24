class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_zero = True
                    if j == 0:
                        col_zero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0