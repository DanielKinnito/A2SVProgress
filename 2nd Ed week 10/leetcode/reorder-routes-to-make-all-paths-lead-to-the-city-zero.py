class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected = defaultdict(list)
        for u, v in connections:
            undirected[u].append(v)
            undirected[v].append(u)
        
        directed = defaultdict(set)
        for u, v in connections:
            directed[u].add(v)
        # print(directed)
        # print(undirected)
        # return 1
        que = deque()
        que.append((0, -1))

        visited = set()
        answer = 0
        while que:
            node, parent = que.popleft()
            if parent in directed and parent not in directed[node]:
                answer += 1
            visited.add(node)
            for ne in undirected[node]:
                if ne not in visited:
                    que.append((ne, node))

        return answer