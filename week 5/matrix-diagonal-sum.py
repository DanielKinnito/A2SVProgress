class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        main_diagonal = {}
        reversed_diagonal = {}

        for i in range(n):
            for j in range(m):
                left = i + j
                right = i - j
                
                if right == 0:
                    main_diagonal[right] = main_diagonal.get(right, 0) + mat[i][j]
                
                if left == n - 1:
                    reversed_diagonal[left] = reversed_diagonal.get(left, 0) + mat[i][j]

        result = 0
        for key in main_diagonal:
            result += main_diagonal[key]
        
        for key in reversed_diagonal:
            result += reversed_diagonal[key]

        # Subtract the middle element if the matrix size is odd
        if n % 2 == 1:
            result -= mat[n // 2][n // 2]

        return result