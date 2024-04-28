class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        cycle = -1

        visited = [0 for _ in edges]
        time = 1
        
        for node in range(len(edges)):
            if visited[node] > 0:
                continue
            start = time
            
            while node != -1 and visited[node] == 0:
                visited[node] = time
                time += 1
                node = edges[node]
            
            if node != -1 and visited[node] >= start:
                cycle = max(cycle, time - visited[node])
        
        return cycle