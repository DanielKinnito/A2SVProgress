class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        height, width = len(grid), len(grid[0])
        
        answer = 0
        count = 0
        que = deque()

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    que.append((i, j))

        if count == 0:
            return 0

        while que:
            answer += 1
            for _ in range(len(que)):
                i, j = que.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < height and 0 <= y < width and grid[x][y] == 1:
                        grid[x][y] = 2
                        que.append((x, y))
                        count -= 1

        return answer - 1 if count == 0 else -1