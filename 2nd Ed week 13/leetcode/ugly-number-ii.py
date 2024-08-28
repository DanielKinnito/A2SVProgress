class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        seen = {1}
        answer = []

        while len(answer) < n:
            num = heapq.heappop(heap)
            answer.append(num)
            
            for factor in [2, 3, 5]:
                new_ugly = num * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return answer[-1]