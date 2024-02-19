class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        num_occ = {}
        count = 0

        left = 0
        right = 0

        while right < len(nums):
            num_occ[nums[right]] = num_occ.get(nums[right], 0) + 1
            while len(num_occ) == total_distinct:
                count += len(nums) - right
                num_occ[nums[left]] -= 1
                if num_occ[nums[left]] == 0:
                    del num_occ[nums[left]]
                left += 1
            right += 1
        return count