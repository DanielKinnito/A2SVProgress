class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        temp = list(zip(capital,profits))        
        temp.sort()
        ptr = 0
        heap = []
        for _ in range(k):
            while ptr < len(profits) and temp[ptr][0] <= w:
                heappush(heap, -temp[ptr][1])
                ptr += 1
            if heap: w += -heappop(heap)
        return w 