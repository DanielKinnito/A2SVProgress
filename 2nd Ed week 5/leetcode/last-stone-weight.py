class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            stones[i] = -stones[i]
            heappush(heap, stones[i])
        
        length = len(heap)
        while length > 1:
            y = - heappop(heap)
            x = - heappop(heap)
            
            if x != y:
                y -= x
                length -= 1
                heappush(heap, -y)
            elif x == y:
                length -= 2
        
        if heap: return -heap[0]
        return 0