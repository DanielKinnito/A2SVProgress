class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        for i, edges in enumerate(graph):
            adj_list[i] = edges
        
        answer = []
        n = len(graph)

        def dfs(node, path):
            if node == n - 1:
                answer.append(path.copy())
                return
            
            for ne in adj_list[node]:
                path.append(ne)
                dfs(ne, path)
                path.pop()
        
        dfs(0, [0])
        return answer