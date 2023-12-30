class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0  
        nums.sort()

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != nums[i - 1]: # if element dif from prev
                ans += len(nums) - i # add the count of pairs (i, j) for all j > i
                
        return ans