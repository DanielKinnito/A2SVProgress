class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height, width = len(board), len(board[0])

        def inbound(x, y):
            return (0 <= x < height) and (0 <= y < width)

        directions = [
            [0, 1], [0, -1],
            [1, 0], [-1, 0]
        ]

        visited = set()
        def dfs(row, col):
            visited.add((row, col))
            stack = [(row, col)]

            while stack:
                row, col = stack.pop()
                board[row][col] = 'S'

                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy

                    if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        if board[new_row][new_col] == 'O':
                            stack.append((new_row, new_col))
        
        for i in range(width):
            if board[0][i] == 'O':
                dfs(0, i)
            
            if board[height - 1][i] == 'O':
                dfs(height - 1, i)
            
        for i in range(height):
            if board[i][0] == 'O':
                dfs(i, 0)            
            
            if board[i][width - 1] == 'O':
                dfs(i, width - 1)
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'S':
                    board[i][j] = 'O'