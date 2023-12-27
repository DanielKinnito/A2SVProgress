class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        1 - setup grids for all directions, including our main grid
                and populate them with 0s to help checking later
        2 - according to the coords given, populate the main grid
        3 - populate the direction grids with G or W as long as we meet the same in the main grid
        4 - Count one for every cell in main that is 0 and corresponding cells in the other directional grids that have either W or G.
        5 - Return the count
        """
        answer = 0

        # grids
        grid = [[0] * n for _ in range(m)]
        west = [[0] * n for _ in range(m)]
        east = [[0] * n for _ in range(m)]
        north = [[0] * n for _ in range(m)]
        south = [[0] * n for _ in range(m)]

        # Populating the grid with guards and walls
        for row, col in guards:
            grid[row][col] = 'G'
        for row, col in walls:
            grid[row][col] = 'W'
        
        # Row-wise directional check for every cardinal direction
        for i in range(m):
            # East grid check
            last_cell = 0
            for j in range(n): # Check forwards for East
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    last_cell = grid[i][j]
                
                else:
                    east[i][j] = last_cell
            
            # set the last cell back to 0 for the other direction
            last_cell = 0
            # West grid check
            for j in range(n - 1, -1, -1): # Check backwards for West
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    last_cell = grid[i][j]
                
                else:
                    west[i][j] = last_cell
        
        # Check column-wise for the other two directions i.e. use n instead of m
        for i in range(n):
            # North grid check
            last_cell = 0
            for j in range(m):
                if grid[j][i] == 'G' or grid[j][i] == 'W': # swap i an j to not go out of index and to insert it row-wise
                    last_cell = grid[j][i]
                
                else:
                    north[j][i] = last_cell
            
            # Set last_cell back to 0 for the next direction
            last_cell = 0
            # South grid check
            for j in range(m - 1, -1, -1):
                if grid[j][i] == 'G' or grid[j][i] == 'W':# swap i an j to not go out of index and to insert it row-wise
                    last_cell = grid[j][i]
                
                else:
                    south[j][i] = last_cell
        
        # Count unguarded cells i.e. no guards/walls in every direction and is 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and east[i][j] != 'G' and west[i][j] != 'G' and north[i][j] != 'G' and south[i][j] != 'G':
                    answer += 1
        
        return answer