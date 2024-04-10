class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        ans = 0
        countFresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    countFresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if countFresh == 0:
            return 0

        while q:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
                        countFresh -= 1

        return ans - 1 if countFresh == 0 else -1