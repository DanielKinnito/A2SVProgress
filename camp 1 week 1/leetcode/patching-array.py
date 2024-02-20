class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches_count = 0
        i = 0
        missing = 1

        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing *= 2
                patches_count += 1
        
        return patches_count