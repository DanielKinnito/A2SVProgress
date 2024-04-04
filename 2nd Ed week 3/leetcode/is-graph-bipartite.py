class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        all_nodes = [-1] * length

        def dfs(node, color):
            all_nodes[node] = color

            for neighbor in graph[node]:
                if all_nodes[neighbor] == color:
                    return False
                elif all_nodes[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False

            return True

        for node in range(length):
            if all_nodes[node] == -1:
                if not dfs(node, 0):
                    return False

        return True