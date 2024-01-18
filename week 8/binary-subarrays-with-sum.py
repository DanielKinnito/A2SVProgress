class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        count = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix += num
            count += prefix_count.get(prefix - goal, 0)
            prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

        return count