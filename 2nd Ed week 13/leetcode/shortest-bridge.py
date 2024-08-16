class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        def dfs(x, y, que):
            que.append((x, y))
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if inbound(new_x, new_y) and (new_x, new_y) not in visited and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y, que)

        visited = set()
        que = deque()
        
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j, que)
                    found = True
                    break
            if found:
                break

        steps = 0
        while que:
            size = len(que)
            for _ in range(size):
                x, y = que.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if inbound(new_x, new_y) and (new_x, new_y) not in visited:
                        if grid[new_x][new_y] == 1:
                            return steps
                        que.append((new_x, new_y))
                        visited.add((new_x, new_y))
            steps += 1
        
        return -1
