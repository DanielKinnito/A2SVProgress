class DSU:
    def __init__(self, length):
        self.parent = {i:i for i in range(length)}
        self.size = [1 for i in range(length)]
    
    def find(self, x):
        while x != self.parent[x]:
            temp = self.parent[self.parent[x]]
            x = temp
            
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_y] > self.size[root_x]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u, v)
        
        print(dsu.parent)
        groups = defaultdict(int)
        for node in dsu.parent.values():
            root = dsu.find(node)
            groups[root] += 1
        
        if len(groups) == 1:
            return 0

        answer = 0
        group_sizes = list(groups.values())
        total_nodes = sum(group_sizes)
        for size in group_sizes:
            total_nodes -= size
            answer += size * total_nodes

        return answer