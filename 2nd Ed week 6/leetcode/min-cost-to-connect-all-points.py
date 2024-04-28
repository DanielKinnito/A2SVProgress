class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        edges = []

        for i in range(length):
            for j in range(i + 1, length):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        uf = UnionFind(length)
        min_cost = 0
        num_edges = 0

        for cost, u, v in sorted(edges):
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                min_cost += cost
                num_edges += 1
                if num_edges == length - 1:
                    break

        return min_cost