class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(20001)]
        rank = [0] * 20001

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x

        for i in range(n):
            for j in range(n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    x, y = stones[i][0], stones[j][0]
                    union(x, y)

        components = set()
        for i in range(n):
            x, _ = stones[i]
            p = find(x)
            components.add(p)

        return n - len(components)