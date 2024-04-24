class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = len(edges)
        parent = {i: i for i in range(1, nodes + 1)}
        size = [1] * (nodes + 1)
    
        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            return x
        def union(x, y, answer):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    parent[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    parent[rootX] = rootY
                    size[rootY] += size[rootX]
            else:
                answer.append([x, y])

        answer = []
        for edge in edges:
            x, y = edge
            union(x, y, answer)
        return answer[-1]