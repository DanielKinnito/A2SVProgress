class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        result = [0] * (row * col)
        
        direction = 1 # positive means left-bot to right-top
        current_row, current_col = 0, 0

        for i in range(row * col):
            result[i] = mat[current_row][current_col]
            current_row -= direction
            current_col += direction

            # Handle out-of-bounds cases
            if current_row == row: # adjusted back to the last row
                current_row = row - 1
                current_col += 2
                direction = -direction
            
            if current_col == col: # adjusted back to the last col
                current_col = col - 1
                current_row += 2
                direction = -direction
            
            if current_row < 0: # it is adjusted back to 0 row and direction reversed
                current_row = 0
                direction = -direction
            
            if current_col < 0: # it is adjusted back to the 0 col and direction reversed
                current_col = 0
                direction = -direction

        return result 