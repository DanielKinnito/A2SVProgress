class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * (n + 1)
        adj_list = defaultdict(list)
        
        for u, v in relations:
            adj_list[u].append(v)
            indegree[v] += 1
        
        que = deque()
        earliest_time = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if indegree[i] == 0:
                que.append(i)
                earliest_time[i] = time[i - 1]
        
        while que:
            node = que.popleft()
            
            for ne in adj_list[node]:
                indegree[ne] -= 1
                earliest_time[ne] = max(earliest_time[ne], earliest_time[node] + time[ne - 1])
                if indegree[ne] == 0:
                    que.append(ne)
        
        return max(earliest_time)