class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        self.time = 0
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridgeUtil(self, u, visited, parent, low, disc, bridges):
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc, bridges)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def findBridges(self):
        visited = [False] * self.v
        disc = [inf] * self.v
        low = [inf] * self.v
        parent = [-1] * self.v
        bridges = []

        for i in range(self.v):
            if not visited[i]:
                self.bridgeUtil(i, visited, parent, low, disc, bridges)
        
        return bridges

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        network = Graph(n)

        for u, v in connections:
            network.addEdge(u, v)

        answer = network.findBridges()
        return answer        