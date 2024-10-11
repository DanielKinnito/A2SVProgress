class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = {i: float('inf') for i in range(n)}
        dist[0] = 0
        
        pq = [(0, 0)] 
        reachable = defaultdict(int)
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, w in graph[u]:
                moves_left = maxMoves - d
                if moves_left > 0:
                    reachable[(u, v)] = min(w, moves_left)
                
                new_dist = d + w + 1
                if new_dist < dist[v] and new_dist <= maxMoves:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
        
        answer = sum(dist[u] <= maxMoves for u in range(n))  # Count reachable nodes
        
        for u, v, w in edges:
            answer += min(w, reachable[(u, v)] + reachable[(v, u)])
        
        return answer
