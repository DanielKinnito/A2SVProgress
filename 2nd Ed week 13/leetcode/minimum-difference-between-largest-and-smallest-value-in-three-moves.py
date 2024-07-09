class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:return 0
        
        nums.sort()

        temp = []
        temp.append(nums[n-4] - nums[0])
        temp.append(nums[n-3] - nums[1])
        temp.append(nums[n-2] - nums[2])
        temp.append(nums[n-1] - nums[3])

        return min(temp)