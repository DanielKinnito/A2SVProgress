class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
            Make a 2D prefix matrix 
            make a map to keep count of the sums
            check against the map to add on the final count
            update the map accordingly
        """
        count = 0
        row = len(matrix)
        col = len(matrix[0])

        prefix_array = []
        for _ in range(row):
            prefix_array.append([0] * col)
        
        prefix_array[0][0] = matrix[0][0]
 
        for i in range(1, col) :
            prefix_array[0][i] = (prefix_array[0][i - 1] + matrix[0][i])
        for i in range(0, row) :
            prefix_array[i][0] = (prefix_array[i - 1][0] + matrix[i][0])
        
        for i in range(1, row) :
            for j in range(1, col) :
                prefix_array[i][j] = (prefix_array[i - 1][j] + prefix_array[i][j - 1] - prefix_array[i - 1][j - 1] + matrix[i][j])
        answer = 0
        for i in range(row):
            for j in range(i, row):
                count_map = {0: 1}
                for k in range(col):
                    cur_sum = prefix_array[j][k]
                    if i > 0:
                        cur_sum -= prefix_array[i-1][k]
                    
                    diff = cur_sum - target
                    if diff in count_map:
                        answer += count_map[diff]
                    if cur_sum in count_map:                      
                        count_map[cur_sum] += 1
                    else:
                        count_map[cur_sum] = 1

        return answer