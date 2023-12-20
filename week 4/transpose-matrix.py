class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Create a new matrix with reversed dimensions
        transpose = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # Swap elements and transpose the matrix
                transpose[j][i] = matrix[i][j]

        return transpose