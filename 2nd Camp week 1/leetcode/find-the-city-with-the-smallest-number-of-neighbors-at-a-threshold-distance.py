class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[20000] * n for _ in range(n)]
        
        for u, v, w in edges:
            if w <= distanceThreshold:
                matrix[u][v] = w
                matrix[v][u] = w
        
        for i in range(n):
            matrix[i][i] = 0
        
        for bn in range(n):
            for u in range(n):
                for v in range(n):
                    if matrix[u][bn] + matrix[bn][v] <= distanceThreshold:
                        matrix[u][v] = min(matrix[u][v], matrix[u][bn] + matrix[bn][v])
        
        answer, comp = 0, 200

        for i in range(n):
            count = 0
            for j in range(n):
                if matrix[i][j] != 0 and matrix[i][j] != 20000:
                    count += 1
            
            if count <= comp:
                answer = i
                comp = count

        return answer        