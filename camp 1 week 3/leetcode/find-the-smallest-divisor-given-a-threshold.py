class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def canBeDevided(mid):
            result = 0
            for num in nums:
                result += ceil(num/mid)
            if result <= threshold:
                return True
            return False
        
        low = 1
        high = max(nums)
        while low <= high:
            middle = (low + high) // 2

            if canBeDevided(middle):
                high = middle - 1
            else:
                low = middle + 1
        
        return low