class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = defaultdict(list)
        for i, num in enumerate(manager):
            if num != -1:
                adj_list[num].append(i)
        
        answer = 0
        que = deque()
        que.append((headID, 0))

        while que:
            node, prev_time = que.popleft()
            prev_time += informTime[node]

            answer = max(answer, prev_time)
            
            for ne in adj_list[node]:
                que.append((ne, prev_time))
                
        return answer