class UnionFind:
    def __init__(self, n):
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
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            current_meetings = []
            
            while i < len(meetings) and meetings[i][2] == time:
                current_meetings.append(meetings[i])
                i += 1
            
            for u, v, _ in current_meetings:
                uf.union(u, v)
            
            connected = set()
            for u, v, _ in current_meetings:
                if uf.find(u) == uf.find(0) or uf.find(v) == uf.find(0):
                    connected.add(u)
                    connected.add(v)
            
            for u, v, _ in current_meetings:
                if u not in connected:
                    uf.parent[u] = u
                if v not in connected:
                    uf.parent[v] = v
        
        answer = [i for i in range(n) if uf.find(i) == uf.find(0)]
        
        return answer