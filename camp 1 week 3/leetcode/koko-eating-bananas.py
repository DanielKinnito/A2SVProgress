class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        total_pile = sum(piles)
        
        def canEat(mid):
            count = 0
            for i in range(length):
                count += ceil(piles[i] / mid)

            if count <= h:
                return True
            
            return False
        
        low = 1
        high = max(piles)

        while low <= high:
            middle = (low + high) //2
            if canEat(middle):
                high = middle - 1
            else:
                low = middle + 1
        
        return low