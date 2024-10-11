class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[inf] * n for _ in range(n)]
        
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
        
        neighbors = [inf] * n

        for i in range(n):
            count = 0
            for j in range(n):
                if matrix[i][j] != 0 and matrix[i][j] != inf:
                    count += 1
            neighbors[i] = count
        
        answer, count = 0, neighbors[0]
        for i in range(1, n):
            if neighbors[i] <= count:
                answer = i
                count = neighbors[i]
                
        return answer