class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        prefix = nums[0]
        
        for i in range(1, len(nums)):
            prefix = max(prefix + nums[i], nums[i])
            answer = max(answer, prefix)
            
        return answer