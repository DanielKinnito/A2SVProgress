class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet) 
        rst, degree, graph = list(range(n)), [0] * n, [[] for _ in range(n)]

        for i, j in richer: 
            degree[j] += 1
            graph[i].append(j)
        q = collections.deque([])
        for i in range(n):
            if degree[i] == 0: q.append(i)
        
        while q:
            i = q.popleft()
            for j in graph[i]:
                if quiet[rst[i]] < quiet[rst[j]]: rst[j] = rst[i]

                degree[j] -= 1
                if degree[j] == 0: q.append(j)
        return rst