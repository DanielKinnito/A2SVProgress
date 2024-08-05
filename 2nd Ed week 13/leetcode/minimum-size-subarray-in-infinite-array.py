class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        remaining = target % total
        repeat_length = (target // total) * n
        
        if remaining == 0:
            return repeat_length

        min_length = n
        prefix_sum = 0
        prefix_to_index = {0: -1}

        for i in range(2 * n):
            prefix_sum += nums[i % n]
            if prefix_sum - remaining in prefix_to_index:
                min_length = min(
                    min_length,
                    i - prefix_to_index[prefix_sum - remaining])
            prefix_to_index[prefix_sum] = i

        return -1 if min_length == n else min_length + repeat_length