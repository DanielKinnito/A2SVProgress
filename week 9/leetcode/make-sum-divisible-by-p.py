class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p

        if target_rem == 0:
            return 0
        if total_sum < p:
            return -1

        answer = len(nums)
        prefix = 0
        prefix_dict = {0: -1}

        for i, num in enumerate(nums):
            prefix += num
            prefix %= p
            target = (prefix - target_rem + p) % p

            if target in prefix_dict:
                answer = min(answer, i - prefix_dict[target])

            prefix_dict[prefix] = i

        return -1 if answer == len(nums) else answer