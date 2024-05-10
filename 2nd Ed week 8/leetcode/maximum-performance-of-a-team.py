class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        min_heap = []
        total_speed = 0
        answer = 0
        
        for eff, spd in engineers:
            if len(min_heap) == k:
                total_speed -= heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, spd)
            total_speed += spd
            
            performance = total_speed * eff
            answer = max(answer, performance)
        
        return answer % MOD