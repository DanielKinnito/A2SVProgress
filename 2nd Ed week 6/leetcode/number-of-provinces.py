class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        answer = len(isConnected)
        parent = {i: i for i in range(1, answer + 1)}
        
        def find(x):
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != root:
                px = parent[x]
                parent[x] = root
                x = px
            
            return root

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    px = find(i + 1)
                    py = find(j + 1)

                    if px != py:
                        parent[px] = parent[py]
                        answer -= 1
        return answer                        