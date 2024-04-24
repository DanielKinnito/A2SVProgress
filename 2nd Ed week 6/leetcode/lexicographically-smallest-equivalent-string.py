class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {ch: ch for ch in s1}
        for ch in s2:
            root[ch] = ch
        for ch in baseStr:
            root[ch] = ch

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
 
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if root[rootX] < root[rootY]:
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        answer = ''
        for i in range(len(baseStr)):
            answer += root[find(baseStr[i])]
        
        return answer