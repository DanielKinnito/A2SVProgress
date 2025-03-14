class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums.sort()

        memo = {}
        
        def dfs(x: int) -> int:
            if x in memo:
                return memo[x]
            
            next_val = x * x
            if next_val in nums_set:
                memo[x] = 1 + dfs(next_val)
            else:
                memo[x] = 1
            
            return memo[x]
        
        longest = 0
        for num in nums:
            longest = max(longest, dfs(num))
        
        return longest if longest > 1 else -1