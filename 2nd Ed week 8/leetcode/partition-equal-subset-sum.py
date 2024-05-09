class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(idx, target):
            if idx >= len(nums) or target <= 0:
                return target == 0
            
            if (idx, target) not in memo:
                memo[(idx, target)] = dp(idx + 1, target - nums[idx]) or dp(idx + 1, target)

            return memo[(idx, target)]
        
        memo = {}
        check = sum(nums)
        return dp(0, check // 2) and check % 2 == 0