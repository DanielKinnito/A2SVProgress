class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = 0
        visited = set()

        directions = [
            [0, 1], [0, -1],
            [1, 0], [-1, 0]    
        ]
        
        def in_bound(x, y, n, m):
            return 0 <= x < n and 0 <= y < m
        
        heap = [(0, (0, 0))]

        while heap:
            cost, cur_node = heappop(heap)
            x, y = cur_node
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))

            for i, j in directions:
                new_x = x + i
                new_y = y + j

                if in_bound(new_x, new_y, n, m):
                    weight = 0
                    if grid[new_x][new_y] == 1:
                        weight = 1
                    
                    if dist[new_x][new_y] > cost + weight:
                        dist[new_x][new_y] = cost + weight
                        heappush(heap, (dist[new_x][new_y], (new_x, new_y)))

        return dist[n-1][m-1]
