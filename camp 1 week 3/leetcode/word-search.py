class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_row = len(board)
        max_col = len(board[0])

        index_set = set()

        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or col < 0 or row >= max_row or col >= max_col or word[index]!=board[row][col]:
                return False
            
            if (row, col) in index_set:
                return False

            index_set.add((row, col))
            answer = (backtrack(row + 1, col ,index + 1) or backtrack(row, col + 1 , index + 1) or backtrack(row - 1, col, index + 1) or backtrack(row, col - 1, index + 1))
            index_set.remove((row, col))
            
            return answer

        
        for i in range(max_row):
            for j in range(max_col):
                if backtrack(i, j, 0):
                    return True
        
        return False