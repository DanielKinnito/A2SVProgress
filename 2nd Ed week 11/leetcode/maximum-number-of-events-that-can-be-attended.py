class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        
        events.sort(reverse=True)
        day = 0
        max_events = 0
        heap = []
        
        while events or heap:
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            while events and events[-1][0] <= day:
                heapq.heappush(heap, events.pop()[1])
                
            if heap:
                heapq.heappop(heap)
                max_events += 1
                
            day += 1
        
        return max_events