class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        
        visited = set((0, 0))
        que = deque()
        que.append((0, 0))

        height = len(grid)
        width = len(grid[0])
        destination = (height - 1, width - 1)

        def inbound(x, y):
            return (0 <= x < height) and (0 <= y < width)

        directions = [[1, 0], [1, 1], [0, 1], [1, -1], [-1, 1], [-1, 0], [0, -1], [-1, -1]]
        level = 1

        while que:
            size = len(que)
            for _ in range(size):
                row, col = que.popleft()
                if (row, col) == destination:
                    return level

                for direc in directions:
                    new_row = row + direc[0]
                    new_col = col + direc[1]

                    if (new_row, new_col) not in visited and inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                        visited.add((new_row, new_col))
                        que.append((new_row, new_col))

            level += 1
        return -1