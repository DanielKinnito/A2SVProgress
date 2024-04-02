class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)

        def inbound(node):
            return (0 <= node[0] < height) and (0 <= node[1] < width)
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        perimeter = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if not inbound((x, y)) or grid[x][y] == 0:
                            perimeter += 1
        
        return perimeter