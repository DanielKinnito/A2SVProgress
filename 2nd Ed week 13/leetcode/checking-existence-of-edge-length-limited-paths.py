class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                self.rank[root_v] += 1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        answer = [False] * len(queries)
        temp = [[0] * 4 for _ in range(len(queries))]
        uf = UnionFind(n)

        for i in range(len(queries)):
            temp[i][0] = queries[i][0]
            temp[i][1] = queries[i][1]
            temp[i][2] = queries[i][2]
            temp[i][3] = i

        temp.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])

        i = 0
        for query in temp:
            while i < len(edgeList) and edgeList[i][2] < query[2]:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            
            if uf.find(query[0]) == uf.find(query[1]):
                answer[query[3]] = True

        return answer