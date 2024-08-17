class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        start = None
        keys_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    start = (i, j)
                if grid[i][j].islower():
                    keys_count += 1
        
        def inbound(x, y):
            return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        
        que = deque()
        que.append((start[0], start[1], 0))

        visited = set()
        visited.add((start[0], start[1], 0))

        steps = 0

        while que:
            size = len(que)

            for _ in range(size):
                x, y, keys_mask = que.popleft()

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if inbound(new_x, new_y):
                        cell = grid[new_x][new_y]

                        if cell == '#':
                            continue

                        new_keys_mask = keys_mask
                        if cell.islower():
                            new_keys_mask |= (1 << (ord(cell) - ord('a')))

                        if cell.isupper() and not (keys_mask & (1 << (ord(cell) - ord('A')))):
                            continue

                        if new_keys_mask == (1 << keys_count) - 1:
                            return steps + 1

                        if (new_x, new_y, new_keys_mask) not in visited:
                            visited.add((new_x, new_y, new_keys_mask))
                            que.append((new_x, new_y, new_keys_mask))

            steps += 1
        
        return -1