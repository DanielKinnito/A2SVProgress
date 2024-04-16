class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in range(len(piles)):
            piles[i] = - piles[i]
            heappush(heap, piles[i])
        
        for _ in range(k):
            num = heappop(heap)
            heappush(heap, num // 2)
        
        total = - sum(heap)
        return total