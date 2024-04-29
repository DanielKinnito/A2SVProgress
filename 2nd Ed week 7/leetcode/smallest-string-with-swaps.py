class UnionFind:
    def __init__(self, n, string):
        self.parent = {i: i for i in range(n)}
        self.rank = [0 for i in range(n)]
    
    def find(self, x):
        if self.parent[x] == x:
            return x
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n, s)
        
        for a, b in pairs:
            uf.union(a, b)
        
        component_map = defaultdict(list)
        
        for i in range(n):
            root = uf.find(i)
            component_map[root].append(i)
        
        answer = list(s)
        for indices in component_map.values():
            chars = sorted(answer[idx] for idx in indices)
            for idx, char in zip(sorted(indices), chars):
                answer[idx] = char
        
        return ''.join(answer)