class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [
            [-1, 0], [1, 0],
            [0, -1], [0, 1],
            [-1, -1], [1, 1],
            [-1, 1], [1, -1]
            ]
        visited = set()
        height = len(board)
        width = len(board[0])

        def inbound(check_row, check_col):
            return (0 <= check_row < height) and (0 <= check_col < width)

        def countMine(row, col):
            count = 0

            for x, y in directions:
                new_row, new_col = row + x, col + y
                if inbound(new_row, new_col):
                    if board[new_row][new_col] == 'M':
                        count += 1
            return count
        
        def dfs(row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            visited.add((row, col))
            count = countMine(row, col)
            if count == 0:
                board[row][col] = 'B'
                for x, y in directions:
                    new_row, new_col = row + x, col + y
                    if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        dfs(new_row, new_col)
            else:
                board[row][col] = str(count)
           

        r, c = click
        dfs(r, c)
        return board