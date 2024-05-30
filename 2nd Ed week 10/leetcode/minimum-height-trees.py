class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        undirected = defaultdict(list)
        for u, v in edges:
            undirected[u].append(v)
            undirected[v].append(u)
      
        indegree = {}
        que = deque()

        for key, item in undirected.items():
            if len(item) == 1:
                que.append(key)
            indegree[key] = len(item)
        
        while que:
            if n <= 2:
                return list(que)
            for _ in range(len(que)):
                n -= 1
                node = que.popleft()
                for ne in undirected[node]:
                    indegree[ne] -= 1
                    if indegree[ne] == 1:
                        que.append(ne)
        return [0]