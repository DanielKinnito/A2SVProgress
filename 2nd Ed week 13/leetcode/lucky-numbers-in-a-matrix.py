class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        minimums = []
        for i in range(n):
            minimums.append(min(matrix[i]))

        maximums = []
        for j in range(m):
            cur_max = matrix[0][j]
            for i in range(1, n):
                cur_max = max(cur_max, matrix[i][j])
            
            maximums.append(cur_max)
        
        answer = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == minimums[i] and matrix[i][j] == maximums[j]:
                    answer.append(matrix[i][j])
        
        return answer