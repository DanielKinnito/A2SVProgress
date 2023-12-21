class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse the order of each row
        n = len(matrix[0])
        for row in matrix:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = row[n - 1 - i], row[i]