class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        directions = [
            [0, 1], [0, -1],
            [1, 0], [-1, 0]
        ]
        
        visited = set()
        def bfs(x, y):
            area = 0
            visited.add((x, y))

            que = deque()
            que.append((x, y))

            while que:
                x, y = que.popleft()
                area += 1

                for dx, dy in directions:
                    tx, ty = x + dx, y + dy

                    if inbound(tx, ty) and (tx, ty) not in visited and grid[tx][ty] == 1:
                        que.append((tx, ty))
                        visited.add((tx, ty))
            
            return area

        answer = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    answer = max(answer, bfs(i, j))
        
        return answer