class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = [0 for _ in range(len(graph))]
        adj_list = defaultdict(list)
        
        for i in range(len(graph)):
            for num in graph[i]:
                adj_list[num].append(i)
                outdegree[i] += 1
        
        que = deque()
        for i in range(len(graph)):
            if outdegree[i] == 0:
                que.append(i)
        
        answer = []
        while que:
            node = que.popleft()
            answer.append(node)

            for ne in adj_list[node]:
                outdegree[ne] -= 1
                if outdegree[ne] == 0:
                    que.append(ne)

        return sorted(answer)