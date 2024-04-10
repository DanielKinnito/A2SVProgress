class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [-1] * n
        
        reds = defaultdict(list)
        for edge in redEdges:
            reds[edge[0]].append(edge[1])
        
        blues = defaultdict(list)
        for edge in blueEdges:
            blues[edge[0]].append(edge[1])
            
        visited = set((0, None))
        
        que = deque()
        que.append([0, 0, None])

        while que:
            node, dist, color = que.popleft()

            if answer[node] == -1:
                answer[node] = dist

            if color != 'Blue':
                for neighbor in blues[node]:
                    if (neighbor, 'Blue') not in visited:
                        visited.add((neighbor, 'Blue'))
                        que.append([neighbor, dist + 1, 'Blue'])
            
            if color != 'Red':
                for neighbor in reds[node]:
                    if (neighbor, 'Red') not in visited:
                        visited.add((neighbor, 'Red'))
                        que.append([neighbor, dist + 1, 'Red'])
        
        return answer