class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        nums.sort()
        answer = 0

        for i in range(1, len(nums)):
            answer = max(answer, nums[i] - nums[i - 1])
        
        return answer