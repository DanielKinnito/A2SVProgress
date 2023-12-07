class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        while matrix:
            # Traverse from left to right
            result += matrix.pop(0)

            if matrix and matrix[0]:
                # Traverse from top to bottom
                for row in matrix:
                    result.append(row.pop())

            if matrix:
                # Traverse from right to left
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                # Traverse from bottom to top
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result