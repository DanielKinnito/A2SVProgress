class DSU:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[y] = root_x
            
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        uf = DSU(n)
        for u, v in edges:
            uf.union(u, v)
        
        champions = set()
        for i in range(n):
            champions.add(uf.find(i))

        if len(champions) == 1:
            return list(champions)[-1]
        else:
            return -1