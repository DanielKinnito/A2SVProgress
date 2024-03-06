class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        length = len(weights)
        
        def canDeliver(mid):
            count = 1
            temp_sum = 0
            for i in range(length):
                if temp_sum + weights[i] > mid:
                    count += 1
                    temp_sum = 0
                temp_sum += weights[i]

            if count <= days:
                return True
            return False
        
        low = max(weights)
        high = sum(weights)

        while low <= high:
            middle = (low + high) //2
            if canDeliver(middle):
                high = middle - 1
            else:
                low = middle + 1
        
        return low