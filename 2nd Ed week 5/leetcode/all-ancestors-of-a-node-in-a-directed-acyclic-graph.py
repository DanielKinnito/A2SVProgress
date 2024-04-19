class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [[] for _ in range(n)]

        adj_list = defaultdict(list)
        for edge in edges:
            fr, to = edge
            adj_list[to].append(fr)
        
        def bfs(node):
            visited = set()
            visited.add(node)
            ret = []
            que = deque()
            que.append(node)

            while que:
                node = que.popleft()
                ret.append(node)

                for ne in adj_list[node]:
                    if ne not in visited:
                        visited.add(ne)
                        que.append(ne)
            if len(ret) > 1:
                ret = ret[1:]
                return sorted(ret)
            else:
                return []

        for key in list(adj_list):
            answer[key] = bfs(key)
        
        return answer