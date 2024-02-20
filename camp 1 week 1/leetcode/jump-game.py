class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        step = 0
        for i in range(len(nums) - 1):
            step = max(step, nums[i])
            if step == 0 and nums[i] == 0:
                return False
            step -= 1
        return True