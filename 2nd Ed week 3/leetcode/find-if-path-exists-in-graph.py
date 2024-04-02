class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for edge in edges:

            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            visited.add(node)
            neighbors = adj[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return False