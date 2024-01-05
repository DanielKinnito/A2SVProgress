class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_answer = float('-inf')
        total = sum(nums[:k])

        left = 0
        right = k - 1

        while right < len(nums):
            max_answer = max(max_answer, total/k)

            right += 1

            if right < len(nums):
                total += nums[right]
                total -= nums[left]

                left += 1
        
        return max_answer