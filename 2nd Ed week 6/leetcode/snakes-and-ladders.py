class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        answer = 0
        que = deque([1])
        seen = set()
        array = [0] * (1 + n * n)

        for i in range(n):
            for j in range(n):
                array[(n - 1 - i) * n + (j + 1 if n - i & 1 else n - j)] = board[i][j]
        
        while que:
            answer += 1
            for _ in range(len(que)):
                curr = que.popleft()
                
                for ne in range(curr + 1, min(curr + 6, n * n) + 1):
                    destination = array[ne] if array[ne] > 0 else ne
                    
                    if destination == n * n:
                        return answer
                    
                    if destination in seen:
                        continue
                    
                    que.append(destination)
                    seen.add(destination)

        return -1