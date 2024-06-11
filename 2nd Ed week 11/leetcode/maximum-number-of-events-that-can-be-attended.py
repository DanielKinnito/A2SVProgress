class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        
        events.sort(reverse=True)
        day = 0
        answer = 0
        heap = []
        
        while events or heap:
            while heap and heap[0] < day:
                heappop(heap)
            
            while events and events[-1][0] <= day:
                heappush(heap, events.pop()[1])
                
            if heap:
                heappop(heap)
                answer += 1
                
            day += 1
        
        return answer