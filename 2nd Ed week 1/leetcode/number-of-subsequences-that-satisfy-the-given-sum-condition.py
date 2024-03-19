class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()

        def subArrays(idx):
            curr_index = bisect_right(nums, target - nums[idx])
            
            if curr_index <= idx:
                if curr_index == idx and nums[idx] + nums[idx] <= target:
                    return 1
                else:                    
                    return 0
            return 2 ** (curr_index - idx - 1)

        count = 0

        for i in range(length):
            added = subArrays(i)
            count += added
        count %= 10 ** 9 + 7
        return count