class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #two separate fors to go through first, the row, then the column.
        #check if there are duplicates using a dict
        row = len(board) # 9
        col = len(board[0]) # 9

        for i in range(row):
            row_dict = {}

            for j in range(col):
                if board[i][j].isdigit() and board[i][j] not in row_dict:
                    row_dict[board[i][j]] = j

                elif board[i][j].isdigit() and board[i][j] in row_dict:
                    return False
        
        for j in range(col):
            col_dict = {}

            for i in range(row):
                if board[i][j].isdigit() and board[i][j] not in col_dict:
                    col_dict[board[i][j]] = i

                elif board[i][j].isdigit() and board[i][j] in col_dict:
                    return False
        
        # Check 3x3 subgrids
        for i in range(0, row, 3):
            for j in range(0, col, 3):
                subgrid_dict = {}
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y].isdigit():
                            if board[i + x][j + y] not in subgrid_dict:
                                subgrid_dict[board[i + x][j + y]] = True
                            else:
                                return False

        return True


        # [[".",".",".",".","5",".",".","1","."],
        #  [".","4",".","3",".",".",".",".","."],
        #  [".",".",".",".",".","3",".",".","1"],
        #  ["8",".",".",".",".",".",".","2","."],
        #  [".",".","2",".","7",".",".",".","."],
        #  [".","1","5",".",".",".",".",".","."],
        #  [".",".",".",".",".","2",".",".","."],
        #  [".","2",".","9",".",".",".",".","."],
        #  [".",".","4",".",".",".",".",".","."]]