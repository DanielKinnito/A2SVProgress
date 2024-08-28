class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        seen = {1}
        count = 0
        last = 1

        while count < n:
            num = heapq.heappop(heap)
            last = num
            
            for factor in [2, 3, 5]:
                new_ugly = num * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
            count += 1

        return last