class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def finess(idx):
            if idx == 0:
                return nums[idx]
            if idx == 1:
                return max(nums[0], nums[idx])
            
            if idx not in memo:
                memo[idx] = max(finess(idx - 1), finess(idx - 2) + nums[idx])
            
            return memo[idx]
        
        return finess(len(nums) - 1)