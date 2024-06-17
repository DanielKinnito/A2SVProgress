class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        
        for i in range(n):
            if n % (i + 1) == 0:
                answer += (nums[i] * nums[i])

        return answer                