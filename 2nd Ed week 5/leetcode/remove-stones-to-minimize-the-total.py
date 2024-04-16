class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = - piles[i]
        
        heapify(piles)

        for _ in range(k):
            num = heappop(piles)
            heappush(piles, num // 2)
        
        total = - sum(piles)
        return total