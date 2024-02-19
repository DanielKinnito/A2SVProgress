class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 0
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + i* (nums[i] - nums[i - 1])

        suffix[n - 1] = 0
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + (n - 1 - i)* (nums[i + 1] - nums[i])
        
        for i in range(n):
            answer[i] = prefix[i] + suffix[i]
        
        return answer