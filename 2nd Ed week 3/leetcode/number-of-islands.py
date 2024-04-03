class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def inbound(node):
            return 0 <= node[0] < height and 0 <= node[1] < width

        def dfs(row, col):
            if not inbound((row, col)) or grid[row][col] == '0':
                return False
            
            # instead of keeping a visited set, we can turn islands into waters
            grid[row][col] = '0'

            for direc in directions:
                check_x, check_y = direc
                new_row, new_col = row + check_x, col + check_y
                
                dfs(new_row, new_col)

            return True

        answer = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == '1':
                    if dfs(row, col):
                        answer += 1
        
        return answer