from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def dp(num):
            if num not in memo:
                take = num * count[num] + dp(num + 2)
                skip = dp(num + 1)
                memo[num] = max(take, skip)
            
            return memo[num]

        count = Counter(nums)
        max_num = max(nums)

        memo = {}
        memo[max_num + 1] = 0
        memo[max_num + 2] = 0

        return dp(min(nums))