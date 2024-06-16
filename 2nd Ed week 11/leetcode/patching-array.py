class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches_count = 0
        i = 0
        target = 1

        while target <= n:
            if i < len(nums) and nums[i] <= target:
                target += nums[i]
                i += 1
            else:
                target *= 2
                patches_count += 1
        
        return patches_count