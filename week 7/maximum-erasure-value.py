class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_set = set()
        left, right = 0, 0
        max_sum = 0
        current_sum = 0

        while right < len(nums):
            if nums[right] not in num_set:
                num_set.add(nums[right])
                current_sum += nums[right]
                max_sum = max(max_sum, current_sum)
                right += 1

            else:
                num_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum