class UnionFind:
    def __init__(self, h, w):
        self.parent = {(i, j): (i, j) for i in range(h) for j in range(w)}
        self.rank = {(i, j): 0 for i in range(h) for j in range(w)}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        uf = UnionFind(height, width)

        directions = [
            (0, 1), (0, -1),
            (1, 0), (-1, 0)
        ]
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] > 0:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < height and 0 <= nj < width and grid[ni][nj] > 0:
                            uf.union((i, j), (ni, nj))
        
        fish_count = defaultdict(int)
        for i in range(height):
            for j in range(width):
                root = uf.find((i, j))
                fish_count[root] += grid[i][j]
        
        max_fish = 0
        for count in fish_count.values():
            max_fish = max(max_fish, count)

        return max_fish