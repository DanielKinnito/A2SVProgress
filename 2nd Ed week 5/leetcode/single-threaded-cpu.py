class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        arr = [[*task, i] for i, task in enumerate(tasks)]
        answer = []
        heap = []
        first = 0
        time = 0

        arr.sort()

        while first < n or heap:
            if not heap:
                time = max(time, arr[first][0])

            while first < n and time >= arr[first][0]:
                heapq.heappush(heap, (arr[first][1], arr[first][2]))
                first += 1
            
            proc, idx = heapq.heappop(heap)
            
            time += proc
            answer.append(idx)

        return answer