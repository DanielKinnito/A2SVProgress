class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        visited.add(start)
        que = deque()
        que.append(start)

        def valid(idx):
            return 0<= idx < len(arr)

        while que:
            index = que.popleft()
            if arr[index] == 0:
                return True

            plus_idx = index + arr[index]
            minus_idx = index - arr[index]
            
            if plus_idx not in visited and valid(plus_idx):
                que.append(plus_idx)
                visited.add(plus_idx)
            if minus_idx not in visited and valid(minus_idx):
                que.append(minus_idx)
                visited.add(minus_idx)
        
        return False