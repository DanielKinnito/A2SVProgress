class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            stones[i] = -stones[i]
            heappush(heap, stones[i])
        
        while len(heap) > 1:
            y = - heappop(heap)
            x = - heappop(heap)
            
            if x != y:
                y -= x
                heappush(heap, -y)
        
        if heap: return -heap[0]
        return 0