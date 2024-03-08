class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        answer = nums[left]

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                answer = min(answer, nums[right])
                left = middle + 1
            else:
                answer = min(answer, nums[middle])
                right = middle - 1

        return answer