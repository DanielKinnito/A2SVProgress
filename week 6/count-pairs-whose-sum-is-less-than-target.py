class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        answer = 0

        while left < right:
            if nums[left] + nums[right] < target:
                answer += right - left
                left += 1
            
            else:
                right -= 1

        return answer