class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(idx):
            if idx >= n:
                return 0
                                    
            if idx not in memo:
                memo[idx] = 1   
                for j in range(idx, n):
                    if nums[j] > nums[idx]:
                        memo[idx] = max(1 + dp(j), memo[idx])

            return memo[idx]
        memo = {}
        n = len(nums)
        answer = -1
        
        for i in range(n):
            answer = max(answer, dp(i))
        
        return answer