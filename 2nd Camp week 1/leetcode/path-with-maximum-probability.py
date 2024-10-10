class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]

            graph[u].append((v, w))
            graph[v].append((u, w))

        prob = [0] * n
        prob[start_node] = 1
        in_que = [False] * n

        que = deque([start_node])
        in_que[start_node] = True

        while que:
            node = que.popleft()
            in_que[node] = False

            for v, w in graph[node]:
                if prob[v] < prob[node] * w:
                    prob[v] = prob[node] * w

                    if not in_que[v]:
                        que.append(v)
                        in_que[v] = True
        
        return prob[end_node]