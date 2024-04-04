class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            
            if node not in adj_list:
                return

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        provinces = 0
        visited = set()
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i, visited)
                provinces += 1

        return provinces