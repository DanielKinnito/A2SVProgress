class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        answer = float('inf')
        graph = [[] for _ in range(n + 1)]
        que = deque([1])
        seen = {1}

        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))

        while que:
            u = que.popleft()
            for v, d in graph[u]:
                answer = min(answer, d)
                if v in seen:
                    continue
                que.append(v)
                seen.add(v)

        return answer